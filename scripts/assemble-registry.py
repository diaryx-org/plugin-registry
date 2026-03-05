#!/usr/bin/env python3
"""Assemble plugins/*.md into a single registry.md and upload to CDN.

Usage:
    python3 scripts/assemble-registry.py [--output registry.md] [--cdn-base https://cdn.diaryx.org]

Walks plugins/*.md, parses YAML frontmatter, validates required fields,
and produces a single registry.md with schema_version 2.
"""

import argparse
import sys
import re
import json
from pathlib import Path
from urllib.parse import urlparse

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml is required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


REQUIRED_FIELDS = ["title", "description", "id", "version", "author", "license", "repository"]
CANONICAL_ID_RE = re.compile(r"^[a-z][a-z0-9]*(\.[a-z][a-z0-9]*)*$")


def normalize_sha256(value: str) -> str:
    return value.strip().lower().removeprefix("sha256:")


def artifact_filename_from_url(url: str, plugin_id: str) -> str:
    parsed = urlparse(url)
    name = Path(parsed.path).name
    if name:
        return name
    return f"{plugin_id.replace('.', '_')}.wasm"


def parse_frontmatter(path: Path) -> tuple[dict, str]:
    """Parse YAML frontmatter and body from a markdown file."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"{path}: missing YAML frontmatter")

    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"{path}: malformed frontmatter (no closing ---)")

    meta = yaml.safe_load(parts[1])
    body = parts[2].strip()
    return meta, body


def validate_plugin(meta: dict, path: Path) -> list[str]:
    """Validate plugin metadata. Returns list of errors."""
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in meta or not meta[field]:
            errors.append(f"{path}: missing required field '{field}'")

    plugin_id = meta.get("id", "")
    if not CANONICAL_ID_RE.match(plugin_id):
        errors.append(f"{path}: invalid plugin ID '{plugin_id}' (must match {CANONICAL_ID_RE.pattern})")

    if "artifact" in meta:
        artifact = meta["artifact"]
        if isinstance(artifact, dict):
            # Warn if artifact fields are empty (placeholder)
            if not artifact.get("url"):
                print(f"  WARN: {path}: artifact.url is empty (placeholder)", file=sys.stderr)
        else:
            errors.append(f"{path}: 'artifact' must be a mapping")

    return errors


def assemble_registry(
    plugins_dir: Path,
    cdn_base: str,
    rewrite_artifact_urls: bool = False,
) -> tuple[dict, list[dict], list[dict]]:
    """Assemble all plugin entries into registry YAML and markdown."""
    entries = []
    all_errors = []
    artifact_plan: list[dict] = []

    for md_file in sorted(plugins_dir.glob("*.md")):
        try:
            meta, body = parse_frontmatter(md_file)
        except ValueError as e:
            all_errors.append(str(e))
            continue

        errors = validate_plugin(meta, md_file)
        all_errors.extend(errors)
        if errors:
            continue

        entry = {
            "id": meta["id"],
            "name": meta["title"],
            "version": meta["version"],
            "description": meta["description"],
            "author": meta["author"],
            "license": meta["license"],
            "repository": meta["repository"],
            "categories": meta.get("categories", []),
            "tags": meta.get("tags", []),
            "capabilities": meta.get("capabilities", []),
            "summary": body or meta["description"],
        }

        if "artifact" in meta and isinstance(meta["artifact"], dict):
            artifact = dict(meta["artifact"])
            source_url = str(artifact.get("url") or "").strip()
            if rewrite_artifact_urls and source_url:
                filename = artifact_filename_from_url(source_url, meta["id"])
                s3_key = f"plugins/artifacts/{meta['id']}/{meta['version']}/{filename}"
                cdn_url = f"{cdn_base.rstrip('/')}/{s3_key}"
                artifact_plan.append(
                    {
                        "id": meta["id"],
                        "version": meta["version"],
                        "filename": filename,
                        "source_url": source_url,
                        "cdn_url": cdn_url,
                        "s3_key": s3_key,
                        "sha256": normalize_sha256(str(artifact.get("sha256", ""))),
                        "size": artifact.get("size"),
                    }
                )
                artifact["url"] = cdn_url

            entry["artifact"] = artifact

        if "ui" in meta:
            entry["ui"] = meta["ui"]

        if "cli" in meta:
            entry["cli"] = meta["cli"]

        if "requested_permissions" in meta:
            entry["requested_permissions"] = meta["requested_permissions"]

        entries.append(entry)

    if all_errors:
        print("ERRORS:", file=sys.stderr)
        for err in all_errors:
            print(f"  {err}", file=sys.stderr)
        sys.exit(1)

    # Build registry
    registry_meta = {
        "schema_version": 2,
        "generated_at": None,  # filled by CI
        "cdn_base": cdn_base,
        "plugins": entries,
    }

    # Add timestamp
    from datetime import datetime, timezone
    registry_meta["generated_at"] = datetime.now(timezone.utc).isoformat()

    return registry_meta, entries, artifact_plan


def write_registry_md(registry_meta: dict, output: Path):
    """Write registry.md with YAML frontmatter."""
    yaml_str = yaml.dump(registry_meta, default_flow_style=False, sort_keys=False, allow_unicode=True)

    body_lines = [f"# Diaryx Plugin Registry", ""]
    body_lines.append(f"Generated at {registry_meta['generated_at']}")
    body_lines.append("")
    body_lines.append(f"**{len(registry_meta['plugins'])}** plugins available.")
    body_lines.append("")

    for plugin in registry_meta["plugins"]:
        body_lines.append(f"## {plugin['name']}")
        body_lines.append(f"**ID:** `{plugin['id']}` | **Version:** {plugin['version']}")
        body_lines.append(f"{plugin.get('summary', plugin['description'])}")
        body_lines.append("")

    content = f"---\n{yaml_str}---\n\n" + "\n".join(body_lines) + "\n"
    output.write_text(content, encoding="utf-8")
    print(f"Wrote {output} ({len(registry_meta['plugins'])} plugins)")


def write_artifact_plan(plan: list[dict], output: Path):
    output.write_text(json.dumps(plan, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote {output} ({len(plan)} artifacts)")


def main():
    parser = argparse.ArgumentParser(description="Assemble Diaryx plugin registry")
    parser.add_argument("--plugins-dir", default="plugins", help="Directory containing plugin .md files")
    parser.add_argument("--output", default="registry.md", help="Output registry file")
    parser.add_argument("--cdn-base", default="https://cdn.diaryx.org", help="CDN base URL")
    parser.add_argument(
        "--rewrite-artifact-urls",
        action="store_true",
        help="Rewrite artifact.url entries to CDN paths and emit an upload plan",
    )
    parser.add_argument(
        "--artifact-plan-out",
        default=None,
        help="Optional JSON file for artifact upload plan",
    )
    args = parser.parse_args()

    plugins_dir = Path(args.plugins_dir)
    if not plugins_dir.is_dir():
        print(f"ERROR: plugins directory not found: {plugins_dir}", file=sys.stderr)
        sys.exit(1)

    registry_meta, entries, artifact_plan = assemble_registry(
        plugins_dir,
        args.cdn_base,
        rewrite_artifact_urls=args.rewrite_artifact_urls,
    )
    write_registry_md(registry_meta, Path(args.output))
    if args.artifact_plan_out:
        write_artifact_plan(artifact_plan, Path(args.artifact_plan_out))

    # Verify roundtrip
    parsed_meta, _ = parse_frontmatter(Path(args.output))
    assert parsed_meta["schema_version"] == 2, "schema_version mismatch"
    assert len(parsed_meta["plugins"]) == len(entries), "plugin count mismatch"
    print("Verification passed.")


if __name__ == "__main__":
    main()

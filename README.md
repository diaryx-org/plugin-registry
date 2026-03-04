# Diaryx Plugin Registry

Central registry for all official and community Diaryx plugins. This repo is the single source of truth for the plugin marketplace.

## How it works

Each plugin has a metadata file in `plugins/` (e.g., `plugins/diaryx.math.md`). On push to `main`, the CI workflow assembles all entries into a single `registry.md` and uploads it to the CDN.

## Plugin entry format

Each `plugins/{id}.md` file uses YAML frontmatter with the `PluginWorkspaceMetadata` schema:

```yaml
---
title: "Plugin Name"
description: "What it does"
id: "diaryx.example"
version: "1.0.0"
author: "Author Name"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-example"
categories: ["category"]
tags: ["tag1", "tag2"]
capabilities: ["custom_commands"]
artifact:
  url: "https://github.com/diaryx-org/plugin-example/releases/download/v1.0.0/plugin.wasm"
  sha256: "abc123..."
  size: 12345
  published_at: "2026-03-01T00:00:00Z"
---

Short description of the plugin for the marketplace listing.
```

## Contributing a plugin

1. Create your plugin repo (see [plugin development docs](https://github.com/diaryx-org/diaryx))
2. Build and publish a GitHub Release with the `.wasm` artifact
3. Open a PR to this repo adding your `plugins/{id}.md` file
4. CI will validate the entry and merge will publish to the CDN

## Scripts

- `scripts/assemble-registry.py` — Assembles `plugins/*.md` into `registry.md`

## License

PolyForm Shield 1.0.0

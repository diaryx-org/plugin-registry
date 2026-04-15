---
title: "Publish"
description: "Export and publish content with optional format conversion"
id: "diaryx.publish"
version: "0.2.10"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-publish"
categories: ["publish", "export"]
tags: ["publish", "export", "html"]
capabilities: ["workspace_events", "custom_commands"]
artifact:
  url: "https://github.com/diaryx-org/diaryx/releases/download/diaryx.publish/v0.2.10/diaryx_publish_extism.wasm"
  sha256: "c525db421ac297af6b6d73c75f72efefdb2ce8ed82c5409e5dd507ef08d32d63"
  size: 2237262
  published_at: "2026-04-15T05:52:20Z"
ui:
  - slot: SidebarTab
    id: publish-panel
    label: "Publish"
  - slot: CommandPaletteItem
    id: publish-export
    label: "Export..."
  - slot: CommandPaletteItem
    id: publish-site
    label: "Publish Site"
cli:
  - name: publish
    about: "Publish workspace as HTML"
  - name: preview
    about: "Preview published workspace"
requested_permissions:
  defaults:
    read_files:
      include: ["all"]
    edit_files:
      include: ["all"]
    create_files:
      include: ["all"]
    http_requests:
      include: ["unpkg.com"]
    plugin_storage:
      include: ["all"]
  reasons:
    read_files: "Read workspace entries and attachments while building export output."
    edit_files: "Update generated publish artifacts during export and preview workflows."
    create_files: "Create exported HTML, assets, and converted output files."
    http_requests: "Download optional converter WASM modules used for format conversion."
    plugin_storage: "Cache downloaded converter modules between runs."
---

Export and publish workspaces.

---
title: "Publish"
description: "Export and publish content with optional format conversion"
id: "diaryx.publish"
version: "0.1.3"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-publish"
categories: ["publish", "export"]
tags: ["publish", "export", "html"]
capabilities: ["workspace_events", "custom_commands"]
artifact:
  url: "https://github.com/diaryx-org/plugin-publish/releases/download/v0.1.3/diaryx_publish_extism.wasm"
  sha256: "b83a54b0e02990d11fbe021a74a73b7ec9ccb84990af113fd6676aa9107da756"
  size: 1892331
  published_at: "2026-03-15T15:27:19Z"
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
---

Export and publish workspaces.

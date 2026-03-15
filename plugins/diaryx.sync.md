---
title: "Sync"
description: "Real-time CRDT sync across devices"
id: "diaryx.sync"
version: "0.1.4"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-sync"
categories: ["sync", "collaboration"]
tags: ["sync", "crdt", "realtime"]
capabilities: ["workspace_events", "file_events", "crdt_commands", "sync_transport", "custom_commands"]
artifact:
  url: "https://github.com/diaryx-org/plugin-sync/releases/download/v0.1.4/diaryx_sync_extism.wasm"
  sha256: "71e3a9680b51af062679137f1c496614d5bc7590a2e18bf3dc68ff23c6fc2185"
  size: 2397204
  published_at: "2026-03-15T16:12:13Z"
ui:
  - slot: SettingsTab
    id: sync-settings
    label: "Sync"
  - slot: SidebarTab
    id: share
    label: "Share"
  - slot: SidebarTab
    id: snapshots
    label: "Snapshots"
  - slot: SidebarTab
    id: history
    label: "History"
  - slot: StatusBarItem
    id: sync-status
    label: "Sync"
  - slot: WorkspaceProvider
    id: diaryx.sync
    label: "Diaryx Sync"
cli:
  - name: sync
    about: "Sync workspace across devices"
---

Realtime multi-device workspace sync.

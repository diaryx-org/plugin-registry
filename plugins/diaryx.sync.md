---
title: "Sync"
description: "Real-time CRDT sync across devices"
id: "diaryx.sync"
version: "0.1.6"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-sync"
categories: ["sync", "collaboration"]
tags: ["sync", "crdt", "realtime"]
capabilities: ["workspace_events", "file_events", "crdt_commands", "sync_transport", "custom_commands"]
artifact:
  url: "https://github.com/diaryx-org/plugin-sync/releases/download/v0.1.6/diaryx_sync_extism.wasm"
  sha256: "99aac49823ea74190b5f2aed5f8aa3527dcd70a1124bf3be8aed6c5856a5d87d"
  size: 2398613
  published_at: "2026-03-16T18:37:34Z"
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

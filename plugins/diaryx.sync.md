---
title: "Sync"
description: "Real-time CRDT sync across devices"
id: "diaryx.sync"
version: "1.2.1"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-sync"
categories: ["sync", "collaboration"]
tags: ["sync", "crdt", "realtime"]
capabilities: ["workspace_events", "file_events", "crdt_commands", "sync_transport", "custom_commands"]
artifact:
  url: ""
  sha256: ""
  size: 0
  published_at: ""
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

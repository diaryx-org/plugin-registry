---
title: "Sync"
description: "Real-time multi-device sync across Diaryx workspaces"
id: "diaryx.sync"
version: "0.2.17"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-sync"
categories: ["sync", "collaboration"]
tags: ["sync", "crdt", "realtime"]
capabilities: ["workspace_events", "file_events", "crdt_commands", "sync_transport", "custom_commands"]
artifact:
  url: "https://github.com/diaryx-org/diaryx/releases/download/diaryx.sync/v0.2.17/diaryx_sync_extism.wasm"
  sha256: "933e94a1a150043101813b0e3ee407808abec3cb389ed2d725e1795014aea2f5"
  size: 764338
  published_at: "2026-04-15T18:16:35Z"
ui:
  - slot: SettingsTab
    id: sync-settings
    label: "Sync"
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
requested_permissions:
  defaults:
    plugin_storage:
      include: ["all"]
    http_requests:
      include: ["all"]
    read_files:
      include: ["all"]
    edit_files:
      include: ["all"]
    create_files:
      include: ["all"]
    delete_files:
      include: ["all"]
  reasons:
    plugin_storage: "Store sync configuration and CRDT state."
    http_requests: "Communicate with the configured sync server."
    read_files: "Read workspace files for snapshotting, reconciliation, and sync."
    edit_files: "Apply remote changes to existing workspace files."
    create_files: "Create files received from remote sync or restored from snapshots."
    delete_files: "Delete files removed by remote sync or snapshot restore operations."
---

Realtime multi-device workspace sync, snapshots, history, and workspace-provider flows.

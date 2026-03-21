---
title: "Live Share"
description: "Real-time guest sharing for Diaryx workspaces"
id: "diaryx.share"
version: "0.2.0"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-share"
categories: ["collaboration"]
tags: ["share", "realtime", "guest"]
capabilities: ["workspace_events", "file_events", "sync_transport", "custom_commands"]
artifact:
  url: "https://github.com/diaryx-org/plugin-share/releases/download/v0.2.0/diaryx_share_extism.wasm"
  sha256: "c31b45a021901e2e2cb788f331a0839ec3a6bdbe39b6c9e1ed63b24f8384c876"
  size: 1053360
  published_at: "2026-03-21T22:44:46Z"
ui:
  - slot: SettingsTab
    id: share-settings
    label: "Live Share"
  - slot: SidebarTab
    id: share
    label: "Share"
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
    execute_commands:
      include:
        - "diaryx.sync:PrepareLiveShareRuntime"
        - "diaryx.sync:ConnectLiveShareSession"
        - "diaryx.sync:DisconnectLiveShareSession"
  reasons:
    plugin_storage: "Store live-share session state."
    http_requests: "Create, join, update, and end share sessions against the Diaryx server."
    read_files: "Read workspace files when building a temporary share snapshot."
    edit_files: "Apply remote edits during standalone live-share sessions."
    create_files: "Create files received during standalone live-share sessions."
    delete_files: "Delete files removed during standalone live-share sessions."
    execute_commands: "Reuse diaryx.sync runtime commands when sync is installed and available."
---

Realtime live sharing for Diaryx workspaces, with optional runtime reuse through `diaryx.sync`.

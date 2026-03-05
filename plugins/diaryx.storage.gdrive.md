---
title: "Google Drive Storage"
description: "Google Drive as a filesystem backend"
id: "diaryx.storage.gdrive"
version: "0.1.0"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-storage-gdrive"
categories: ["storage", "integration"]
tags: ["google-drive", "storage", "cloud"]
capabilities: ["custom_commands"]
artifact:
  url: "https://github.com/diaryx-org/plugin-storage-gdrive/releases/download/v0.1.0/diaryx_storage_gdrive_extism.wasm"
  sha256: "d1819d2b59f9b2f7abce05b9614ca8485558869bb146e5acb03c69fc7ad06acd"
  size: 362804
  published_at: "2026-03-05T01:14:10Z"
ui:
  - slot: StorageProvider
    id: diaryx.storage.gdrive
    label: "Google Drive"
  - slot: SettingsTab
    id: gdrive-storage-settings
    label: "Google Drive"
---

Google Drive storage backend.

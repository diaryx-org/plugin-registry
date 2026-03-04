---
title: "Google Drive Storage"
description: "Google Drive as a filesystem backend"
id: "diaryx.storage.gdrive"
version: "1.2.1"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-storage-gdrive"
categories: ["storage", "integration"]
tags: ["google-drive", "storage", "cloud"]
capabilities: ["custom_commands"]
artifact:
  url: ""
  sha256: ""
  size: 0
  published_at: ""
ui:
  - slot: StorageProvider
    id: diaryx.storage.gdrive
    label: "Google Drive"
  - slot: SettingsTab
    id: gdrive-storage-settings
    label: "Google Drive"
---

Google Drive storage backend.

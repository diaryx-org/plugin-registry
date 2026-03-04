---
title: "S3 Storage"
description: "S3-compatible object storage as a filesystem backend"
id: "diaryx.storage.s3"
version: "1.2.1"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-storage-s3"
categories: ["storage", "integration"]
tags: ["s3", "storage", "cloud"]
capabilities: ["custom_commands"]
artifact:
  url: ""
  sha256: ""
  size: 0
  published_at: ""
ui:
  - slot: StorageProvider
    id: diaryx.storage.s3
    label: "Amazon S3"
  - slot: SettingsTab
    id: s3-storage-settings
    label: "S3 Storage"
---

S3-compatible storage backend.

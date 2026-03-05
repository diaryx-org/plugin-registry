---
title: "S3 Storage"
description: "S3-compatible object storage as a filesystem backend"
id: "diaryx.storage.s3"
version: "0.1.0"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-storage-s3"
categories: ["storage", "integration"]
tags: ["s3", "storage", "cloud"]
capabilities: ["custom_commands"]
artifact:
  url: "https://github.com/diaryx-org/plugin-storage-s3/releases/download/v0.1.0/diaryx_storage_s3_extism.wasm"
  sha256: "49f7ba4f3fd698f87d2cc6cf2d1d045a8604d34d2c8eb7e93543c1fff62117f0"
  size: 393864
  published_at: "2026-03-05T01:14:09Z"
ui:
  - slot: StorageProvider
    id: diaryx.storage.s3
    label: "Amazon S3"
  - slot: SettingsTab
    id: s3-storage-settings
    label: "S3 Storage"
---

S3-compatible storage backend.

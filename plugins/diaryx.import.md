---
title: "Import"
description: "Import entries from Day One, Markdown directories, and other formats"
id: "diaryx.import"
version: "0.1.4"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-import"
categories: ["import", "migration"]
tags: ["import", "day-one", "markdown"]
capabilities: ["custom_commands"]
artifact:
  url: "https://github.com/diaryx-org/plugin-import/releases/download/v0.1.4/diaryx_import_extism.wasm"
  sha256: "387849493b7b19851046b9e9ab7c20e7eb391f4bcf01639d0ba1c1a99f3109ae"
  size: 1224198
  published_at: "2026-03-16T18:37:15Z"
ui:
  - slot: SettingsTab
    id: import-settings
    label: "Import"
cli:
  - name: import
    about: "Import entries from external formats"
requested_permissions:
  defaults:
    read_files:
      include: ["all"]
    edit_files:
      include: ["all"]
    create_files:
      include: ["all"]
  reasons:
    read_files: "Read existing entries during import."
    edit_files: "Update entry metadata during import."
    create_files: "Create new entries from imported data."
---

Import entries from external formats.

---
title: "Import"
description: "Import entries from Day One, Markdown directories, and other formats"
id: "diaryx.import"
version: "0.1.0"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-import"
categories: ["import", "migration"]
tags: ["import", "day-one", "markdown"]
capabilities: ["custom_commands"]
artifact:
  url: "https://github.com/diaryx-org/plugin-import/releases/download/v0.1.0/diaryx_import_extism.wasm"
  sha256: "55adc8cb91da4548e2a3250e9b086c966548cd2ee0f4673f608960f6741dca26"
  size: 1083363
  published_at: "2026-03-05T00:20:18Z"
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

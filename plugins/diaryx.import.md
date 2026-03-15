---
title: "Import"
description: "Import entries from Day One, Markdown directories, and other formats"
id: "diaryx.import"
version: "0.1.2"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-import"
categories: ["import", "migration"]
tags: ["import", "day-one", "markdown"]
capabilities: ["custom_commands"]
artifact:
  url: "https://github.com/diaryx-org/plugin-import/releases/download/v0.1.2/diaryx_import_extism.wasm"
  sha256: "5ace5867e02ab2b6582449094d39bce35b28f3119d0682620db4eb6f94375e5c"
  size: 1222285
  published_at: "2026-03-15T16:11:44Z"
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

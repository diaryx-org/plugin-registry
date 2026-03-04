---
title: "Import"
description: "Import entries from Day One, Markdown directories, and other formats"
id: "diaryx.import"
version: "1.2.1"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-import"
categories: ["import", "migration"]
tags: ["import", "day-one", "markdown"]
capabilities: ["custom_commands"]
artifact:
  url: ""
  sha256: ""
  size: 0
  published_at: ""
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

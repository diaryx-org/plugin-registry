---
title: "Daily"
description: "Daily entry plugin with date hierarchy, navigation, and CLI surface"
id: "diaryx.daily"
version: "0.1.1"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-daily"
categories: ["productivity", "journaling"]
tags: ["daily", "journal", "calendar"]
capabilities: ["workspace_events", "custom_commands"]
artifact:
  url: "https://github.com/diaryx-org/plugin-daily/releases/download/v0.1.1/diaryx_daily_extism.wasm"
  sha256: "0ed812cf8e3f315677929186761c79e33fe27b105fd9a5691968259bccdc79da"
  size: 834429
  published_at: "2026-03-12T03:19:54Z"
ui:
  - slot: SidebarTab
    id: daily-panel
    label: "Daily"
  - slot: CommandPaletteItem
    id: daily-open-today
    label: "Open Today's Entry"
  - slot: CommandPaletteItem
    id: daily-open-yesterday
    label: "Open Yesterday's Entry"
cli:
  - name: daily
    about: "Daily entry commands"
---

Daily entry workflow and navigation.

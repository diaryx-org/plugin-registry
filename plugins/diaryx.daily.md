---
title: "Daily"
description: "Daily entry plugin with date hierarchy, navigation, and CLI surface"
id: "diaryx.daily"
version: "0.1.3"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-daily"
categories: ["productivity", "journaling"]
tags: ["daily", "journal", "calendar"]
capabilities: ["workspace_events", "custom_commands"]
artifact:
  url: "https://github.com/diaryx-org/plugin-daily/releases/download/v0.1.3/diaryx_daily_extism.wasm"
  sha256: "85c5a3e3ede24a0fb9cf9483b7b1272525eab864d1041d5cc16ee8f485d7c069"
  size: 887416
  published_at: "2026-03-15T16:11:24Z"
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

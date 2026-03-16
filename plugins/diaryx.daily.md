---
title: "Daily"
description: "Daily entry plugin with date hierarchy, navigation, and CLI surface"
id: "diaryx.daily"
version: "0.1.6"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-daily"
categories: ["productivity", "journaling"]
tags: ["daily", "journal", "calendar"]
capabilities: ["workspace_events", "custom_commands"]
artifact:
  url: "https://github.com/diaryx-org/plugin-daily/releases/download/v0.1.6/diaryx_daily_extism.wasm"
  sha256: "8d157c1d2af6fb7c0810776263f0995c0b563def7931cbcb53f186ab34e38992"
  size: 889485
  published_at: "2026-03-16T18:44:41Z"
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

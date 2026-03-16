---
title: "Daily"
description: "Daily entry plugin with date hierarchy, navigation, and CLI surface"
id: "diaryx.daily"
version: "0.1.7"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-daily"
categories: ["productivity", "journaling"]
tags: ["daily", "journal", "calendar"]
capabilities: ["workspace_events", "custom_commands"]
artifact:
  url: "https://github.com/diaryx-org/plugin-daily/releases/download/v0.1.7/diaryx_daily_extism.wasm"
  sha256: "3f2a6c4c2c09081e2590f4226954d2c65f2c3322471135145f46d69ed02f4942"
  size: 905436
  published_at: "2026-03-16T19:41:22Z"
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

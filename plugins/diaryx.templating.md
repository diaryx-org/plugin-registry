---
title: "Templating"
description: "Creation-time templates and render-time body templating with Handlebars"
id: "diaryx.templating"
version: "0.1.2"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-templating"
categories: ["productivity", "editor"]
tags: ["templates", "handlebars", "workflow"]
capabilities: ["workspace_events", "custom_commands"]
artifact:
  url: "https://github.com/diaryx-org/plugin-templating/releases/download/v0.1.2/diaryx_templating_extism.wasm"
  sha256: "299db688d7c1a0f523974cd39198acb7f6624081522ccf0c5f9aee3444b5b1a6"
  size: 1018152
  published_at: "2026-03-15T15:26:54Z"
ui:
  - slot: SettingsTab
    id: templating-settings
    label: "Templates"
  - slot: EditorExtension
    id: templateVariable
  - slot: EditorExtension
    id: conditionalBlock
  - slot: BlockPickerItem
    id: templating-if-else
    label: "If / Else"
  - slot: BlockPickerItem
    id: templating-for-audience
    label: "For Audience"
---

Creation-time and render-time templating.

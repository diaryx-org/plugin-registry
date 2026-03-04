---
title: "Templating"
description: "Creation-time templates and render-time body templating with Handlebars"
id: "diaryx.templating"
version: "1.2.1"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-templating"
categories: ["productivity", "editor"]
tags: ["templates", "handlebars", "workflow"]
capabilities: ["workspace_events", "custom_commands"]
artifact:
  url: ""
  sha256: ""
  size: 0
  published_at: ""
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

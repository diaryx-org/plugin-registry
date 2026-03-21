---
title: "Templating"
description: "Creation-time templates and render-time body templating with Handlebars"
id: "diaryx.templating"
version: "0.1.5"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-templating"
categories: ["productivity", "editor"]
tags: ["templates", "handlebars", "workflow"]
capabilities: ["workspace_events", "custom_commands"]
artifact:
  url: "https://github.com/diaryx-org/plugin-templating/releases/download/v0.1.5/diaryx_templating_extism.wasm"
  sha256: "f12d0cd5abde477855e3165383bd2a0e50ef4774fa9f929cc7e90ee1a1af1d61"
  size: 1020303
  published_at: "2026-03-16T18:37:09Z"
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
requested_permissions:
  defaults:
    read_files:
      include: ["all"]
    edit_files:
      include: ["all"]
    create_files:
      include: ["all"]
    delete_files:
      include: ["all"]
    plugin_storage:
      include: ["all"]
  reasons:
    read_files: "Read workspace templates from the _templates directory."
    edit_files: "Update existing workspace templates when saving changes."
    create_files: "Create new workspace templates in the _templates directory."
    delete_files: "Remove workspace templates that are no longer needed."
    plugin_storage: "Persist templating plugin configuration for the current workspace."
---

Creation-time and render-time templating.

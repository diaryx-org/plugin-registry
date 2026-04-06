---
title: "Templating"
description: "Creation-time templates and render-time body templating with Handlebars"
id: "diaryx.templating"
version: "0.1.6"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-templating"
categories: ["productivity", "editor"]
tags: ["templates", "handlebars", "workflow"]
capabilities: ["workspace_events", "custom_commands"]
artifact:
  url: "https://github.com/diaryx-org/plugin-templating/releases/download/v0.1.6/diaryx_templating_extism.wasm"
  sha256: "d60f36a1c6b5afd1c885bbd33a031d1deddcfc2be5c86fae5d0a34b5c768bf0e"
  size: 1021019
  published_at: "2026-04-06T22:48:25Z"
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

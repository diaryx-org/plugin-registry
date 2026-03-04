---
title: "AI Assistant"
description: "AI chat assistant powered by OpenAI-compatible APIs"
id: "diaryx.ai"
version: "1.2.1"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-ai"
categories: ["assistant", "writing"]
tags: ["ai", "chat", "assistant"]
capabilities: ["custom_commands"]
artifact:
  url: ""
  sha256: ""
  size: 0
  published_at: ""
ui:
  - slot: ToolbarButton
    id: ai-chat-toggle
    label: "AI Assistant"
  - slot: SidebarTab
    id: ai-chat
    label: "AI"
  - slot: SettingsTab
    id: ai-settings
    label: "AI"
requested_permissions:
  defaults:
    http_requests:
      include: ["openrouter.ai"]
    plugin_storage:
      include: ["all"]
  reasons:
    http_requests: "Send chat requests to the configured OpenAI-compatible API endpoint."
    plugin_storage: "Persist conversation history and plugin settings between sessions."
---

Chat assistant plugin for Diaryx.

---
title: "AI Assistant"
description: "AI chat assistant powered by OpenAI-compatible APIs"
id: "diaryx.ai"
version: "0.1.0"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-ai"
categories: ["assistant", "writing"]
tags: ["ai", "chat", "assistant"]
capabilities: ["custom_commands"]
artifact:
  url: "https://github.com/diaryx-org/plugin-ai/releases/download/v0.1.0/diaryx_ai_extism.wasm"
  sha256: "52dc1d255a88c571199e327fa968aa9d88e2cae9bb9e8f6afbeb1b11570d104c"
  size: 379567
  published_at: "2026-03-05T00:18:50Z"
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

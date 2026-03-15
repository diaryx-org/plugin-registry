---
title: "AI Assistant"
description: "AI chat assistant powered by OpenAI-compatible APIs"
id: "diaryx.ai"
version: "0.1.1"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-ai"
categories: ["assistant", "writing"]
tags: ["ai", "chat", "assistant"]
capabilities: ["custom_commands"]
artifact:
  url: "https://github.com/diaryx-org/plugin-ai/releases/download/v0.1.1/diaryx_ai_extism.wasm"
  sha256: "5cd021164bf4d11d91faeaa3ac2479e93035359aab1f7c2c7aa56601c6f4cbaa"
  size: 445085
  published_at: "2026-03-15T15:26:25Z"
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

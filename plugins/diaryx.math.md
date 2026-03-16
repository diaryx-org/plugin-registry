---
title: "Math"
description: "LaTeX math rendering with inline ($...$) and block ($$...$$) support"
id: "diaryx.math"
version: "0.1.6"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-math"
categories: ["editor", "formatting"]
tags: ["math", "latex", "editor"]
capabilities: ["editor_extension"]
artifact:
  url: "https://github.com/diaryx-org/plugin-math/releases/download/v0.1.6/diaryx_math_extism.wasm"
  sha256: "ee9095ffbecc850de7e192ababaebf3748667bab95060c04107893649767d0cd"
  size: 425883
  published_at: "2026-03-16T18:44:31Z"
ui:
  - slot: EditorExtension
    id: mathInline
    label: "Math"
  - slot: EditorExtension
    id: mathBlock
    label: "Math Block"
---

Render inline and block LaTeX.

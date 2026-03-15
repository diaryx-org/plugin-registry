---
title: "Math"
description: "LaTeX math rendering with inline ($...$) and block ($$...$$) support"
id: "diaryx.math"
version: "0.1.2"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-math"
categories: ["editor", "formatting"]
tags: ["math", "latex", "editor"]
capabilities: ["editor_extension"]
artifact:
  url: "https://github.com/diaryx-org/plugin-math/releases/download/v0.1.2/diaryx_math_extism.wasm"
  sha256: "f9ba2463700d18c3b1e8f7d36f3818fb65047997eb877eb2b31c118bd7f1e440"
  size: 419818
  published_at: "2026-03-15T15:26:31Z"
ui:
  - slot: EditorExtension
    id: mathInline
    label: "Math"
  - slot: EditorExtension
    id: mathBlock
    label: "Math Block"
---

Render inline and block LaTeX.

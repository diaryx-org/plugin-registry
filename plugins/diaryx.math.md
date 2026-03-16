---
title: "Math"
description: "LaTeX math rendering with inline ($...$) and block ($$...$$) support"
id: "diaryx.math"
version: "0.1.3"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-math"
categories: ["editor", "formatting"]
tags: ["math", "latex", "editor"]
capabilities: ["editor_extension"]
artifact:
  url: "https://github.com/diaryx-org/plugin-math/releases/download/v0.1.3/diaryx_math_extism.wasm"
  sha256: "f3f8e7bc981be77d3ecebfc9e0fa6f8db3f2ae93f1c7e336ea5a0b855e962c9b"
  size: 419818
  published_at: "2026-03-15T16:11:17Z"
ui:
  - slot: EditorExtension
    id: mathInline
    label: "Math"
  - slot: EditorExtension
    id: mathBlock
    label: "Math Block"
---

Render inline and block LaTeX.

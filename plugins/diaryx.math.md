---
title: "Math"
description: "LaTeX math rendering with inline ($...$) and block ($$...$$) support"
id: "diaryx.math"
version: "0.1.1"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-math"
categories: ["editor", "formatting"]
tags: ["math", "latex", "editor"]
capabilities: ["editor_extension"]
artifact:
  url: "https://github.com/diaryx-org/plugin-math/releases/download/v0.1.1/diaryx_math_extism.wasm"
  sha256: "6e07960272b21e6db47b31f4947680af24e6fb369f4c959c623941270cbce013"
  size: 418696
  published_at: "2026-03-10T18:24:29Z"
ui:
  - slot: EditorExtension
    id: mathInline
    label: "Math"
  - slot: EditorExtension
    id: mathBlock
    label: "Math Block"
---

Render inline and block LaTeX.

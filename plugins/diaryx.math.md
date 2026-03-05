---
title: "Math"
description: "LaTeX math rendering with inline ($...$) and block ($$...$$) support"
id: "diaryx.math"
version: "0.1.0"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-math"
categories: ["editor", "formatting"]
tags: ["math", "latex", "editor"]
capabilities: ["editor_extension"]
artifact:
  url: "https://github.com/diaryx-org/plugin-math/releases/download/v0.1.0/diaryx_math_extism.wasm"
  sha256: "e013c399b9e77a5ae91adb67db06d32d48421cc5b3789070c312486e0147affb"
  size: 413866
  published_at: "2026-03-05T00:20:23Z"
ui:
  - slot: EditorExtension
    id: mathInline
    label: "Math"
  - slot: EditorExtension
    id: mathBlock
    label: "Math Block"
---

Render inline and block LaTeX.

---
title: "Math"
description: "LaTeX math rendering with inline ($...$) and block ($$...$$) support"
id: "diaryx.math"
version: "1.2.1"
author: "Diaryx Team"
license: "PolyForm Shield 1.0.0"
repository: "https://github.com/diaryx-org/plugin-math"
categories: ["editor", "formatting"]
tags: ["math", "latex", "editor"]
capabilities: ["editor_extension"]
artifact:
  url: ""
  sha256: ""
  size: 0
  published_at: ""
ui:
  - slot: EditorExtension
    id: mathInline
    label: "Math"
  - slot: EditorExtension
    id: mathBlock
    label: "Math Block"
---

Render inline and block LaTeX.

---
title: MTLMathMode.safe
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlmathmode/safe
source_url: 'https://developer.apple.com/documentation/metal/mtlmathmode/safe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlmathmode/safe.json'
content_hash: 'sha256:f9c79c7c5d20a116'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLMathMode](../mtlmathmode.md)

# MTLMathMode.safe

<sub>Case</sub>

An indicator of the mode the compiler uses to disable unsafe floating-point optimizations by preventing the compiler from making any transformations that could affect the results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case safe
```

## See Also

### Modes

- [MTLMathModeFast](fast.md) — An indicator of the mode the compiler uses to make aggressive, potentially lossy assumptions about floating-point math.
- [MTLMathModeRelaxed](relaxed.md) — An indicator of the mode the compiler uses to make aggressive, potentially lossy assumptions about floating-point math, while honoring Inf/NaN.

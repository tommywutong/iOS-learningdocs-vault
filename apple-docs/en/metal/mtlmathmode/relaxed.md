---
title: MTLMathMode.relaxed
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlmathmode/relaxed
source_url: 'https://developer.apple.com/documentation/metal/mtlmathmode/relaxed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlmathmode/relaxed.json'
content_hash: 'sha256:5094ba85cfc5110a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLMathMode](../mtlmathmode.md)

# MTLMathMode.relaxed

<sub>Case</sub>

An indicator of the mode the compiler uses to make aggressive, potentially lossy assumptions about floating-point math, while honoring Inf/NaN.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case relaxed
```

## Discussion

This is the default for Apple silicon devices.

## See Also

### Modes

- [MTLMathModeFast](fast.md) — An indicator of the mode the compiler uses to make aggressive, potentially lossy assumptions about floating-point math.
- [MTLMathModeSafe](safe.md) — An indicator of the mode the compiler uses to disable unsafe floating-point optimizations by preventing the compiler from making any transformations that could affect the results.

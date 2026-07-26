---
title: MTLMathMode.fast
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlmathmode/fast
source_url: 'https://developer.apple.com/documentation/metal/mtlmathmode/fast'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlmathmode/fast.json'
content_hash: 'sha256:32b4750dbcc33540'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLMathMode](../mtlmathmode.md)

# MTLMathMode.fast

<sub>Case</sub>

An indicator of the mode the compiler uses to make aggressive, potentially lossy assumptions about floating-point math.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case fast
```

## Discussion

This is the default for Intel and AMD devices.

## See Also

### Modes

- [MTLMathModeRelaxed](relaxed.md) — An indicator of the mode the compiler uses to make aggressive, potentially lossy assumptions about floating-point math, while honoring Inf/NaN.
- [MTLMathModeSafe](safe.md) — An indicator of the mode the compiler uses to disable unsafe floating-point optimizations by preventing the compiler from making any transformations that could affect the results.

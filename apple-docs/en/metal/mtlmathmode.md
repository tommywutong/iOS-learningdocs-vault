---
title: MTLMathMode
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlmathmode
source_url: 'https://developer.apple.com/documentation/metal/mtlmathmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlmathmode.json'
content_hash: 'sha256:c9bf7e33479ae3f5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLMathMode

<sub>Enumeration</sub>

An indication of whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLMathMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Modes

- [MTLMathModeFast](mtlmathmode/fast.md) — An indicator of the mode the compiler uses to make aggressive, potentially lossy assumptions about floating-point math.
- [MTLMathModeRelaxed](mtlmathmode/relaxed.md) — An indicator of the mode the compiler uses to make aggressive, potentially lossy assumptions about floating-point math, while honoring Inf/NaN.
- [MTLMathModeSafe](mtlmathmode/safe.md) — An indicator of the mode the compiler uses to disable unsafe floating-point optimizations by preventing the compiler from making any transformations that could affect the results.

### Initializers

- [init(rawValue:)](<mtlmathmode/init(rawvalue_).md>)

## See Also

### Enumerations

- [Code](mtltensorerror-swift.struct/code.md) — The error codes that Metal can raise when you create a tensor.
- [MTLArgumentBuffersTier](mtlargumentbufferstier.md) — The values that determine the limits and capabilities of argument buffers.
- [MTLLogStateError](mtllogstateerror.md)
- [MTLMathFloatingPointFunctions](mtlmathfloatingpointfunctions.md) — Indicates which FP32 math functions Metal uses.
- [MTLMatrixLayout](mtlmatrixlayout.md)
- [MTLReadWriteTextureTier](mtlreadwritetexturetier.md) — The support level for read-write texture formats.
- [MTLShaderValidation](mtlshadervalidation.md) — Indicates whether shader validation in an enabled or disabled state, or neither state.
- [MTLTransformType](mtltransformtype.md)

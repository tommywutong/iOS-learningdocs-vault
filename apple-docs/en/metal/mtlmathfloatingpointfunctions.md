---
title: MTLMathFloatingPointFunctions
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlmathfloatingpointfunctions
source_url: 'https://developer.apple.com/documentation/metal/mtlmathfloatingpointfunctions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlmathfloatingpointfunctions.json'
content_hash: 'sha256:7de880e7f93d2276'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLMathFloatingPointFunctions

<sub>Enumeration</sub>

Indicates which FP32 math functions Metal uses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLMathFloatingPointFunctions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Function sets

- [MTLMathFloatingPointFunctionsFast](mtlmathfloatingpointfunctions/fast.md) — An indication that Metal uses the fast version of the 32b floating-point math functions.
- [MTLMathFloatingPointFunctionsPrecise](mtlmathfloatingpointfunctions/precise.md) — An indication that Metal uses the precise version of the 32b floating-point math functions.

### Initializers

- [init(rawValue:)](<mtlmathfloatingpointfunctions/init(rawvalue_).md>)

## See Also

### Enumerations

- [Code](mtltensorerror-swift.struct/code.md) — The error codes that Metal can raise when you create a tensor.
- [MTLArgumentBuffersTier](mtlargumentbufferstier.md) — The values that determine the limits and capabilities of argument buffers.
- [MTLLogStateError](mtllogstateerror.md)
- [MTLMathMode](mtlmathmode.md) — An indication of whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.
- [MTLMatrixLayout](mtlmatrixlayout.md)
- [MTLReadWriteTextureTier](mtlreadwritetexturetier.md) — The support level for read-write texture formats.
- [MTLShaderValidation](mtlshadervalidation.md) — Indicates whether shader validation in an enabled or disabled state, or neither state.
- [MTLTransformType](mtltransformtype.md)

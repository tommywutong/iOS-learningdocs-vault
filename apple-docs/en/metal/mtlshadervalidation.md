---
title: MTLShaderValidation
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlshadervalidation
source_url: 'https://developer.apple.com/documentation/metal/mtlshadervalidation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlshadervalidation.json'
content_hash: 'sha256:60ddf3787b20e0ac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLShaderValidation

<sub>Enumeration</sub>

Indicates whether shader validation in an enabled or disabled state, or neither state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLShaderValidation
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Validation states

- [MTLShaderValidationDefault](mtlshadervalidation/default.md) — The default value when the property isn’t set.
- [MTLShaderValidationDisabled](mtlshadervalidation/disabled.md) — Disables shader validation.
- [MTLShaderValidationEnabled](mtlshadervalidation/enabled.md) — Enables shader validation.

### Initializers

- [init(rawValue:)](<mtlshadervalidation/init(rawvalue_).md>)

## See Also

### Enumerations

- [Code](mtltensorerror-swift.struct/code.md) — The error codes that Metal can raise when you create a tensor.
- [MTLArgumentBuffersTier](mtlargumentbufferstier.md) — The values that determine the limits and capabilities of argument buffers.
- [MTLLogStateError](mtllogstateerror.md)
- [MTLMathFloatingPointFunctions](mtlmathfloatingpointfunctions.md) — Indicates which FP32 math functions Metal uses.
- [MTLMathMode](mtlmathmode.md) — An indication of whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.
- [MTLMatrixLayout](mtlmatrixlayout.md)
- [MTLReadWriteTextureTier](mtlreadwritetexturetier.md) — The support level for read-write texture formats.
- [MTLTransformType](mtltransformtype.md)

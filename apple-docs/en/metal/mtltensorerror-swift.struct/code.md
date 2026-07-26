---
title: MTLTensorError.Code
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltensorerror-swift.struct/code
source_url: 'https://developer.apple.com/documentation/metal/mtltensorerror-swift.struct/code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensorerror-swift.struct/code.json'
content_hash: 'sha256:a193ba010837ef01'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensorError](../mtltensorerror-swift.struct.md)

# MTLTensorError.Code

<sub>Enumeration</sub>

The error codes that Metal can raise when you create a tensor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum Code
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [MTLTensorErrorInternalError](code/internalerror.md) — An internal Metal error occurred.
- [MTLTensorErrorInvalidDescriptor](code/invaliddescriptor.md) — The tensor descriptor is invalid.
- [MTLTensorErrorNone](code/none.md) — No error occurred.

### Initializers

- [init(rawValue:)](<code/init(rawvalue_).md>)

## See Also

### Enumerations

- [MTLArgumentBuffersTier](../mtlargumentbufferstier.md) — The values that determine the limits and capabilities of argument buffers.
- [MTLLogStateError](../mtllogstateerror.md)
- [MTLMathFloatingPointFunctions](../mtlmathfloatingpointfunctions.md) — Indicates which FP32 math functions Metal uses.
- [MTLMathMode](../mtlmathmode.md) — An indication of whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.
- [MTLMatrixLayout](../mtlmatrixlayout.md)
- [MTLReadWriteTextureTier](../mtlreadwritetexturetier.md) — The support level for read-write texture formats.
- [MTLShaderValidation](../mtlshadervalidation.md) — Indicates whether shader validation in an enabled or disabled state, or neither state.
- [MTLTransformType](../mtltransformtype.md)

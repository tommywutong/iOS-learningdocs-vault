---
title: MTLReadWriteTextureTier
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlreadwritetexturetier
source_url: 'https://developer.apple.com/documentation/metal/mtlreadwritetexturetier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlreadwritetexturetier.json'
content_hash: 'sha256:ff938c2f7a0e5e5a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLReadWriteTextureTier

<sub>Enumeration</sub>

The support level for read-write texture formats.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLReadWriteTextureTier
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration cases

- [MTLReadWriteTextureTier1](mtlreadwritetexturetier/tier1.md) — Indicates the system supports tier 1 read-write textures.
- [MTLReadWriteTextureTier2](mtlreadwritetexturetier/tier2.md) — Indicates the system supports tier 2 read-write textures.
- [MTLReadWriteTextureTierNone](mtlreadwritetexturetier/tiernone.md) — Indicates the system doesn’t support read-write textures.

### Initializers

- [init(rawValue:)](<mtlreadwritetexturetier/init(rawvalue_).md>)

## See Also

### Enumerations

- [Code](mtltensorerror-swift.struct/code.md) — The error codes that Metal can raise when you create a tensor.
- [MTLArgumentBuffersTier](mtlargumentbufferstier.md) — The values that determine the limits and capabilities of argument buffers.
- [MTLLogStateError](mtllogstateerror.md)
- [MTLMathFloatingPointFunctions](mtlmathfloatingpointfunctions.md) — Indicates which FP32 math functions Metal uses.
- [MTLMathMode](mtlmathmode.md) — An indication of whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.
- [MTLMatrixLayout](mtlmatrixlayout.md)
- [MTLShaderValidation](mtlshadervalidation.md) — Indicates whether shader validation in an enabled or disabled state, or neither state.
- [MTLTransformType](mtltransformtype.md)

---
title: MTLArgumentBuffersTier
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlargumentbufferstier
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentbufferstier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentbufferstier.json'
content_hash: 'sha256:0be020d7cbc503e7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLArgumentBuffersTier

<sub>Enumeration</sub>

The values that determine the limits and capabilities of argument buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLArgumentBuffersTier
```

## Overview

See [Improving CPU performance by using argument buffers](improving-cpu-performance-by-using-argument-buffers.md) for more information about argument buffer tiers, limits, and capabilities. Query the [argumentBuffersSupport](mtldevice/argumentbufferssupport.md) property to determine argument buffer tier support for a given device.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration cases

- [MTLArgumentBuffersTier1](mtlargumentbufferstier/tier1.md) — Support for tier 1 argument buffers.
- [MTLArgumentBuffersTier2](mtlargumentbufferstier/tier2.md) — Support for tier 2 argument buffers.

### Initializers

- [init(rawValue:)](<mtlargumentbufferstier/init(rawvalue_).md>)

## See Also

### Enumerations

- [Code](mtltensorerror-swift.struct/code.md) — The error codes that Metal can raise when you create a tensor.
- [MTLLogStateError](mtllogstateerror.md)
- [MTLMathFloatingPointFunctions](mtlmathfloatingpointfunctions.md) — Indicates which FP32 math functions Metal uses.
- [MTLMathMode](mtlmathmode.md) — An indication of whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.
- [MTLMatrixLayout](mtlmatrixlayout.md)
- [MTLReadWriteTextureTier](mtlreadwritetexturetier.md) — The support level for read-write texture formats.
- [MTLShaderValidation](mtlshadervalidation.md) — Indicates whether shader validation in an enabled or disabled state, or neither state.
- [MTLTransformType](mtltransformtype.md)

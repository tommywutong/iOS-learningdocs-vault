---
title: MTLTensorExtents
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltensorextents
source_url: 'https://developer.apple.com/documentation/metal/mtltensorextents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensorextents.json'
content_hash: 'sha256:fe750c35a91d0bfd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTensorExtents

<sub>Class</sub>

An integer array that holds per-dimension values such as tensor sizes, strides, or block factors

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLTensorExtents
```

## Overview

Supports a rank between `0` and [MTL_TENSOR_MAX_RANK](mtl_tensor_max_rank.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializers

- [init(_:)](<mtltensorextents/init(__).md>) — Creates a tensor with extents from an array of dimension values.

### Instance Properties

- [extents](mtltensorextents/extents.md) — Retrieves the extents for this object.
- [rank](mtltensorextents/rank.md) — The number of values in the extents object.

## See Also

### Tensors

- [MTLTensor](mtltensor.md) — A resource representing a multi-dimensional array that you can use with machine learning workloads.
- [MTLTensorDescriptor](mtltensordescriptor.md) — A configuration type for creating new tensor instances.
- [MTLTensorReferenceType](mtltensorreferencetype.md) — An object that represents a tensor in the shading language in a struct or array.
- [MTLTensorUsage](mtltensorusage.md) — The contexts in which you can use a tensor.
- [MTLTensorDomain](mtltensordomain.md) — An error domain for errors that pertain to creating a tensor.
- [MTLTensorBinding](mtltensorbinding.md) — An object that represents a tensor bound to a graphics or compute function or a machine learning function.
- [MTLTensorError](mtltensorerror-swift.struct.md)
- [Code](mtltensorerror-swift.struct/code.md) — The error codes that Metal can raise when you create a tensor.
- [MTLTensorDataType](mtltensordatatype.md) — The possible data types for the elements of a tensor.
- [MTLTensorDomain](mtltensordomain.md) — An error domain for errors that pertain to creating a tensor.
- [MTL_TENSOR_MAX_RANK](mtl_tensor_max_rank.md)

---
title: MTLTensorReferenceType
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltensorreferencetype
source_url: 'https://developer.apple.com/documentation/metal/mtltensorreferencetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensorreferencetype.json'
content_hash: 'sha256:050b78075efa54e8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTensorReferenceType

<sub>Class</sub>

An object that represents a tensor in the shading language in a struct or array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLTensorReferenceType
```

## Relationships

- **Inherits From**: [MTLType](mtltype.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [access](mtltensorreferencetype/access.md) — A value that represents the read/write permissions of the tensor.
- [auxiliaryPlanes](mtltensorreferencetype/auxiliaryplanes.md) — The auxiliary planes that this tensor reference requires. _(beta)_
- [dimensions](mtltensorreferencetype/dimensions.md) — The array of sizes, in elements, one for each dimension of this tensor.
- [indexType](mtltensorreferencetype/indextype.md) — The data format you use for indexing into the tensor.
- [tensorDataType](mtltensorreferencetype/tensordatatype.md) — The underlying data format of the tensor.

## See Also

### Tensors

- [MTLTensor](mtltensor.md) — A resource representing a multi-dimensional array that you can use with machine learning workloads.
- [MTLTensorDescriptor](mtltensordescriptor.md) — A configuration type for creating new tensor instances.
- [MTLTensorExtents](mtltensorextents.md) — An integer array that holds per-dimension values such as tensor sizes, strides, or block factors
- [MTLTensorUsage](mtltensorusage.md) — The contexts in which you can use a tensor.
- [MTLTensorDomain](mtltensordomain.md) — An error domain for errors that pertain to creating a tensor.
- [MTLTensorBinding](mtltensorbinding.md) — An object that represents a tensor bound to a graphics or compute function or a machine learning function.
- [MTLTensorError](mtltensorerror-swift.struct.md)
- [Code](mtltensorerror-swift.struct/code.md) — The error codes that Metal can raise when you create a tensor.
- [MTLTensorDataType](mtltensordatatype.md) — The possible data types for the elements of a tensor.
- [MTLTensorDomain](mtltensordomain.md) — An error domain for errors that pertain to creating a tensor.
- [MTL_TENSOR_MAX_RANK](mtl_tensor_max_rank.md)

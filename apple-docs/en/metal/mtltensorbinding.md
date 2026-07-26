---
title: MTLTensorBinding
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltensorbinding
source_url: 'https://developer.apple.com/documentation/metal/mtltensorbinding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensorbinding.json'
content_hash: 'sha256:87b42d588efbcd48'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTensorBinding

<sub>Protocol</sub>

An object that represents a tensor bound to a graphics or compute function or a machine learning function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLTensorBinding : MTLBinding
```

## Relationships

- **Inherits From**: [MTLBinding](mtlbinding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [auxiliaryPlanes](mtltensorbinding/auxiliaryplanes.md) — An array of the tensor’s auxiliary planes. _(beta)_
- [dimensions](mtltensorbinding/dimensions.md) — The array of sizes, in elements, one for each dimension of this tensor.
- [indexType](mtltensorbinding/indextype.md) — The data format you use for indexing into the tensor.
- [tensorDataType](mtltensorbinding/tensordatatype.md) — The underlying data format of this tensor.

## See Also

### Tensors

- [MTLTensor](mtltensor.md) — A resource representing a multi-dimensional array that you can use with machine learning workloads.
- [MTLTensorDescriptor](mtltensordescriptor.md) — A configuration type for creating new tensor instances.
- [MTLTensorExtents](mtltensorextents.md) — An integer array that holds per-dimension values such as tensor sizes, strides, or block factors
- [MTLTensorReferenceType](mtltensorreferencetype.md) — An object that represents a tensor in the shading language in a struct or array.
- [MTLTensorUsage](mtltensorusage.md) — The contexts in which you can use a tensor.
- [MTLTensorDomain](mtltensordomain.md) — An error domain for errors that pertain to creating a tensor.
- [MTLTensorError](mtltensorerror-swift.struct.md)
- [Code](mtltensorerror-swift.struct/code.md) — The error codes that Metal can raise when you create a tensor.
- [MTLTensorDataType](mtltensordatatype.md) — The possible data types for the elements of a tensor.
- [MTLTensorDomain](mtltensordomain.md) — An error domain for errors that pertain to creating a tensor.
- [MTL_TENSOR_MAX_RANK](mtl_tensor_max_rank.md)

---
title: MTLTensor
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltensor
source_url: 'https://developer.apple.com/documentation/metal/mtltensor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensor.json'
content_hash: 'sha256:976ab77d570f659d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTensor

<sub>Protocol</sub>

A resource representing a multi-dimensional array that you can use with machine learning workloads.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLTensor : MTLResource
```

## Relationships

- **Inherits From**: [MTLAllocation](mtlallocation.md), [MTLResource](mtlresource.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [auxiliaryPlanes](mtltensor/auxiliaryplanes.md) — The auxiliary planes of this tensor. _(beta)_
- [buffer](mtltensor/buffer.md) — A buffer instance this tensor shares its storage with or `nil` if this tensor does not wrap an underlying buffer.
- [bufferOffset](mtltensor/bufferoffset.md) — An offset, in bytes, into the buffer instance this tensor shares its storage with, or zero if this tensor does not wrap an underlying buffer.
- [dataType](mtltensor/datatype.md) — The underlying data format of the data plane.
- [dimensions](mtltensor/dimensions.md) — An array of sizes, in elements, one for each dimension of this tensor.
- [gpuResourceID](mtltensor/gpuresourceid.md) — A handle that represents the GPU resource, which you can store in an argument buffer.
- [strides](mtltensor/strides.md) — An array of strides, in elements, one for each dimension of this tensor, if applicable.
- [usage](mtltensor/usage.md) — A set of contexts in which you can use this tensor.

### Instance Methods

- [- getBytes:strides:fromSliceOrigin:sliceDimensions:](<mtltensor/getbytes(__strides_sliceorigin_slicedimensions_).md>) — Copies data from a slice of the data plane of this tensor into a pointer you provide.
- [- getBytes:strides:fromSliceOrigin:sliceDimensions:plane:](<mtltensor/getbytes(__strides_sliceorigin_slicedimensions_plane_).md>) — Copies data from a slice of a plane of this tensor into a pointer you provide. _(beta)_
- [- replaceSliceOrigin:sliceDimensions:plane:withBytes:strides:](<mtltensor/replace(sliceorigin_slicedimensions_plane_withbytes_strides_).md>) — Replaces a slice of a plane of this tensor with data from a pointer you provide. _(beta)_
- [- replaceSliceOrigin:sliceDimensions:withBytes:strides:](<mtltensor/replace(sliceorigin_slicedimensions_withbytes_strides_).md>) — Replaces a slice of the data plane of this tensor with data from a pointer you provide.

## See Also

### Tensors

- [MTLTensorDescriptor](mtltensordescriptor.md) — A configuration type for creating new tensor instances.
- [MTLTensorExtents](mtltensorextents.md) — An integer array that holds per-dimension values such as tensor sizes, strides, or block factors
- [MTLTensorReferenceType](mtltensorreferencetype.md) — An object that represents a tensor in the shading language in a struct or array.
- [MTLTensorUsage](mtltensorusage.md) — The contexts in which you can use a tensor.
- [MTLTensorDomain](mtltensordomain.md) — An error domain for errors that pertain to creating a tensor.
- [MTLTensorBinding](mtltensorbinding.md) — An object that represents a tensor bound to a graphics or compute function or a machine learning function.
- [MTLTensorError](mtltensorerror-swift.struct.md)
- [Code](mtltensorerror-swift.struct/code.md) — The error codes that Metal can raise when you create a tensor.
- [MTLTensorDataType](mtltensordatatype.md) — The possible data types for the elements of a tensor.
- [MTLTensorDomain](mtltensordomain.md) — An error domain for errors that pertain to creating a tensor.
- [MTL_TENSOR_MAX_RANK](mtl_tensor_max_rank.md)

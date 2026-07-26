---
title: MTLTensorDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltensordescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtltensordescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensordescriptor.json'
content_hash: 'sha256:1264979cd13663ff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTensorDescriptor

<sub>Class</sub>

A configuration type for creating new tensor instances.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLTensorDescriptor
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [auxiliaryPlanes](mtltensordescriptor/auxiliaryplanes.md) — The auxiliary plane configurations for this tensor. _(beta)_
- [cpuCacheMode](mtltensordescriptor/cpucachemode.md) — A value that configures the cache mode of CPU mapping of tensors you create with this descriptor.
- [dataType](mtltensordescriptor/datatype.md) — The data format of all elements in the data plane.
- [dimensions](mtltensordescriptor/dimensions.md) — An array of sizes, in elements, one for each dimension of the tensors you create with this descriptor.
- [hazardTrackingMode](mtltensordescriptor/hazardtrackingmode.md) — A value that configures the hazard tracking of tensors you create with this descriptor.
- [resourceOptions](mtltensordescriptor/resourceoptions.md) — A packed set of the [storageMode](mtltensordescriptor/storagemode.md), [cpuCacheMode](mtltensordescriptor/cpucachemode.md), and [hazardTrackingMode](mtltensordescriptor/hazardtrackingmode.md) properties.
- [storageMode](mtltensordescriptor/storagemode.md) — A value that configures the memory location and access permissions of tensors you create with this descriptor.
- [strides](mtltensordescriptor/strides.md) — An array of strides, in elements, one for each dimension of this tensor, if applicable.
- [usage](mtltensordescriptor/usage.md) — A set of contexts in which you can use tensors you create with this descriptor.

## See Also

### Tensors

- [MTLTensor](mtltensor.md) — A resource representing a multi-dimensional array that you can use with machine learning workloads.
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

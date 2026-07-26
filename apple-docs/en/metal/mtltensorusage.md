---
title: MTLTensorUsage
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltensorusage
source_url: 'https://developer.apple.com/documentation/metal/mtltensorusage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensorusage.json'
content_hash: 'sha256:0bebc5d8da549c7d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTensorUsage

<sub>Structure</sub>

The contexts in which you can use a tensor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLTensorUsage
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<mtltensorusage/init(rawvalue_).md>)

### Type Properties

- [MTLTensorUsageCompute](mtltensorusage/compute.md) — A tensor context that applies to compute encoders.
- [MTLTensorUsageMachineLearning](mtltensorusage/machinelearning.md) — A tensor context that applies to machine learning encoders.
- [MTLTensorUsageRender](mtltensorusage/render.md) — A tensor context that applies to render encoders.

## See Also

### Tensors

- [MTLTensor](mtltensor.md) — A resource representing a multi-dimensional array that you can use with machine learning workloads.
- [MTLTensorDescriptor](mtltensordescriptor.md) — A configuration type for creating new tensor instances.
- [MTLTensorExtents](mtltensorextents.md) — An integer array that holds per-dimension values such as tensor sizes, strides, or block factors
- [MTLTensorReferenceType](mtltensorreferencetype.md) — An object that represents a tensor in the shading language in a struct or array.
- [MTLTensorDomain](mtltensordomain.md) — An error domain for errors that pertain to creating a tensor.
- [MTLTensorBinding](mtltensorbinding.md) — An object that represents a tensor bound to a graphics or compute function or a machine learning function.
- [MTLTensorError](mtltensorerror-swift.struct.md)
- [Code](mtltensorerror-swift.struct/code.md) — The error codes that Metal can raise when you create a tensor.
- [MTLTensorDataType](mtltensordatatype.md) — The possible data types for the elements of a tensor.
- [MTLTensorDomain](mtltensordomain.md) — An error domain for errors that pertain to creating a tensor.
- [MTL_TENSOR_MAX_RANK](mtl_tensor_max_rank.md)

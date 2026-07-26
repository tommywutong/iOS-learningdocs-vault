---
title: auxiliaryPlanes
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/metal/mtltensordescriptor/auxiliaryplanes
source_url: 'https://developer.apple.com/documentation/metal/mtltensordescriptor/auxiliaryplanes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensordescriptor/auxiliaryplanes.json'
content_hash: 'sha256:f162e55a0f3cbea2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensorDescriptor](../mtltensordescriptor.md)

# auxiliaryPlanes

<sub>Instance Property</sub>

The auxiliary plane configurations for this tensor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var auxiliaryPlanes: MTLTensorAuxiliaryPlaneDescriptorMap? { get set }
```

## Discussion

Set this property with a populated [MTLTensorAuxiliaryPlaneDescriptorMap](../mtltensorauxiliaryplanedescriptormap.md) to create a multi-plane tensor. When `nil`, the tensor has only a data plane.

Multi-plane tensors do not support [MTLTensorUsageMachineLearning](../mtltensorusage/machinelearning.md). Use [MTLTensorUsageCompute](../mtltensorusage/compute.md) or [MTLTensorUsageRender](../mtltensorusage/render.md).

Multi-plane tensors do not support data types larger than one byte as the data plane type.

Multi-plane tensors do not support rank zero.

The default value is `nil`.

---
title: 'setDescriptor(_:for:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/metal/mtltensorauxiliaryplanedescriptormap/setdescriptor(_:for:)'
source_url: 'https://developer.apple.com/documentation/metal/mtltensorauxiliaryplanedescriptormap/setdescriptor(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensorauxiliaryplanedescriptormap/setdescriptor%28_%3Afor%3A%29.json'
content_hash: 'sha256:00c973e5381722f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensorAuxiliaryPlaneDescriptorMap](../mtltensorauxiliaryplanedescriptormap.md)

# setDescriptor(_:for:)

<sub>Instance Method</sub>

Sets the auxiliary plane descriptor for the given plane type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setDescriptor(_ descriptor: MTLTensorAuxiliaryPlaneDescriptor, for plane: MTLTensorPlaneType)
```

## Parameters

- `descriptor` — The descriptor configuring the auxiliary plane.

- `plane` — The plane type to associate the descriptor with.

## Discussion

[MTLTensorPlaneTypeData](../mtltensorplanetype/data.md) is not a valid plane type for this method. The data plane is always present, and you configure it directly on [MTLTensorDescriptor](../mtltensordescriptor.md).

[MTLTensorPlaneTypeScales](../mtltensorplanetype/scales.md) auxiliary planes only support [MTLTensorDataTypeMetalFloat8UE8M0](../mtltensordatatype/metalfloat8ue8m0.md) as a data type.

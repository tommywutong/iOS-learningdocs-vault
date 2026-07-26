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
doc_path: /documentation/metal/mtltensor/auxiliaryplanes
source_url: 'https://developer.apple.com/documentation/metal/mtltensor/auxiliaryplanes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensor/auxiliaryplanes.json'
content_hash: 'sha256:4fd9b0f122d8f9dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensor](../mtltensor.md)

# auxiliaryPlanes

<sub>Instance Property</sub>

The auxiliary planes of this tensor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var auxiliaryPlanes: [any MTLTensorAuxiliaryPlane] { get }
```

## Discussion

Returns an array of [MTLTensorAuxiliaryPlane](../mtltensorauxiliaryplane.md) objects describing each auxiliary plane configured on this tensor. For single-plane tensors, this array is empty.

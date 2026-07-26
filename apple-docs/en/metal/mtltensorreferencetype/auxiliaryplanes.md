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
doc_path: /documentation/metal/mtltensorreferencetype/auxiliaryplanes
source_url: 'https://developer.apple.com/documentation/metal/mtltensorreferencetype/auxiliaryplanes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensorreferencetype/auxiliaryplanes.json'
content_hash: 'sha256:1c23a7d5d65e8c5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensorReferenceType](../mtltensorreferencetype.md)

# auxiliaryPlanes

<sub>Instance Property</sub>

The auxiliary planes that this tensor reference requires.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var auxiliaryPlanes: [MTLTensorAuxiliaryPlaneType] { get }
```

## Discussion

Returns an array of [MTLTensorAuxiliaryPlaneType](../mtltensorauxiliaryplanetype.md) objects describing each auxiliary plane the shader expects. Empty if the tensor has no auxiliary planes.

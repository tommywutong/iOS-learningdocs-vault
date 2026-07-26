---
title: blockFactors
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/metal/mtltensorauxiliaryplanedescriptor/blockfactors
source_url: 'https://developer.apple.com/documentation/metal/mtltensorauxiliaryplanedescriptor/blockfactors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensorauxiliaryplanedescriptor/blockfactors.json'
content_hash: 'sha256:545a9fa4260d5971'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensorAuxiliaryPlaneDescriptor](../mtltensorauxiliaryplanedescriptor.md)

# blockFactors

<sub>Instance Property</sub>

An extents instance that represents the number of data plane elements which correspond to one element in a plane you create with this descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var blockFactors: MTLTensorExtents { get set }
```

## Discussion

The number of dimensions in the extents needs to match the number of the tensor’s dimensions.

The first element of the block factors needs to be `32`. All remaining elements need to be `1`.

The default value is a 1D block size of width `32`.

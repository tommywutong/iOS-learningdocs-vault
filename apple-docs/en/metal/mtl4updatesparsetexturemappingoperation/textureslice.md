---
title: textureSlice
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4updatesparsetexturemappingoperation/textureslice
source_url: 'https://developer.apple.com/documentation/metal/mtl4updatesparsetexturemappingoperation/textureslice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4updatesparsetexturemappingoperation/textureslice.json'
content_hash: 'sha256:ed67b42372006b56'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4UpdateSparseTextureMappingOperation](../mtl4updatesparsetexturemappingoperation.md)

# textureSlice

<sub>Instance Property</sub>

The index of the array slice in the texture to update.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var textureSlice: Int
```

## Discussion

Provide `0` in this member if the texture type is not an array.

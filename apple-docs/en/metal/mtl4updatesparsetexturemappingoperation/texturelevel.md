---
title: textureLevel
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4updatesparsetexturemappingoperation/texturelevel
source_url: 'https://developer.apple.com/documentation/metal/mtl4updatesparsetexturemappingoperation/texturelevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4updatesparsetexturemappingoperation/texturelevel.json'
content_hash: 'sha256:b0548cc6ea1e8143'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4UpdateSparseTextureMappingOperation](../mtl4updatesparsetexturemappingoperation.md)

# textureLevel

<sub>Instance Property</sub>

The index of the mipmap level in the texture to update.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var textureLevel: Int
```

## Discussion

Provide a value between `0` and the texture’s [firstMipmapInTail](../mtltexture/firstmipmapintail.md).

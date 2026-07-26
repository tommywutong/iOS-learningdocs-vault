---
title: textureRegion
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4updatesparsetexturemappingoperation/textureregion
source_url: 'https://developer.apple.com/documentation/metal/mtl4updatesparsetexturemappingoperation/textureregion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4updatesparsetexturemappingoperation/textureregion.json'
content_hash: 'sha256:9c409bb7907e1f2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4UpdateSparseTextureMappingOperation](../mtl4updatesparsetexturemappingoperation.md)

# textureRegion

<sub>Instance Property</sub>

The region in the texture to update, in tiles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var textureRegion: MTLRegion
```

## Discussion

When [textureLevel](texturelevel.md) is equal to the texture’s [firstMipmapInTail](../mtltexture/firstmipmapintail.md), set `origin.y` to `0` and `size.height` to `1`.

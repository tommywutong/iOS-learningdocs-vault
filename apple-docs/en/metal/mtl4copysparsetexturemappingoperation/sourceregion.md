---
title: sourceRegion
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4copysparsetexturemappingoperation/sourceregion
source_url: 'https://developer.apple.com/documentation/metal/mtl4copysparsetexturemappingoperation/sourceregion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4copysparsetexturemappingoperation/sourceregion.json'
content_hash: 'sha256:8705d8bdef8d7c04'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CopySparseTextureMappingOperation](../mtl4copysparsetexturemappingoperation.md)

# sourceRegion

<sub>Instance Property</sub>

The region in the source texture, in tiles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sourceRegion: MTLRegion
```

## Discussion

The tiles remain mapped in the source texture.

When [sourceLevel](sourcelevel.md) is equal to the source texture’s [firstMipmapInTail](../mtltexture/firstmipmapintail.md), set `origin.y` to `0` and `size.height` to `1`.

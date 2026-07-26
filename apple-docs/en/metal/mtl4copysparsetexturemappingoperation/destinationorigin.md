---
title: destinationOrigin
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4copysparsetexturemappingoperation/destinationorigin
source_url: 'https://developer.apple.com/documentation/metal/mtl4copysparsetexturemappingoperation/destinationorigin'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4copysparsetexturemappingoperation/destinationorigin.json'
content_hash: 'sha256:2f1dddbef306dac2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CopySparseTextureMappingOperation](../mtl4copysparsetexturemappingoperation.md)

# destinationOrigin

<sub>Instance Property</sub>

The origin in the destination texture to copy into, in tiles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var destinationOrigin: MTLOrigin
```

## Discussion

The X, Y and Z coordinates of the tiles relative to the origin match the same coordinates in the source region.

When [destinationLevel](destinationlevel.md) is equal to the destination texture’s [firstMipmapInTail](../mtltexture/firstmipmapintail.md), set `destinationOrigin.y` to `0`.

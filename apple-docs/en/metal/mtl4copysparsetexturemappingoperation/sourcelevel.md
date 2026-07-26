---
title: sourceLevel
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4copysparsetexturemappingoperation/sourcelevel
source_url: 'https://developer.apple.com/documentation/metal/mtl4copysparsetexturemappingoperation/sourcelevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4copysparsetexturemappingoperation/sourcelevel.json'
content_hash: 'sha256:9f4a7b5fb6d81ddb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CopySparseTextureMappingOperation](../mtl4copysparsetexturemappingoperation.md)

# sourceLevel

<sub>Instance Property</sub>

The index of the mipmap level in the source texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sourceLevel: Int
```

## Discussion

Provide a value between `0` and the source texture’s [firstMipmapInTail](../mtltexture/firstmipmapintail.md).

When [sourceLevel](sourcelevel.md) is equal to the source texture’s [firstMipmapInTail](../mtltexture/firstmipmapintail.md), set [destinationLevel](destinationlevel.md) to the destination texture’s [firstMipmapInTail](../mtltexture/firstmipmapintail.md).

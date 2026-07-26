---
title: destinationLevel
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4copysparsetexturemappingoperation/destinationlevel
source_url: 'https://developer.apple.com/documentation/metal/mtl4copysparsetexturemappingoperation/destinationlevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4copysparsetexturemappingoperation/destinationlevel.json'
content_hash: 'sha256:deb915347a4bdf23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CopySparseTextureMappingOperation](../mtl4copysparsetexturemappingoperation.md)

# destinationLevel

<sub>Instance Property</sub>

The index of the mipmap level in the destination texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var destinationLevel: Int
```

## Discussion

Provide a value between `0` and the destination texture’s [firstMipmapInTail](../mtltexture/firstmipmapintail.md).

When [sourceLevel](sourcelevel.md) is equal to the source texture’s [firstMipmapInTail](../mtltexture/firstmipmapintail.md), set [destinationLevel](destinationlevel.md) to the destination texture’s [firstMipmapInTail](../mtltexture/firstmipmapintail.md).

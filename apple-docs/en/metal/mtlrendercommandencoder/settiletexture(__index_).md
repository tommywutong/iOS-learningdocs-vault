---
title: 'setTileTexture(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/settiletexture(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settiletexture(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/settiletexture%28_%3Aindex%3A%29.json'
content_hash: 'sha256:086a62da210b8518'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setTileTexture(_:index:)

<sub>Instance Method</sub>

Assigns a texture to an entry in the tile shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setTileTexture(_ texture: (any MTLTexture)?, index: Int)
```

## Parameters

- `texture` — An [MTLTexture](../mtltexture.md) instance the command assigns to an entry in the tile shader argument table for textures.

- `index` — An integer that represents the entry in the tile shader argument table for textures that stores a record of `texture`.

## Discussion

By default, the texture at each index is `nil`.

## See Also

### Assigning textures

- [setTileTextures(_:range:)](<settiletextures(__range_).md>) — Assigns multiple textures to a range of entries in the tile shader argument table.

---
title: 'setObjectTexture(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setobjecttexture(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setobjecttexture(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setobjecttexture%28_%3Aindex%3A%29.json'
content_hash: 'sha256:a2606712b8662a05'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setObjectTexture(_:index:)

<sub>Instance Method</sub>

Assigns a texture to an entry in the object shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setObjectTexture(_ texture: (any MTLTexture)?, index: Int)
```

## Parameters

- `texture` — An [MTLTexture](../mtltexture.md) instance the command assigns to an entry in the object shader argument table for textures.

- `index` — An integer that represents the entry in the object shader argument table for textures that stores a record of `texture`.

## Discussion

By default, the texture at each index is `nil`.

## See Also

### Assigning textures for object shaders

- [setObjectTextures(_:range:)](<setobjecttextures(__range_).md>) — Assigns multiple textures to a range of entries in the object shader argument table.

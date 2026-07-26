---
title: 'setVertexTexture(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setvertextexture(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertextexture(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setvertextexture%28_%3Aindex%3A%29.json'
content_hash: 'sha256:6459a58e4bb5d8c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setVertexTexture(_:index:)

<sub>Instance Method</sub>

Assigns a texture to an entry in the vertex shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setVertexTexture(_ texture: (any MTLTexture)?, index: Int)
```

## Parameters

- `texture` — An [MTLTexture](../mtltexture.md) instance the command assigns to an entry in the vertex shader argument table for textures.

- `index` — An integer that represents the entry in the vertex shader argument table for textures that stores a record of `texture`.

## Discussion

By default, the texture at each index is `nil`.

## See Also

### Assigning textures

- [setVertexTextures(_:range:)](<setvertextextures(__range_).md>) — Assigns multiple textures to a range of entries in the vertex shader argument table.

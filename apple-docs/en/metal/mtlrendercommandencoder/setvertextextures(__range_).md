---
title: 'setVertexTextures(_:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.11+, tvOS 8.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setvertextextures(_:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertextextures(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setvertextextures%28_%3Arange%3A%29.json'
content_hash: 'sha256:0d80cc322f628329'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setVertexTextures(_:range:)

<sub>Instance Method</sub>

Assigns multiple textures to a range of entries in the vertex shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setVertexTextures(_ textures: [(any MTLTexture)?], range: Range<Int>)
```

## Parameters

- `textures` — An array of [MTLTexture](../mtltexture.md) instances the command assigns to entries in the vertex shader argument table for textures.

- `range` — A span of integers that represent the entries in the vertex shader argument table for textures. Each entry stores a record of the corresponding element in `textures`.

## Discussion

By default, the texture at each index is `nil`.

> [!note] Note
> The Objective-C version of this method is [setVertexTextures:withRange:](setvertextextures_withrange_.md).

## See Also

### Assigning textures

- [- setVertexTexture:atIndex:](<setvertextexture(__index_).md>) — Assigns a texture to an entry in the vertex shader argument table.

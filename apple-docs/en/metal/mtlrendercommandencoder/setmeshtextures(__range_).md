---
title: 'setMeshTextures(_:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setmeshtextures(_:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setmeshtextures(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setmeshtextures%28_%3Arange%3A%29.json'
content_hash: 'sha256:d33d4e678a3223cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setMeshTextures(_:range:)

<sub>Instance Method</sub>

Assigns multiple textures to a range of entries in the mesh shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setMeshTextures(_ textures: [(any MTLTexture)?], range: Range<Int>)
```

## Parameters

- `textures` — An array of [MTLTexture](../mtltexture.md) instances the command assigns to entries in the mesh shader argument table for textures.

- `range` — A span of integers that represent the entries in the mesh shader argument table for textures. Each entry stores a record of the corresponding element in `textures`.

## Discussion

By default, the texture at each index is `nil`.

> [!note] Note
> The Objective-C version of this method is [setMeshTextures:withRange:](setmeshtextures_withrange_.md).

## See Also

### Assigning textures for mesh shaders

- [- setMeshTexture:atIndex:](<setmeshtexture(__index_).md>) — Assigns a texture to an entry in the mesh shader argument table.

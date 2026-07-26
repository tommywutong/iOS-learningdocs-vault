---
title: 'setTextures(_:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, macOS 10.13+, tvOS 11.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/settextures(_:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/settextures(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/settextures%28_%3Arange%3A%29.json'
content_hash: 'sha256:5261ae2ade695dda'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setTextures(_:range:)

<sub>Instance Method</sub>

Encodes references to an array of textures into the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setTextures(_ textures: [(any MTLTexture)?], range: Range<Int>)
```

## Parameters

- `textures` — An array of textures the method encodes.

- `range` — A range of indices within the argument buffer for each element in `textures`. The values correspond to either the index IDs of declarations in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instances.

## See Also

### Encoding textures

- [- setTexture:atIndex:](<settexture(__index_).md>) — Encodes a reference to a texture into the argument buffer.

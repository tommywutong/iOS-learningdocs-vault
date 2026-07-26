---
title: 'setTexture(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/settexture(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/settexture(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/settexture%28_%3Aindex%3A%29.json'
content_hash: 'sha256:1c7aaaae662cd2de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setTexture(_:index:)

<sub>Instance Method</sub>

Encodes a reference to a texture into the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setTexture(_ texture: (any MTLTexture)?, index: Int)
```

## Parameters

- `texture` — A texture the method encodes.

- `index` — The index of a texture within the argument buffer. The value corresponds to either the index ID of a declaration in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of an [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instance.

## See Also

### Encoding textures

- [setTextures(_:range:)](<settextures(__range_).md>) — Encodes references to an array of textures into the argument buffer.

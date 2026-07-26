---
title: 'setTextures:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/settextures:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/settextures:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/settextures%3Awithrange%3A.json'
content_hash: 'sha256:94b6513eadd7e061'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setTextures:withRange:

<sub>Instance Method</sub>

Encodes references to an array of textures into the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setTextures:(id<MTLTexture> const[]) textures withRange:(NSRange) range;
```

## Parameters

- `textures` — An array of textures the method encodes.

- `range` — A range of indices within the argument buffer for each element in `textures`. The values correspond to either the index IDs of declarations in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instances.

## See Also

### Encoding textures

- [- setTexture:atIndex:](<settexture(__index_).md>) — Encodes a reference to a texture into the argument buffer.

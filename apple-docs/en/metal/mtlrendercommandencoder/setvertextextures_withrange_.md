---
title: 'setVertexTextures:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setvertextextures:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertextextures:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setvertextextures%3Awithrange%3A.json'
content_hash: 'sha256:5e82b549fc026a5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setVertexTextures:withRange:

<sub>Instance Method</sub>

Assigns multiple textures to a range of entries in the vertex shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setVertexTextures:(id<MTLTexture> const[]) textures withRange:(NSRange) range;
```

## Parameters

- `textures` — A pointer to a C array of [MTLTexture](../mtltexture.md) instances the command assigns to entries in the vertex shader argument table for textures.

- `range` — A span of integers that represent the entries in the vertex shader argument table for textures. Each entry stores a record of the corresponding element in `textures`.

## Discussion

By default, the texture at each index is `nil`.

> [!note] Note
> The Swift version of this method is [setVertexTextures(_:range:)](<setvertextextures(__range_).md>).

## See Also

### Assigning textures

- [- setVertexTexture:atIndex:](<setvertextexture(__index_).md>) — Assigns a texture to an entry in the vertex shader argument table.

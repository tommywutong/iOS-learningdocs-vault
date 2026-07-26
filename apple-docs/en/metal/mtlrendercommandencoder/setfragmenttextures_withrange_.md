---
title: 'setFragmentTextures:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setfragmenttextures:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfragmenttextures:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setfragmenttextures%3Awithrange%3A.json'
content_hash: 'sha256:56cc0d5766e8f3f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setFragmentTextures:withRange:

<sub>Instance Method</sub>

Assigns multiple textures to a range of entries in the fragment shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setFragmentTextures:(id<MTLTexture> const[]) textures withRange:(NSRange) range;
```

## Parameters

- `textures` — A pointer to a C array of [MTLTexture](../mtltexture.md) instances the command assigns to entries in the fragment shader argument table for textures.

- `range` — A span of integers that represent the entries in the fragment shader argument table for textures. Each entry stores a record of the corresponding element in `textures`.

## Discussion

By default, the texture at each index is `nil`.

> [!note] Note
> The Swift version of this method is [setFragmentTextures(_:range:)](<setfragmenttextures(__range_).md>).

## See Also

### Assigning textures

- [- setFragmentTexture:atIndex:](<setfragmenttexture(__index_).md>) — Assigns a texture to an entry in the fragment shader argument table.

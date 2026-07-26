---
title: 'setMeshTextures:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setmeshtextures:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setmeshtextures:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setmeshtextures%3Awithrange%3A.json'
content_hash: 'sha256:379aab2c7e3d3536'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setMeshTextures:withRange:

<sub>Instance Method</sub>

Assigns multiple textures to a range of entries in the mesh shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setMeshTextures:(id<MTLTexture> const[]) textures withRange:(NSRange) range;
```

## Parameters

- `textures` — A pointer to a C array of [MTLTexture](../mtltexture.md) instances the command assigns to entries in the mesh shader argument table for textures.

- `range` — A span of integers that represent the entries in the mesh shader argument table for textures. Each entry stores a record of the corresponding element in `textures`.

## Discussion

By default, the texture at each index is `nil`.

> [!note] Note
> The Swift version of this method is [setMeshTextures(_:range:)](<setmeshtextures(__range_).md>).

## See Also

### Assigning textures for mesh shaders

- [- setMeshTexture:atIndex:](<setmeshtexture(__index_).md>) — Assigns a texture to an entry in the mesh shader argument table.

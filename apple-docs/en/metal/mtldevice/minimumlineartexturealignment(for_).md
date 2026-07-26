---
title: 'minimumLinearTextureAlignment(for:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/minimumlineartexturealignment(for:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/minimumlineartexturealignment(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/minimumlineartexturealignment%28for%3A%29.json'
content_hash: 'sha256:eb256af8512d27a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# minimumLinearTextureAlignment(for:)

<sub>Instance Method</sub>

Returns the minimum alignment the GPU device requires to create a linear texture from a buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func minimumLinearTextureAlignment(for format: MTLPixelFormat) -> Int
```

## Parameters

- `format` — An [MTLPixelFormat](../mtlpixelformat.md) instance that can’t be any of the depth, stencil, or compressed pixel formats.

## Discussion

Metal aligns linear textures to their minimum alignment value, which directly affects the [- newTextureWithDescriptor:offset:bytesPerRow:](<../mtlbuffer/maketexture(descriptor_offset_bytesperrow_).md>) method’s `offset` and `bytesPerRow` parameters.

## See Also

### Creating textures

- [- newTextureWithDescriptor:](<maketexture(descriptor_).md>) — Creates a new texture instance.
- [- newTextureWithDescriptor:iosurface:plane:](<maketexture(descriptor_iosurface_plane_).md>) — Creates a texture instance that uses I/O surface to store its underlying data.
- [- newSharedTextureWithDescriptor:](<makesharedtexture(descriptor_).md>) — Creates a texture that you can share across process boundaries.
- [- newSharedTextureWithHandle:](<makesharedtexture(handle_).md>) — Creates a texture that references a shared texture.
- [- minimumTextureBufferAlignmentForPixelFormat:](<minimumtexturebufferalignment(for_).md>) — Returns the minimum alignment the GPU device requires to create a texture buffer from a buffer.

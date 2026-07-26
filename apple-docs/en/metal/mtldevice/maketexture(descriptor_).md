---
title: 'makeTexture(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/maketexture(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/maketexture(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/maketexture%28descriptor%3A%29.json'
content_hash: 'sha256:c9807315fae13c57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeTexture(descriptor:)

<sub>Instance Method</sub>

Creates a new texture instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?
```

## Parameters

- `descriptor` — An [MTLTextureDescriptor](../mtltexturedescriptor.md) instance.

## Return Value

A new [MTLTexture](../mtltexture.md) instance if the method completed successfully; otherwise `nil`.

## See Also

### Creating textures

- [- newTextureWithDescriptor:iosurface:plane:](<maketexture(descriptor_iosurface_plane_).md>) — Creates a texture instance that uses I/O surface to store its underlying data.
- [- newSharedTextureWithDescriptor:](<makesharedtexture(descriptor_).md>) — Creates a texture that you can share across process boundaries.
- [- newSharedTextureWithHandle:](<makesharedtexture(handle_).md>) — Creates a texture that references a shared texture.
- [- minimumLinearTextureAlignmentForPixelFormat:](<minimumlineartexturealignment(for_).md>) — Returns the minimum alignment the GPU device requires to create a linear texture from a buffer.
- [- minimumTextureBufferAlignmentForPixelFormat:](<minimumtexturebufferalignment(for_).md>) — Returns the minimum alignment the GPU device requires to create a texture buffer from a buffer.

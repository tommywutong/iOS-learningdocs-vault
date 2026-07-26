---
title: 'makeSharedTexture(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makesharedtexture(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makesharedtexture(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makesharedtexture%28descriptor%3A%29.json'
content_hash: 'sha256:b28a0b4374bb9920'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeSharedTexture(descriptor:)

<sub>Instance Method</sub>

Creates a texture that you can share across process boundaries.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeSharedTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?
```

## Parameters

- `descriptor` — An [MTLTextureDescriptor](../mtltexturedescriptor.md) instance.

## Return Value

A new [MTLTexture](../mtltexture.md) instance if the method completed successfully; otherwise `nil`.

## Discussion

You can create a shared texture but only with [MTLResourceStorageModePrivate](../mtlresourceoptions/storagemodeprivate.md). You can share the texture with another process by:

1. Creating a texture handle (see [- newSharedTextureHandle](<../mtltexture/makesharedtexturehandle().md>))
2. Passing the texture handle to the other process
3. Creating a texture in the other process by calling the [- newSharedTextureWithHandle:](<makesharedtexture(handle_).md>)method

> [!important] Important
> You can share a texture with another process that uses the same GPU, but not with a different GPU.

## See Also

### Creating textures

- [- newTextureWithDescriptor:](<maketexture(descriptor_).md>) — Creates a new texture instance.
- [- newTextureWithDescriptor:iosurface:plane:](<maketexture(descriptor_iosurface_plane_).md>) — Creates a texture instance that uses I/O surface to store its underlying data.
- [- newSharedTextureWithHandle:](<makesharedtexture(handle_).md>) — Creates a texture that references a shared texture.
- [- minimumLinearTextureAlignmentForPixelFormat:](<minimumlineartexturealignment(for_).md>) — Returns the minimum alignment the GPU device requires to create a linear texture from a buffer.
- [- minimumTextureBufferAlignmentForPixelFormat:](<minimumtexturebufferalignment(for_).md>) — Returns the minimum alignment the GPU device requires to create a texture buffer from a buffer.

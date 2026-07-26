---
title: 'makeSharedTexture(handle:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makesharedtexture(handle:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makesharedtexture(handle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makesharedtexture%28handle%3A%29.json'
content_hash: 'sha256:5af49e1deb61136a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeSharedTexture(handle:)

<sub>Instance Method</sub>

Creates a texture that references a shared texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeSharedTexture(handle sharedHandle: MTLSharedTextureHandle) -> (any MTLTexture)?
```

## Parameters

- `sharedHandle` — An [MTLSharedTextureHandle](../mtlsharedtexturehandle.md) instance, typically from another process using the same GPU device.

## Return Value

A new [MTLTexture](../mtltexture.md) instance if the method completed successfully; otherwise `nil`.

## Discussion

Call this method from the same [MTLDevice](../mtldevice.md) instance that created the shared texture instance.

> [!tip] Tip
> You can identify the correct device with the texture handle’s [device](../mtlsharedtexturehandle/device.md) property.

## See Also

### Creating textures

- [- newTextureWithDescriptor:](<maketexture(descriptor_).md>) — Creates a new texture instance.
- [- newTextureWithDescriptor:iosurface:plane:](<maketexture(descriptor_iosurface_plane_).md>) — Creates a texture instance that uses I/O surface to store its underlying data.
- [- newSharedTextureWithDescriptor:](<makesharedtexture(descriptor_).md>) — Creates a texture that you can share across process boundaries.
- [- minimumLinearTextureAlignmentForPixelFormat:](<minimumlineartexturealignment(for_).md>) — Returns the minimum alignment the GPU device requires to create a linear texture from a buffer.
- [- minimumTextureBufferAlignmentForPixelFormat:](<minimumtexturebufferalignment(for_).md>) — Returns the minimum alignment the GPU device requires to create a texture buffer from a buffer.

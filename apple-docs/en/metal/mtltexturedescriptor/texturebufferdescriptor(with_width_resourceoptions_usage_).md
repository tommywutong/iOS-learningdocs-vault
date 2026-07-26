---
title: 'textureBufferDescriptor(with:width:resourceOptions:usage:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtltexturedescriptor/texturebufferdescriptor(with:width:resourceoptions:usage:)'
source_url: 'https://developer.apple.com/documentation/metal/mtltexturedescriptor/texturebufferdescriptor(with:width:resourceoptions:usage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexturedescriptor/texturebufferdescriptor%28with%3Awidth%3Aresourceoptions%3Ausage%3A%29.json'
content_hash: 'sha256:6504d3b4c1bfe64a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTextureDescriptor](../mtltexturedescriptor.md)

# textureBufferDescriptor(with:width:resourceOptions:usage:)

<sub>Type Method</sub>

Creates a texture descriptor object for a texture buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func textureBufferDescriptor(with pixelFormat: MTLPixelFormat, width: Int, resourceOptions: MTLResourceOptions = [], usage: MTLTextureUsage) -> MTLTextureDescriptor
```

## Parameters

- `pixelFormat` — The format describing how every pixel on the texture buffer is stored. The default value is [MTLPixelFormatRGBA8Unorm](../mtlpixelformat/rgba8unorm.md).

- `width` — The width of the texture buffer. The value needs to be greater than or equal to `1`.

- `resourceOptions` — The access options to use for the new texture buffer.

- `usage` — The allowed usage of the new texture buffer.

## Return Value

A pointer to a texture descriptor object for a texture buffer.

## See Also

### Creating texture descriptors

- [+ texture2DDescriptorWithPixelFormat:width:height:mipmapped:](<texture2ddescriptor(pixelformat_width_height_mipmapped_).md>) — Creates a texture descriptor object for a 2D texture.
- [+ textureCubeDescriptorWithPixelFormat:size:mipmapped:](<texturecubedescriptor(pixelformat_size_mipmapped_).md>) — Creates a texture descriptor object for a cube texture.

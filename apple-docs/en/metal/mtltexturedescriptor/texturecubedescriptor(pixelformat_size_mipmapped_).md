---
title: 'textureCubeDescriptor(pixelFormat:size:mipmapped:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtltexturedescriptor/texturecubedescriptor(pixelformat:size:mipmapped:)'
source_url: 'https://developer.apple.com/documentation/metal/mtltexturedescriptor/texturecubedescriptor(pixelformat:size:mipmapped:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexturedescriptor/texturecubedescriptor%28pixelformat%3Asize%3Amipmapped%3A%29.json'
content_hash: 'sha256:f1a2e2c136c424e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTextureDescriptor](../mtltexturedescriptor.md)

# textureCubeDescriptor(pixelFormat:size:mipmapped:)

<sub>Type Method</sub>

Creates a texture descriptor object for a cube texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func textureCubeDescriptor(pixelFormat: MTLPixelFormat, size: Int, mipmapped: Bool) -> MTLTextureDescriptor
```

## Parameters

- `pixelFormat` — The format describing how every pixel on the texture image is stored. The default value is [MTLPixelFormatRGBA8Unorm](../mtlpixelformat/rgba8unorm.md).

- `size` — The width and height of each slice of the cube texture. The value needs to be greater than or equal to `1`.

- `mipmapped` — A Boolean indicating whether the resulting image should be mipmapped. If [true](../../swift/true.md), then the [mipmapLevelCount](mipmaplevelcount.md) property in the returned descriptor is computed from `width` and `height`. If [false](../../swift/false.md), then [mipmapLevelCount](mipmaplevelcount.md) is `1`.

## Return Value

A pointer to a texture descriptor object for a cube texture.

## Discussion

For a cube texture, the property values describe one slice, which is any one of its six sides. Each slice is a square.

## See Also

### Creating texture descriptors

- [+ texture2DDescriptorWithPixelFormat:width:height:mipmapped:](<texture2ddescriptor(pixelformat_width_height_mipmapped_).md>) — Creates a texture descriptor object for a 2D texture.
- [+ textureBufferDescriptorWithPixelFormat:width:resourceOptions:usage:](<texturebufferdescriptor(with_width_resourceoptions_usage_).md>) — Creates a texture descriptor object for a texture buffer.

---
title: 'texture2DDescriptor(pixelFormat:width:height:mipmapped:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtltexturedescriptor/texture2ddescriptor(pixelformat:width:height:mipmapped:)'
source_url: 'https://developer.apple.com/documentation/metal/mtltexturedescriptor/texture2ddescriptor(pixelformat:width:height:mipmapped:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexturedescriptor/texture2ddescriptor%28pixelformat%3Awidth%3Aheight%3Amipmapped%3A%29.json'
content_hash: 'sha256:343a75e05c05b999'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTextureDescriptor](../mtltexturedescriptor.md)

# texture2DDescriptor(pixelFormat:width:height:mipmapped:)

<sub>Type Method</sub>

Creates a texture descriptor object for a 2D texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func texture2DDescriptor(pixelFormat: MTLPixelFormat, width: Int, height: Int, mipmapped: Bool) -> MTLTextureDescriptor
```

## Parameters

- `pixelFormat` — The format describing how every pixel on the texture image is stored. The default value is [MTLPixelFormatRGBA8Unorm](../mtlpixelformat/rgba8unorm.md).

- `width` — The width of the 2D texture image. The value needs to be greater than or equal to `1`.

- `height` — The height of the 2D texture image. The value needs to be greater than or equal to `1`.

- `mipmapped` — A Boolean indicating whether the resulting image should be mipmapped. If [true](../../swift/true.md), then the [mipmapLevelCount](mipmaplevelcount.md) property in the returned descriptor is computed from `width` and `height`. If [false](../../swift/false.md), then [mipmapLevelCount](mipmaplevelcount.md) is `1`.

## Return Value

A pointer to a texture descriptor object for a 2D texture.

## See Also

### Related Documentation

- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)

### Creating texture descriptors

- [+ textureCubeDescriptorWithPixelFormat:size:mipmapped:](<texturecubedescriptor(pixelformat_size_mipmapped_).md>) — Creates a texture descriptor object for a cube texture.
- [+ textureBufferDescriptorWithPixelFormat:width:resourceOptions:usage:](<texturebufferdescriptor(with_width_resourceoptions_usage_).md>) — Creates a texture descriptor object for a texture buffer.

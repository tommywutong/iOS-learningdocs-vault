---
title: 'makeTextureView(pixelFormat:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtltexture/maketextureview(pixelformat:)'
source_url: 'https://developer.apple.com/documentation/metal/mtltexture/maketextureview(pixelformat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexture/maketextureview%28pixelformat%3A%29.json'
content_hash: 'sha256:8ba377d602f21fdb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTexture](../mtltexture.md)

# makeTextureView(pixelFormat:)

<sub>Instance Method</sub>

Creates a new view of the texture, reinterpreting its data using a different pixel format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeTextureView(pixelFormat: MTLPixelFormat) -> (any MTLTexture)?
```

## Parameters

- `pixelFormat` — A new pixel format, which needs to be compatible with the original pixel format.

## Return Value

A new texture object that shares the same storage allocation of the texture.

## Discussion

When you create a texture normally, Metal allocates memory for the textureʼs pixel data. These storage allocations can be quite large. You can reduce memory use and avoid copying texture data by using a _texture view_—a texture object that shares another textureʼs storage allocation, reinterpreting the pixel data in some other format.

Not all pixel formats are compatible with one another. Reinterpretation of image data between pixel formats is supported within the following groups:

- All 8-, 16-, 32-, 64-, and 128-bit color formats are compatible with other formats with the same bit length.
- sRGB and non-sRGB forms of the same compressed format (for example, [MTLPixelFormatBC1_RGBA](../mtlpixelformat/bc1_rgba.md) and [MTLPixelFormatBC1_RGBA_sRGB](../mtlpixelformat/bc1_rgba_srgb.md))
- Combined depth-stencil texture formats and the related format used to access the stencil from a shader (for example, [MTLPixelFormatDepth24Unorm_Stencil8](../mtlpixelformat/depth24unorm_stencil8.md) and [MTLPixelFormatX24_Stencil8](../mtlpixelformat/x24_stencil8.md))

This method doesn’t change the original texture image data in any way, but it may drastically change how the data is interpreted. For example, given a texture with the [MTLPixelFormatRG16Uint](../mtlpixelformat/rg16uint.md) pixel format that contains image data for Red `0xFFFE` and Green `0x0001`, this method would reinterpret that data in an [MTLPixelFormatR32Uint](../mtlpixelformat/r32uint.md) format as Red `0x0001FFFE`.

Some format reinterpretations are supported but may not be useful. For example, this method considers the 32-bit packed color formats [MTLPixelFormatBGR10A2Unorm](../mtlpixelformat/bgr10a2unorm.md) and [MTLDataTypeRG11B10Float](../mtldatatype/rg11b10float.md) to be compatible, but it’s unlikely that the same data can be interpreted by both formats in a meaningful way.

Some format reinterpretations require you to create the source texture with a special usage flag. Set that flag only when necessary, as it can affect performance. For more details, see [MTLTextureUsagePixelFormatView](../mtltextureusage/pixelformatview.md).

## See Also

### Related Documentation

- [parentRelativeLevel](parentrelativelevel.md) — The base level of the parent texture used to create this texture.
- [parentTexture](parent.md) — The parent texture used to create this texture, if any.
- [parentRelativeSlice](parentrelativeslice.md) — The base slice of the parent texture used to create this texture.

### Creating textures by reinterpreting existing texture data

- [makeTextureView(pixelFormat:textureType:levels:slices:)](<maketextureview(pixelformat_texturetype_levels_slices_).md>) — Creates a new view of the texture, reinterpreting a subset of its data using a different type and pixel format.
- [makeTextureView(pixelFormat:textureType:levels:slices:swizzle:)](<maketextureview(pixelformat_texturetype_levels_slices_swizzle_).md>) — Creates a new view of the texture, reinterpreting a subset of its data using a different type, pixel format, and swizzle pattern.

---
title: MTLPixelFormat.depth24Unorm_stencil8
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.11+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlpixelformat/depth24unorm_stencil8
source_url: 'https://developer.apple.com/documentation/metal/mtlpixelformat/depth24unorm_stencil8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpixelformat/depth24unorm_stencil8.json'
content_hash: 'sha256:3039d1bcca6af0c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPixelFormat](../mtlpixelformat.md)

# MTLPixelFormat.depth24Unorm_stencil8

<sub>Case</sub>

A 32-bit combined depth and stencil pixel format with a 24-bit normalized unsigned integer for depth and an 8-bit unsigned integer for stencil.

> [!warning] Deprecated
> Use MTLPixelFormatDepth32Float_Stencil8 instead

<sub>Mac Catalyst, macOS</sub>

```swift
case depth24Unorm_stencil8
```

## Discussion

To blit either the depth or stencil information to a Metal buffer, call the [- copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:](<../mtlblitcommandencoder/copy(from_sourceslice_sourcelevel_sourceorigin_sourcesize_to_destinationoffset_destinationbytesperrow_destinationbytesperimage_options_).md>) method, specifying the blit options for which part you want to copy. You need to provide space for 4 bytes per pixel in your destination buffer. When Metal copies the data, it sets the bottom 3 bytes of each pixel to the depth data and sets the top byte to arbitrary data. Ignore any data stored in the top byte of each pixel.

## See Also

### Depth and stencil pixel formats

- [MTLPixelFormatDepth16Unorm](depth16unorm.md) — A pixel format for a depth-render target that has a 16-bit normalized, unsigned-integer component.
- [MTLPixelFormatDepth32Float](depth32float.md) — A pixel format with one 32-bit floating-point component, used for a depth render target.
- [MTLPixelFormatStencil8](stencil8.md) — A pixel format with an 8-bit unsigned integer component, used for a stencil render target.
- [MTLPixelFormatDepth32Float_Stencil8](depth32float_stencil8.md) — A 40-bit combined depth and stencil pixel format with a 32-bit floating-point value for depth and an 8-bit unsigned integer for stencil.
- [MTLPixelFormatX32_Stencil8](x32_stencil8.md) — A stencil pixel format used to read the stencil value from a texture with a combined 32-bit depth and 8-bit stencil value.
- [MTLPixelFormatX24_Stencil8](x24_stencil8.md) — A stencil pixel format used to read the stencil value from a texture with a combined 24-bit depth and 8-bit stencil value. _(deprecated)_

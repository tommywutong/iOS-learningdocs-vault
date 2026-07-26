---
title: MTLPixelFormat.depth32Float_stencil8
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpixelformat/depth32float_stencil8
source_url: 'https://developer.apple.com/documentation/metal/mtlpixelformat/depth32float_stencil8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpixelformat/depth32float_stencil8.json'
content_hash: 'sha256:395eb99cc6195aca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPixelFormat](../mtlpixelformat.md)

# MTLPixelFormat.depth32Float_stencil8

<sub>Case</sub>

A 40-bit combined depth and stencil pixel format with a 32-bit floating-point value for depth and an 8-bit unsigned integer for stencil.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case depth32Float_stencil8
```

## Discussion

When using this format, some Metal device objects allocate 64-bits per pixel.

## See Also

### Depth and stencil pixel formats

- [MTLPixelFormatDepth16Unorm](depth16unorm.md) — A pixel format for a depth-render target that has a 16-bit normalized, unsigned-integer component.
- [MTLPixelFormatDepth32Float](depth32float.md) — A pixel format with one 32-bit floating-point component, used for a depth render target.
- [MTLPixelFormatStencil8](stencil8.md) — A pixel format with an 8-bit unsigned integer component, used for a stencil render target.
- [MTLPixelFormatDepth24Unorm_Stencil8](depth24unorm_stencil8.md) — A 32-bit combined depth and stencil pixel format with a 24-bit normalized unsigned integer for depth and an 8-bit unsigned integer for stencil. _(deprecated)_
- [MTLPixelFormatX32_Stencil8](x32_stencil8.md) — A stencil pixel format used to read the stencil value from a texture with a combined 32-bit depth and 8-bit stencil value.
- [MTLPixelFormatX24_Stencil8](x24_stencil8.md) — A stencil pixel format used to read the stencil value from a texture with a combined 24-bit depth and 8-bit stencil value. _(deprecated)_

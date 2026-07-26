---
title: MTLPixelFormat.x32_stencil8
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpixelformat/x32_stencil8
source_url: 'https://developer.apple.com/documentation/metal/mtlpixelformat/x32_stencil8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpixelformat/x32_stencil8.json'
content_hash: 'sha256:fda7739eec7413ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPixelFormat](../mtlpixelformat.md)

# MTLPixelFormat.x32_stencil8

<sub>Case</sub>

A stencil pixel format used to read the stencil value from a texture with a combined 32-bit depth and 8-bit stencil value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case x32_stencil8
```

## Discussion

You can’t directly read the stencil value of a texture with the [MTLPixelFormatDepth32Float_Stencil8](depth32float_stencil8.md) format. To read stencil values from a texture with the [MTLPixelFormatDepth32Float_Stencil8](depth32float_stencil8.md) format, create a texture view of that texture using the [MTLPixelFormatX32_Stencil8](x32_stencil8.md) format, and sample the texture view instead.

## See Also

### Depth and stencil pixel formats

- [MTLPixelFormatDepth16Unorm](depth16unorm.md) — A pixel format for a depth-render target that has a 16-bit normalized, unsigned-integer component.
- [MTLPixelFormatDepth32Float](depth32float.md) — A pixel format with one 32-bit floating-point component, used for a depth render target.
- [MTLPixelFormatStencil8](stencil8.md) — A pixel format with an 8-bit unsigned integer component, used for a stencil render target.
- [MTLPixelFormatDepth24Unorm_Stencil8](depth24unorm_stencil8.md) — A 32-bit combined depth and stencil pixel format with a 24-bit normalized unsigned integer for depth and an 8-bit unsigned integer for stencil. _(deprecated)_
- [MTLPixelFormatDepth32Float_Stencil8](depth32float_stencil8.md) — A 40-bit combined depth and stencil pixel format with a 32-bit floating-point value for depth and an 8-bit unsigned integer for stencil.
- [MTLPixelFormatX24_Stencil8](x24_stencil8.md) — A stencil pixel format used to read the stencil value from a texture with a combined 24-bit depth and 8-bit stencil value. _(deprecated)_

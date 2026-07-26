---
title: MTLPixelFormat.depth16Unorm
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpixelformat/depth16unorm
source_url: 'https://developer.apple.com/documentation/metal/mtlpixelformat/depth16unorm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpixelformat/depth16unorm.json'
content_hash: 'sha256:e480dbc325a2a198'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPixelFormat](../mtlpixelformat.md)

# MTLPixelFormat.depth16Unorm

<sub>Case</sub>

A pixel format for a depth-render target that has a 16-bit normalized, unsigned-integer component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case depth16Unorm
```

## Discussion

If you need to apply depth bias, choose a different depth format. Setting a depth bias with this format, such as with [- setDepthBias:slopeScale:clamp:](<../mtlrendercommandencoder/setdepthbias(__slopescale_clamp_).md>), generates incorrect results for apps that run on a device with an Apple A8 or earlier GPU.

## See Also

### Depth and stencil pixel formats

- [MTLPixelFormatDepth32Float](depth32float.md) — A pixel format with one 32-bit floating-point component, used for a depth render target.
- [MTLPixelFormatStencil8](stencil8.md) — A pixel format with an 8-bit unsigned integer component, used for a stencil render target.
- [MTLPixelFormatDepth24Unorm_Stencil8](depth24unorm_stencil8.md) — A 32-bit combined depth and stencil pixel format with a 24-bit normalized unsigned integer for depth and an 8-bit unsigned integer for stencil. _(deprecated)_
- [MTLPixelFormatDepth32Float_Stencil8](depth32float_stencil8.md) — A 40-bit combined depth and stencil pixel format with a 32-bit floating-point value for depth and an 8-bit unsigned integer for stencil.
- [MTLPixelFormatX32_Stencil8](x32_stencil8.md) — A stencil pixel format used to read the stencil value from a texture with a combined 32-bit depth and 8-bit stencil value.
- [MTLPixelFormatX24_Stencil8](x24_stencil8.md) — A stencil pixel format used to read the stencil value from a texture with a combined 24-bit depth and 8-bit stencil value. _(deprecated)_

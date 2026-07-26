---
title: MTLPixelFormat.unspecialized
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpixelformat/unspecialized
source_url: 'https://developer.apple.com/documentation/metal/mtlpixelformat/unspecialized'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpixelformat/unspecialized.json'
content_hash: 'sha256:286d01d53402d48e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPixelFormat](../mtlpixelformat.md)

# MTLPixelFormat.unspecialized

<sub>Case</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case unspecialized
```

## Discussion

A pixel format where the red and green channels are subsampled horizontally.  Two pixels are stored in 32 bits, with shared red and blue values, and unique green values.

This format is equivalent to UYVY, 2vuy, or GL_RGB_422_APPLE/GL_UNSIGNED_SHORT_8_8_APPLE. The component order, from lowest addressed byte to highest, is Cb, Y0, Cr, Y1.  There is no implicit colorspace conversion from YUV to RGB, the shader will receive (Cr, Y, Cb, 1).  422 textures must have a width that is a multiple of 2, and can only be used for 2D non-mipmap textures.  When sampling, ClampToEdge is the only usable wrap mode.

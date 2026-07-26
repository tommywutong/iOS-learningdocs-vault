---
title: pixelFormat
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametallayer/pixelformat
source_url: 'https://developer.apple.com/documentation/quartzcore/cametallayer/pixelformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametallayer/pixelformat.json'
content_hash: 'sha256:3f743a615db2cd0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMetalLayer](../cametallayer.md)

# pixelFormat

<sub>Instance Property</sub>

The pixel format of the layer’s textures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var pixelFormat: MTLPixelFormat { get set }
```

## Discussion

The default value is [MTLPixelFormat.bgra8Unorm](../../metal/mtlpixelformat/bgra8unorm.md).

You must use one of the following formats:

- [MTLPixelFormat.bgra8Unorm](../../metal/mtlpixelformat/bgra8unorm.md)
- [MTLPixelFormat.bgra8Unorm_srgb](../../metal/mtlpixelformat/bgra8unorm_srgb.md)
- [MTLPixelFormat.rgba16Float](../../metal/mtlpixelformat/rgba16float.md)
- [MTLPixelFormat.rgb10a2Unorm](../../metal/mtlpixelformat/rgb10a2unorm.md)
- [MTLPixelFormat.bgr10a2Unorm](../../metal/mtlpixelformat/bgr10a2unorm.md)
- [MTLPixelFormat.bgra10_xr](../../metal/mtlpixelformat/bgra10_xr.md)
- [MTLPixelFormat.bgra10_xr_srgb](../../metal/mtlpixelformat/bgra10_xr_srgb.md)
- [MTLPixelFormat.bgr10_xr](../../metal/mtlpixelformat/bgr10_xr.md)
- [MTLPixelFormat.bgr10_xr_srgb](../../metal/mtlpixelformat/bgr10_xr_srgb.md)

## See Also

### Configuring the Layer’s Drawable Objects

- [colorspace](colorspace.md) — The color space of the rendered content.
- [framebufferOnly](framebufferonly.md) — A Boolean value that determines whether the layer’s textures are used only for rendering.
- [drawableSize](drawablesize.md) — The size, in pixels, of textures for rendering layer content.

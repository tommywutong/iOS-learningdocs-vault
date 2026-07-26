---
title: alphaInfo
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontext/alphainfo
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/alphainfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/alphainfo.json'
content_hash: 'sha256:49837bbe9a10b0c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# alphaInfo

<sub>Instance Property</sub>

Returns the alpha information associated with the context, which indicates how a bitmap context handles the alpha component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var alphaInfo: CGImageAlphaInfo { get }
```

## Discussion

Every bitmap context contains an attribute that specifies whether the bitmap contains an alpha component, and how it is generated. The alpha component determines the opacity of a pixel when it is drawn.

## See Also

### Managing a Bitmap Graphics Context

- [CGBitmapContextGetBitmapInfo](bitmapinfo.md) — Obtains the bitmap information associated with a bitmap graphics context.
- [CGBitmapContextGetBitsPerComponent](bitspercomponent.md) — Returns the bits per component of a bitmap context.
- [CGBitmapContextGetBitsPerPixel](bitsperpixel.md) — Returns the bits per pixel of a bitmap context.
- [CGBitmapContextGetBytesPerRow](bytesperrow.md) — Returns the bytes per row of a bitmap context.
- [CGBitmapContextGetColorSpace](colorspace.md) — Returns the color space of a bitmap context.
- [CGBitmapContextGetData](data.md) — Returns a pointer to the image data associated with a bitmap context.
- [CGBitmapContextGetHeight](height.md) — Returns the height in pixels of a bitmap context.
- [CGBitmapContextGetWidth](width.md) — Returns the width in pixels of a bitmap context.
- [CGBitmapContextCreateImage](<makeimage().md>) — Creates and returns a CGImage from the pixel data in a bitmap graphics context.

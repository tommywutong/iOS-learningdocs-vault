---
title: bitmapInfo
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontext/bitmapinfo
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/bitmapinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/bitmapinfo.json'
content_hash: 'sha256:f59cd79a2a384d7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# bitmapInfo

<sub>Instance Property</sub>

Obtains the bitmap information associated with a bitmap graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var bitmapInfo: CGBitmapInfo { get }
```

## Discussion

The data returned by the function specifies whether the bitmap contains an alpha channel and how the alpha channel is generated, along with whether the components are floating-point or integer.

## See Also

### Managing a Bitmap Graphics Context

- [CGBitmapContextGetAlphaInfo](alphainfo.md) — Returns the alpha information associated with the context, which indicates how a bitmap context handles the alpha component.
- [CGBitmapContextGetBitsPerComponent](bitspercomponent.md) — Returns the bits per component of a bitmap context.
- [CGBitmapContextGetBitsPerPixel](bitsperpixel.md) — Returns the bits per pixel of a bitmap context.
- [CGBitmapContextGetBytesPerRow](bytesperrow.md) — Returns the bytes per row of a bitmap context.
- [CGBitmapContextGetColorSpace](colorspace.md) — Returns the color space of a bitmap context.
- [CGBitmapContextGetData](data.md) — Returns a pointer to the image data associated with a bitmap context.
- [CGBitmapContextGetHeight](height.md) — Returns the height in pixels of a bitmap context.
- [CGBitmapContextGetWidth](width.md) — Returns the width in pixels of a bitmap context.
- [CGBitmapContextCreateImage](<makeimage().md>) — Creates and returns a CGImage from the pixel data in a bitmap graphics context.

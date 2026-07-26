---
title: data
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontext/data
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/data'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/data.json'
content_hash: 'sha256:575150712e346144'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# data

<sub>Instance Property</sub>

Returns a pointer to the image data associated with a bitmap context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var data: UnsafeMutableRawPointer? { get }
```

## Discussion

If you provided the memory for the bitmap data, you can use this method to get that data pointer. If you passed `NULL` for the data pointer when creating your bitmap context, it is safe to get the data pointer in iOS 4.0 and later and macOS 10.6 and later only. In earlier versions of the operating system, passing `NULL` for the data parameter is not supported and may lead to crashes when attempting to access this data using this function.

## See Also

### Managing a Bitmap Graphics Context

- [CGBitmapContextGetBitmapInfo](bitmapinfo.md) — Obtains the bitmap information associated with a bitmap graphics context.
- [CGBitmapContextGetAlphaInfo](alphainfo.md) — Returns the alpha information associated with the context, which indicates how a bitmap context handles the alpha component.
- [CGBitmapContextGetBitsPerComponent](bitspercomponent.md) — Returns the bits per component of a bitmap context.
- [CGBitmapContextGetBitsPerPixel](bitsperpixel.md) — Returns the bits per pixel of a bitmap context.
- [CGBitmapContextGetBytesPerRow](bytesperrow.md) — Returns the bytes per row of a bitmap context.
- [CGBitmapContextGetColorSpace](colorspace.md) — Returns the color space of a bitmap context.
- [CGBitmapContextGetHeight](height.md) — Returns the height in pixels of a bitmap context.
- [CGBitmapContextGetWidth](width.md) — Returns the width in pixels of a bitmap context.
- [CGBitmapContextCreateImage](<makeimage().md>) — Creates and returns a CGImage from the pixel data in a bitmap graphics context.

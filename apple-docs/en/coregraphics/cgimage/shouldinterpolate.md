---
title: shouldInterpolate
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgimage/shouldinterpolate
source_url: 'https://developer.apple.com/documentation/coregraphics/cgimage/shouldinterpolate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgimage/shouldinterpolate.json'
content_hash: 'sha256:22cbf619f3b48b40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGImage](../cgimage.md)

# shouldInterpolate

<sub>Instance Property</sub>

Returns the interpolation setting for a bitmap image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var shouldInterpolate: Bool { get }
```

## Discussion

The interpolation setting specifies whether an edge-smoothing algorithm is applied to the associated image.

## See Also

### Examining an image

- [CGImageIsMask](ismask.md) — Returns whether a bitmap image is an image mask.
- [CGImageGetWidth](width.md) — Returns the width of a bitmap image, in pixels.
- [CGImageGetHeight](height.md) — Returns the height of a bitmap image.
- [CGImageGetBitsPerComponent](bitspercomponent.md) — Returns the number of bits allocated for a single color component of a bitmap image.
- [CGImageGetBitsPerPixel](bitsperpixel.md) — Returns the number of bits allocated for a single pixel in a bitmap image.
- [CGImageGetBytesPerRow](bytesperrow.md) — Returns the number of bytes allocated for a single row of a bitmap image.
- [CGImageGetColorSpace](colorspace.md) — Return the color space for a bitmap image.
- [CGImageGetAlphaInfo](alphainfo.md) — Returns the alpha channel information for a bitmap image.
- [CGImageAlphaInfo](../cgimagealphainfo.md) — Storage options for alpha component data.
- [CGImageGetDataProvider](dataprovider.md) — Returns the data provider for a bitmap image or image mask.
- [CGImageGetDecode](decode.md) — Returns the decode array for a bitmap image.
- [CGImageGetRenderingIntent](renderingintent.md) — Returns the rendering intent setting for a bitmap image.
- [CGImageGetBitmapInfo](bitmapinfo.md) — Returns the bitmap information for a bitmap image.
- [CGBitmapInfo](../cgbitmapinfo.md) — Component information for a bitmap image.
- [CGImageGetUTType](uttype.md) — The Universal Type Identifier for the image.

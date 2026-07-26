---
title: renderingIntent
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgimage/renderingintent
source_url: 'https://developer.apple.com/documentation/coregraphics/cgimage/renderingintent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgimage/renderingintent.json'
content_hash: 'sha256:58c240fc6b634420'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGImage](../cgimage.md)

# renderingIntent

<sub>Instance Property</sub>

Returns the rendering intent setting for a bitmap image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var renderingIntent: CGColorRenderingIntent { get }
```

## Discussion

Provides the `CGColorRenderingIntent` constant that specifies how to handle colors that are not located within the gamut of the destination color space of a graphics context in which the image is drawn. If the image is an image mask, this function returns [kCGRenderingIntentDefault](../cgcolorrenderingintent/defaultintent.md).

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
- [CGImageGetShouldInterpolate](shouldinterpolate.md) — Returns the interpolation setting for a bitmap image.
- [CGImageGetBitmapInfo](bitmapinfo.md) — Returns the bitmap information for a bitmap image.
- [CGBitmapInfo](../cgbitmapinfo.md) — Component information for a bitmap image.
- [CGImageGetUTType](uttype.md) — The Universal Type Identifier for the image.

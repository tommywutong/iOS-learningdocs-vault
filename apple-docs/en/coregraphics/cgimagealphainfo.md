---
title: CGImageAlphaInfo
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgimagealphainfo
source_url: 'https://developer.apple.com/documentation/coregraphics/cgimagealphainfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgimagealphainfo.json'
content_hash: 'sha256:0b8957710cd7bc99'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGImageAlphaInfo

<sub>Enumeration</sub>

Storage options for alpha component data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CGImageAlphaInfo
```

## Overview

A [CGImageAlphaInfo](cgimagealphainfo.md) constant specifies (1) whether a bitmap contains an alpha channel, (2) where the alpha bits are located in the image data, and (3) whether the alpha value is premultiplied. You can obtain a [CGImageAlphaInfo](cgimagealphainfo.md) constant for an image by calling the [CGImageGetAlphaInfo](cgimage/alphainfo.md) function. (You provide a [CGBitmapInfo](cgbitmapinfo.md) constant to the function [CGImageCreate](<cgimage/init(width_height_bitspercomponent_bitsperpixel_bytesperrow_space_bitmapinfo_provider_decode_shouldinterpolate_intent_).md>), part of which is a [CGImageAlphaInfo](cgimagealphainfo.md) constant.)

Alpha blending is accomplished by combining the color components of the source image with the color components of the destination image using the linear interpolation formula, where “source” is one color component of one pixel of the new paint and “destination” is one color component of the background image.

Core Graphics supports premultiplied alpha only for images. You should not premultiply any other color values specified in Core Graphics.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [CaseIterable](../swift/caseiterable.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCGImageAlphaFirst](cgimagealphainfo/first.md) — The alpha component is stored in the most significant bits of each pixel. For example, non-premultiplied ARGB.
- [kCGImageAlphaLast](cgimagealphainfo/last.md) — The alpha component is stored in the least significant bits of each pixel. For example, non-premultiplied RGBA.
- [kCGImageAlphaNone](cgimagealphainfo/none.md) — There is no alpha channel.
- [kCGImageAlphaNoneSkipFirst](cgimagealphainfo/noneskipfirst.md) — There is no alpha channel. If the total size of the pixel is greater than the space required for the number of color components in the color space, the most significant bits are ignored.
- [kCGImageAlphaOnly](cgimagealphainfo/alphaonly.md) — There is no color data, only an alpha channel.
- [kCGImageAlphaNoneSkipLast](cgimagealphainfo/noneskiplast.md) — There is no alpha channel.
- [kCGImageAlphaPremultipliedFirst](cgimagealphainfo/premultipliedfirst.md) — The alpha component is stored in the most significant bits of each pixel and the color components have already been multiplied by this alpha value. For example, premultiplied ARGB.
- [kCGImageAlphaPremultipliedLast](cgimagealphainfo/premultipliedlast.md) — The alpha component is stored in the least significant bits of each pixel and the color components have already been multiplied by this alpha value. For example, premultiplied RGBA.

### Initializers

- [init(rawValue:)](<cgimagealphainfo/init(rawvalue_).md>)

## See Also

### Examining an image

- [CGImageIsMask](cgimage/ismask.md) — Returns whether a bitmap image is an image mask.
- [CGImageGetWidth](cgimage/width.md) — Returns the width of a bitmap image, in pixels.
- [CGImageGetHeight](cgimage/height.md) — Returns the height of a bitmap image.
- [CGImageGetBitsPerComponent](cgimage/bitspercomponent.md) — Returns the number of bits allocated for a single color component of a bitmap image.
- [CGImageGetBitsPerPixel](cgimage/bitsperpixel.md) — Returns the number of bits allocated for a single pixel in a bitmap image.
- [CGImageGetBytesPerRow](cgimage/bytesperrow.md) — Returns the number of bytes allocated for a single row of a bitmap image.
- [CGImageGetColorSpace](cgimage/colorspace.md) — Return the color space for a bitmap image.
- [CGImageGetAlphaInfo](cgimage/alphainfo.md) — Returns the alpha channel information for a bitmap image.
- [CGImageGetDataProvider](cgimage/dataprovider.md) — Returns the data provider for a bitmap image or image mask.
- [CGImageGetDecode](cgimage/decode.md) — Returns the decode array for a bitmap image.
- [CGImageGetShouldInterpolate](cgimage/shouldinterpolate.md) — Returns the interpolation setting for a bitmap image.
- [CGImageGetRenderingIntent](cgimage/renderingintent.md) — Returns the rendering intent setting for a bitmap image.
- [CGImageGetBitmapInfo](cgimage/bitmapinfo.md) — Returns the bitmap information for a bitmap image.
- [CGBitmapInfo](cgbitmapinfo.md) — Component information for a bitmap image.
- [CGImageGetUTType](cgimage/uttype.md) — The Universal Type Identifier for the image.

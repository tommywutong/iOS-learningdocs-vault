---
title: CGImage
framework: Core Graphics
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgimage
source_url: 'https://developer.apple.com/documentation/coregraphics/cgimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgimage.json'
content_hash: 'sha256:eab6c88692d3eae6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGImage

<sub>Class</sub>

A bitmap image or image mask.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CGImage
```

## Overview

A bitmap image is a rectangular array of pixels, each of which represents a single sample or data point from a source image.

## Relationships

- **Conforms To**: [AttachableAsImage](../testing/attachableasimage.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating images

- [CGImageCreate](<cgimage/init(width_height_bitspercomponent_bitsperpixel_bytesperrow_space_bitmapinfo_provider_decode_shouldinterpolate_intent_).md>) — Creates a bitmap image from data supplied by a data provider.
- [CGImageCreateWithJPEGDataProvider](<cgimage/init(jpegdataprovidersource_decode_shouldinterpolate_intent_).md>) — Creates a bitmap image using JPEG-encoded data supplied by a data provider.
- [CGImageCreateWithPNGDataProvider](<cgimage/init(pngdataprovidersource_decode_shouldinterpolate_intent_).md>) — Creates a bitmap image using PNG-encoded data supplied by a data provider.
- [CGImageCreateWithContentHeadroom](<cgimage/init(headroom_width_height_bitspercomponent_bitsperpixel_bytesperrow_space_bitmapinfo_provider_decode_shouldinterpolate_intent_).md>)

### Examining an image

- [CGImageIsMask](cgimage/ismask.md) — Returns whether a bitmap image is an image mask.
- [CGImageGetWidth](cgimage/width.md) — Returns the width of a bitmap image, in pixels.
- [CGImageGetHeight](cgimage/height.md) — Returns the height of a bitmap image.
- [CGImageGetBitsPerComponent](cgimage/bitspercomponent.md) — Returns the number of bits allocated for a single color component of a bitmap image.
- [CGImageGetBitsPerPixel](cgimage/bitsperpixel.md) — Returns the number of bits allocated for a single pixel in a bitmap image.
- [CGImageGetBytesPerRow](cgimage/bytesperrow.md) — Returns the number of bytes allocated for a single row of a bitmap image.
- [CGImageGetColorSpace](cgimage/colorspace.md) — Return the color space for a bitmap image.
- [CGImageGetAlphaInfo](cgimage/alphainfo.md) — Returns the alpha channel information for a bitmap image.
- [CGImageAlphaInfo](cgimagealphainfo.md) — Storage options for alpha component data.
- [CGImageGetDataProvider](cgimage/dataprovider.md) — Returns the data provider for a bitmap image or image mask.
- [CGImageGetDecode](cgimage/decode.md) — Returns the decode array for a bitmap image.
- [CGImageGetShouldInterpolate](cgimage/shouldinterpolate.md) — Returns the interpolation setting for a bitmap image.
- [CGImageGetRenderingIntent](cgimage/renderingintent.md) — Returns the rendering intent setting for a bitmap image.
- [CGImageGetBitmapInfo](cgimage/bitmapinfo.md) — Returns the bitmap information for a bitmap image.
- [CGBitmapInfo](cgbitmapinfo.md) — Component information for a bitmap image.
- [CGImageGetUTType](cgimage/uttype.md) — The Universal Type Identifier for the image.

### Copying an image

- [CGImageCreateCopy](<cgimage/copy().md>) — Creates a copy of a bitmap image.
- [CGImageCreateCopyWithColorSpace](<cgimage/copy(colorspace_).md>) — Creates a copy of a bitmap image, replacing its colorspace.

### Creating images by modifying an image

- [CGImageCreateWithImageInRect](<cgimage/cropping(to_).md>) — Creates a bitmap image using the data contained within a subregion of an existing bitmap image.
- [CGImageCreateWithMask](<cgimage/masking(__).md>) — Creates a bitmap image from an existing image and an image mask.
- [copy(maskingColorComponents:)](<cgimage/copy(maskingcolorcomponents_).md>)

### Creating image masks

- [CGImageMaskCreate](<cgimage/init(maskwidth_height_bitspercomponent_bitsperpixel_bytesperrow_provider_decode_shouldinterpolate_).md>) — Creates a bitmap image mask from data supplied by a data provider.

### Adopting high dynamic range (HDR)

- [Enhancing high dynamic range image rendering](adopting-advancements-in-hdr-image-rendering.md) — Improve your app’s High Dynamic Range (HDR) image support with metadata.
- [CGImageGetContentHeadroom](cgimage/contentheadroom.md)
- [CGImageCalculateContentHeadroom](cgimage/calculatedcontentheadroom.md)
- [CGImageGetContentAverageLightLevel](cgimage/contentaveragelightlevel.md)
- [CGImageCalculateContentAverageLightLevel](cgimage/calculatedcontentaveragelightlevel.md)
- [CGImageCreateCopyWithContentAverageLightLevel](<cgimage/copy(contentaveragelightlevel_).md>)
- [CGImageCreateCopyWithCalculatedHDRStats](<cgimage/copywithcalculatedhdrstats().md>)

### Constants

- [CGImageAlphaInfo](cgimagealphainfo.md) — Storage options for alpha component data.
- [CGBitmapInfo](cgbitmapinfo.md) — Component information for a bitmap image.
- [Host Endian Bitmap Formats](host-endian-bitmap-formats.md) — Bit-depth constants for image bitmaps in host-endian byte order.

### Working with Core Foundation types

- [CGImageGetTypeID](cgimage/typeid.md) — Returns the type identifier for CGImage objects.

### Instance properties

- [CGImageGetByteOrderInfo](cgimage/byteorderinfo.md)
- [CGImageContainsImageSpecificToneMappingMetadata](cgimage/containsimagespecifictonemappingmetadata.md)
- [CGImageGetContentHeadroom](cgimage/contentheadroom.md)
- [CGImageGetPixelFormatInfo](cgimage/pixelformatinfo.md)
- [CGImageShouldToneMap](cgimage/shouldtonemap.md)

## See Also

### Related Documentation

- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)

### 2D Drawing

- [CGContext](cgcontext.md) — A Quartz 2D drawing environment.
- [CGPath](cgpath.md) — An immutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [CGMutablePath](cgmutablepath.md) — A mutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [CGLayer](cglayer.md) — An offscreen context for reusing content drawn with Core Graphics.

---
title: 'imageAccumulatorWithExtent:format:colorSpace:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimageaccumulator/imageaccumulatorwithextent:format:colorspace:'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageaccumulator/imageaccumulatorwithextent:format:colorspace:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageaccumulator/imageaccumulatorwithextent%3Aformat%3Acolorspace%3A.json'
content_hash: 'sha256:e81db206f1c23895'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageAccumulator](../ciimageaccumulator.md)

# imageAccumulatorWithExtent:format:colorSpace:

<sub>Type Method</sub>

Creates an image accumulator with the specified extent, pixel format, and color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (instancetype) imageAccumulatorWithExtent:(CGRect) extent format:(CIFormat) format colorSpace:(CGColorSpaceRef) colorSpace;
```

## Parameters

- `extent` — A rectangle that specifies the x-value of the rectangle origin, the y-value of the rectangle origin, and the width and height.

- `format` — The format and size of each pixel. You must supply a pixel format constant, such as  kCIFormatARGB8  (32 bit-per-pixel, fixed-point pixel format) or kCIFormatRGBAf (128 bit-per-pixel, floating-point pixel format). See [CIImage](../ciimage.md) for more information about pixel format constants.

- `colorSpace` — A [CGColorSpace](../../coregraphics/cgcolorspace.md) object describing the color space for the image accumulator.

## Return Value

The image accumulator object.

## See Also

### Related Documentation

- [- initWithExtent:format:](<init(extent_format_).md>) — Initializes an image accumulator with the specified extent and pixel format.

### Creating an Image Accumulator

- [imageAccumulatorWithExtent:format:](imageaccumulatorwithextent_format_.md) — Creates an image accumulator with the specified extent and pixel format.

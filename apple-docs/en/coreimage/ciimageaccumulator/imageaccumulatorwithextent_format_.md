---
title: 'imageAccumulatorWithExtent:format:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimageaccumulator/imageaccumulatorwithextent:format:'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageaccumulator/imageaccumulatorwithextent:format:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageaccumulator/imageaccumulatorwithextent%3Aformat%3A.json'
content_hash: 'sha256:d38161c4cb25fd05'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageAccumulator](../ciimageaccumulator.md)

# imageAccumulatorWithExtent:format:

<sub>Type Method</sub>

Creates an image accumulator with the specified extent and pixel format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (instancetype) imageAccumulatorWithExtent:(CGRect) extent format:(CIFormat) format;
```

## Parameters

- `extent` — A rectangle that specifies the x-value of the rectangle origin, the y-value of the rectangle origin, and the width and height.

- `format` — The format and size of each pixel. You must supply a pixel format constant, such as  kCIFormatARGB8  (32 bit-per-pixel, fixed-point pixel format) or kCIFormatRGBAf (128 bit-per-pixel, floating-point pixel format). See [CIImage](../ciimage.md) for more information about pixel format constants.

## Return Value

The image accumulator object.

## See Also

### Related Documentation

- [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)
- [- initWithExtent:format:](<init(extent_format_).md>) — Initializes an image accumulator with the specified extent and pixel format.

### Creating an Image Accumulator

- [imageAccumulatorWithExtent:format:colorSpace:](imageaccumulatorwithextent_format_colorspace_.md) — Creates an image accumulator with the specified extent, pixel format, and color space.

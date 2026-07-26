---
title: 'init(extent:format:colorSpace:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimageaccumulator/init(extent:format:colorspace:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageaccumulator/init(extent:format:colorspace:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageaccumulator/init%28extent%3Aformat%3Acolorspace%3A%29.json'
content_hash: 'sha256:c7965c5cd41768aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageAccumulator](../ciimageaccumulator.md)

# init(extent:format:colorSpace:)

<sub>Initializer</sub>

Initializes an image accumulator with the specified extent, pixel format, and color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init?(extent: CGRect, format: CIFormat, colorSpace: CGColorSpace)
```

## Parameters

- `extent` — A rectangle that specifies the x-value of the rectangle origin, the y-value of the rectangle origin, and the width and height.

- `format` — The format and size of each pixel. You must supply a pixel format constant, such askCIFormatARGB8  (32 bit-per-pixel, fixed-point pixel format) or kCIFormatRGBAf (128 bit-per-pixel, floating-point pixel format). See [CIImage](../ciimage.md) for more information about pixel format constants.

- `colorSpace` — A [CGColorSpace](../../coregraphics/cgcolorspace.md) object describing the color space for the image accumulator.

## Return Value

The initialized image accumulator object.

## See Also

### Initializing an Image Accumulator

- [- initWithExtent:format:](<init(extent_format_).md>) — Initializes an image accumulator with the specified extent and pixel format.

---
title: 'init(extent:format:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimageaccumulator/init(extent:format:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageaccumulator/init(extent:format:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageaccumulator/init%28extent%3Aformat%3A%29.json'
content_hash: 'sha256:ae04e9aef7257026'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageAccumulator](../ciimageaccumulator.md)

# init(extent:format:)

<sub>Initializer</sub>

Initializes an image accumulator with the specified extent and pixel format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init?(extent: CGRect, format: CIFormat)
```

## Parameters

- `extent` — A rectangle that specifies the x-value of the rectangle origin, the y-value of the rectangle origin, and the width and height.

- `format` — The format and size of each pixel. You must supply a pixel format constant, such askCIFormatARGB8  (32 bit-per-pixel, fixed-point pixel format) or kCIFormatRGBAf (128 bit-per-pixel, floating-point pixel format). See [CIImage](../ciimage.md) for more information about pixel format constants.

## Return Value

The initialized image accumulator object.

## See Also

### Initializing an Image Accumulator

- [- initWithExtent:format:colorSpace:](<init(extent_format_colorspace_).md>) — Initializes an image accumulator with the specified extent, pixel format, and color space.

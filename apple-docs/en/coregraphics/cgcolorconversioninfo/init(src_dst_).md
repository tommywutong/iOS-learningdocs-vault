---
title: 'init(src:dst:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcolorconversioninfo/init(src:dst:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfo/init(src:dst:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorconversioninfo/init%28src%3Adst%3A%29.json'
content_hash: 'sha256:8b855c71ba9afa54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColorConversionInfo](../cgcolorconversioninfo.md)

# init(src:dst:)

<sub>Initializer</sub>

Creates a conversion between two specified color spaces.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(src: CGColorSpace, dst: CGColorSpace)
```

## Parameters

- `src` — The source color space from which color values are to be converted.

- `dst` — The destination color space to which colors are to be converted.

## Return Value

A color conversion object, or `nil` if no conversion between the specified color spaces is allowed.

## Discussion

The source and destination color spaces must be calibrated color spaces (that is, not device-specific or indexed color spaces).

You can use a color conversion object to create [MPSImageConversion](../../metalperformanceshaders/mpsimageconversion.md) filters that perform GPU-accelerated color space conversion.

## See Also

### Creating a Color Conversion

- [CGColorConversionInfoCreateWithOptions](<init(optionssrc_dst_options_).md>)
- [CGColorConversionInfoTransformType](../cgcolorconversioninfotransformtype.md) — Constants describing how a color conversion uses color spaces.

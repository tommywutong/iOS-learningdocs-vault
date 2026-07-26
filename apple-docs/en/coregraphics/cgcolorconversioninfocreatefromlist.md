---
title: CGColorConversionInfoCreateFromList
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorconversioninfocreatefromlist
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfocreatefromlist'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorconversioninfocreatefromlist.json'
content_hash: 'sha256:19249b76eef764b9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGColorConversionInfoCreateFromList

<sub>Function</sub>

Creates a conversion between an arbitrary number of specified color spaces.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGColorConversionInfoRefCGColorConversionInfoCreateFromList(CFDictionaryRef options, CGColorSpaceRef , CGColorConversionInfoTransformType , CGColorRenderingIntent , ...);
```

### Parameters

- **options** — A dictionary containing options for color space conversion. See [CGColorConversionInfo](cgcolorconversioninfo.md).
- **colorSpace** — The first color space in the conversion.
- **transformType** — The role of the first color space to the conversion process. See [CGColorConversionInfoTransformType](cgcolorconversioninfotransformtype.md).
- **renderingIntent** — The rendering intent to use with the first color space. See [CGColorRenderingIntent](cgcolorrenderingintent.md).
- **…** — A `NULL`-terminated list of additional `colorSpace, transformType, renderingIntent` triplets.

### Returns

A color conversion object, or `nil` if no conversion between the specified color spaces is allowed.

## Discussion

To call this function you must pass a triplet of color space, transform type, and rendering intent for each color space in the chain of conversions. For example, the following code is equivalent to calling [CGColorConversionInfoCreate](<cgcolorconversioninfo/init(src_dst_).md>):

```objc
// convert from `src` to `dst` space with default intent
CGColorConversionInfoCreateFromList(NULL,
    src, kCGColorConversionTransformFromSpace, kCGRenderingIntentDefault,
    dst, kCGColorConversionTransformToSpace,   kCGRenderingIntentDefault,
    NULL);
```

To extend this example to convert through an intermediate color space, insert another space/type/intent triplet between the `src` and `dst` lines, using the [kCGColorConversionTransformApplySpace](cgcolorconversioninfotransformtype/transformapplyspace.md) type.

The listed color spaces must be calibrated color spaces (that is, not device-specific or indexed color spaces), and the list must contain at least two color spaces (that is, two triplets of space, type, and intent).

You can use a color conversion object to create [MPSImageConversion](../metalperformanceshaders/mpsimageconversion.md) filters that perform GPU-accelerated color space conversion.

## See Also

### Creating a Color Conversion

- [CGColorConversionInfoCreate](<cgcolorconversioninfo/init(src_dst_).md>) — Creates a conversion between two specified color spaces.
- [CGColorConversionInfoCreateWithOptions](<cgcolorconversioninfo/init(optionssrc_dst_options_).md>)
- [CGColorConversionInfoTransformType](cgcolorconversioninfotransformtype.md) — Constants describing how a color conversion uses color spaces.

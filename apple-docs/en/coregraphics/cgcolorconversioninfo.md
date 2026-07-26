---
title: CGColorConversionInfo
framework: Core Graphics
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorconversioninfo
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorconversioninfo.json'
content_hash: 'sha256:d0b32d62459fe84d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGColorConversionInfo

<sub>Class</sub>

An object that describes how to convert between color spaces for use by other system services.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CGColorConversionInfo
```

## Overview

A [CGColorConversionInfo](cgcolorconversioninfo.md) object specifies a conversion between two or more color spaces, including information about the intent of the conversion. You use color conversion objects to specify the work to be done by an [MPSImageConversion](../metalperformanceshaders/mpsimageconversion.md) filter, which can then perform GPU-accelerated image conversion.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a Color Conversion

- [CGColorConversionInfoCreate](<cgcolorconversioninfo/init(src_dst_).md>) — Creates a conversion between two specified color spaces.
- [CGColorConversionInfoCreateWithOptions](<cgcolorconversioninfo/init(optionssrc_dst_options_).md>)
- [CGColorConversionInfoTransformType](cgcolorconversioninfotransformtype.md) — Constants describing how a color conversion uses color spaces.

### Working with Core Foundation Types

- [CGColorConversionInfoGetTypeID](cgcolorconversioninfo/typeid.md) — Returns the Core Foundation type identifier for a color conversion info data type.

### Instance Methods

- [CGColorConversionInfoConvertData](<cgcolorconversioninfo/convert(width_height_to_format_from_format_options_).md>)

### Initializers

- [CGColorConversionInfoCreateForToneMapping](<cgcolorconversioninfo/init(src_srcheadroom_dst_dstheadroom_tonemapping_options___).md>) _(deprecated)_

## See Also

### Colors and Fonts

- [CGColor](cgcolor.md) — A set of components that define a color, with a color space specifying how to interpret them.
- [CGColorSpace](cgcolorspace.md) — A profile that specifies how to interpret a color value for display.
- [CGFont](cgfont.md) — A set of character glyphs and layout information for drawing text.

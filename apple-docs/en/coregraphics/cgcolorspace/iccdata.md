---
title: iccData
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（11.0 起废弃）, iPadOS 2.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.5+（10.13 起废弃）, tvOS（11.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（4.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/coregraphics/cgcolorspace/iccdata
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorspace/iccdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorspace/iccdata.json'
content_hash: 'sha256:905b421dcdd6b42c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColorSpace](../cgcolorspace.md)

# iccData

<sub>Instance Property</sub>

Returns a copy of the ICC profile of the provided color space.

> [!warning] Deprecated
> Use [CGColorSpaceCopyICCData](<copyiccdata().md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var iccData: CFData? { get }
```

## See Also

### Examining a Color Space

- [CGColorSpaceGetBaseColorSpace](basecolorspace.md) — Returns the base color space of a pattern or indexed color space.
- [CGColorSpaceGetNumberOfComponents](numberofcomponents.md) — Returns the number of color components in a color space.
- [CGColorSpaceGetModel](model.md) — Returns the color space model of the provided color space.
- [CGColorSpaceModel](../cgcolorspacemodel.md) — Models for color spaces.
- [colorTable](colortable.md) — The entries in the color table of an indexed color space.
- [CGColorSpaceCopyICCData](<copyiccdata().md>) — Returns a copy of the ICC profile data of the provided color space.
- [CGColorSpaceCopyPropertyList](<copypropertylist().md>) — Returns a copy of the color space’s properties.
- [CGColorSpaceCopyName](name.md) — Returns the name used to create the specified color space.
- [CGColorSpaceSupportsOutput](supportsoutput.md) — Returns a Boolean indicating whether the color space can be used as a destination color space.
- [CGColorSpaceIsWideGamutRGB](iswidegamutrgb.md) — Returns whether the RGB color space covers a significant portion of the NTSC color gamut.

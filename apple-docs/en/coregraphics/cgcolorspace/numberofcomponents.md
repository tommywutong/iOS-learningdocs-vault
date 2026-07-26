---
title: numberOfComponents
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorspace/numberofcomponents
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorspace/numberofcomponents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorspace/numberofcomponents.json'
content_hash: 'sha256:7c640fb76d5eb413'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColorSpace](../cgcolorspace.md)

# numberOfComponents

<sub>Instance Property</sub>

Returns the number of color components in a color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var numberOfComponents: Int { get }
```

## Discussion

A color space defines an n-dimensional space whose dimensions (or components) represent intensity values. Use this function to obtain the number of components in a given color space: for example, in an RGB color space this function returns 3 (for the three intensity values red, green, and blue).

## See Also

### Examining a Color Space

- [CGColorSpaceGetBaseColorSpace](basecolorspace.md) — Returns the base color space of a pattern or indexed color space.
- [CGColorSpaceGetModel](model.md) — Returns the color space model of the provided color space.
- [CGColorSpaceModel](../cgcolorspacemodel.md) — Models for color spaces.
- [colorTable](colortable.md) — The entries in the color table of an indexed color space.
- [CGColorSpaceCopyICCData](<copyiccdata().md>) — Returns a copy of the ICC profile data of the provided color space.
- [CGColorSpaceCopyPropertyList](<copypropertylist().md>) — Returns a copy of the color space’s properties.
- [CGColorSpaceCopyICCProfile](iccdata.md) — Returns a copy of the ICC profile of the provided color space. _(deprecated)_
- [CGColorSpaceCopyName](name.md) — Returns the name used to create the specified color space.
- [CGColorSpaceSupportsOutput](supportsoutput.md) — Returns a Boolean indicating whether the color space can be used as a destination color space.
- [CGColorSpaceIsWideGamutRGB](iswidegamutrgb.md) — Returns whether the RGB color space covers a significant portion of the NTSC color gamut.

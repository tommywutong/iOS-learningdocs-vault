---
title: isWideGamutRGB
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorspace/iswidegamutrgb
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorspace/iswidegamutrgb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorspace/iswidegamutrgb.json'
content_hash: 'sha256:64fb46106c54af17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColorSpace](../cgcolorspace.md)

# isWideGamutRGB

<sub>Instance Property</sub>

Returns whether the RGB color space covers a significant portion of the NTSC color gamut.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isWideGamutRGB: Bool { get }
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
- [CGColorSpaceCopyICCProfile](iccdata.md) — Returns a copy of the ICC profile of the provided color space. _(deprecated)_
- [CGColorSpaceCopyName](name.md) — Returns the name used to create the specified color space.
- [CGColorSpaceSupportsOutput](supportsoutput.md) — Returns a Boolean indicating whether the color space can be used as a destination color space.

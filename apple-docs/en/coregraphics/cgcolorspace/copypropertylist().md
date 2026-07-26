---
title: copyPropertyList()
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorspace/copypropertylist()
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorspace/copypropertylist()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorspace/copypropertylist%28%29.json'
content_hash: 'sha256:beddca049bfa5b77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColorSpace](../cgcolorspace.md)

# copyPropertyList()

<sub>Instance Method</sub>

Returns a copy of the color space’s properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func copyPropertyList() -> CFPropertyList?
```

## See Also

### Related Documentation

- [CGColorSpaceCreateWithPropertyList](<init(propertylistplist_).md>) — Creates a color space from a property list.

### Examining a Color Space

- [CGColorSpaceGetBaseColorSpace](basecolorspace.md) — Returns the base color space of a pattern or indexed color space.
- [CGColorSpaceGetNumberOfComponents](numberofcomponents.md) — Returns the number of color components in a color space.
- [CGColorSpaceGetModel](model.md) — Returns the color space model of the provided color space.
- [CGColorSpaceModel](../cgcolorspacemodel.md) — Models for color spaces.
- [colorTable](colortable.md) — The entries in the color table of an indexed color space.
- [CGColorSpaceCopyICCData](<copyiccdata().md>) — Returns a copy of the ICC profile data of the provided color space.
- [CGColorSpaceCopyICCProfile](iccdata.md) — Returns a copy of the ICC profile of the provided color space. _(deprecated)_
- [CGColorSpaceCopyName](name.md) — Returns the name used to create the specified color space.
- [CGColorSpaceSupportsOutput](supportsoutput.md) — Returns a Boolean indicating whether the color space can be used as a destination color space.
- [CGColorSpaceIsWideGamutRGB](iswidegamutrgb.md) — Returns whether the RGB color space covers a significant portion of the NTSC color gamut.

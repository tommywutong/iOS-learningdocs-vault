---
title: colorTable
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 7.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorspace/colortable
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorspace/colortable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorspace/colortable.json'
content_hash: 'sha256:b7aa6d99ca95073e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColorSpace](../cgcolorspace.md)

# colorTable

<sub>Instance Property</sub>

The entries in the color table of an indexed color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var colorTable: [UInt8]? { get }
```

## Discussion

If the color space is an indexed color space, this array contains color component values for the colors in the color space, in the same format you use when creating an indexed color space with the [CGColorSpaceCreateIndexed](<init(indexedbasespace_last_colortable_).md>) initializer.

If the color space is not an indexed color space, this property’s value is `nil`. To determine whether a color space is an indexed color space, read the [CGColorSpaceGetModel](model.md) property.

## See Also

### Examining a Color Space

- [CGColorSpaceGetBaseColorSpace](basecolorspace.md) — Returns the base color space of a pattern or indexed color space.
- [CGColorSpaceGetNumberOfComponents](numberofcomponents.md) — Returns the number of color components in a color space.
- [CGColorSpaceGetModel](model.md) — Returns the color space model of the provided color space.
- [CGColorSpaceModel](../cgcolorspacemodel.md) — Models for color spaces.
- [CGColorSpaceCopyICCData](<copyiccdata().md>) — Returns a copy of the ICC profile data of the provided color space.
- [CGColorSpaceCopyPropertyList](<copypropertylist().md>) — Returns a copy of the color space’s properties.
- [CGColorSpaceCopyICCProfile](iccdata.md) — Returns a copy of the ICC profile of the provided color space. _(deprecated)_
- [CGColorSpaceCopyName](name.md) — Returns the name used to create the specified color space.
- [CGColorSpaceSupportsOutput](supportsoutput.md) — Returns a Boolean indicating whether the color space can be used as a destination color space.
- [CGColorSpaceIsWideGamutRGB](iswidegamutrgb.md) — Returns whether the RGB color space covers a significant portion of the NTSC color gamut.

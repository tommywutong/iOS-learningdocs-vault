---
title: copyICCData()
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorspace/copyiccdata()
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorspace/copyiccdata()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorspace/copyiccdata%28%29.json'
content_hash: 'sha256:12a77fad2ea1bfc5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColorSpace](../cgcolorspace.md)

# copyICCData()

<sub>Instance Method</sub>

Returns a copy of the ICC profile data of the provided color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func copyICCData() -> CFData?
```

## Return Value

The ICC profile data or `NULL` if the color space does not have an ICC data profile.

## See Also

### Examining a Color Space

- [CGColorSpaceGetBaseColorSpace](basecolorspace.md) — Returns the base color space of a pattern or indexed color space.
- [CGColorSpaceGetNumberOfComponents](numberofcomponents.md) — Returns the number of color components in a color space.
- [CGColorSpaceGetModel](model.md) — Returns the color space model of the provided color space.
- [CGColorSpaceModel](../cgcolorspacemodel.md) — Models for color spaces.
- [colorTable](colortable.md) — The entries in the color table of an indexed color space.
- [CGColorSpaceCopyPropertyList](<copypropertylist().md>) — Returns a copy of the color space’s properties.
- [CGColorSpaceCopyICCProfile](iccdata.md) — Returns a copy of the ICC profile of the provided color space. _(deprecated)_
- [CGColorSpaceCopyName](name.md) — Returns the name used to create the specified color space.
- [CGColorSpaceSupportsOutput](supportsoutput.md) — Returns a Boolean indicating whether the color space can be used as a destination color space.
- [CGColorSpaceIsWideGamutRGB](iswidegamutrgb.md) — Returns whether the RGB color space covers a significant portion of the NTSC color gamut.

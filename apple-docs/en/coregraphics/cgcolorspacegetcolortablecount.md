---
title: CGColorSpaceGetColorTableCount
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorspacegetcolortablecount
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorspacegetcolortablecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorspacegetcolortablecount.json'
content_hash: 'sha256:2f02c810a2373434'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGColorSpaceGetColorTableCount

<sub>Function</sub>

Returns the number of entries in the color table of an indexed color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern size_t CGColorSpaceGetColorTableCount(CGColorSpaceRef space);
```

## Parameters

- `space` — A color space object for an indexed color space.

## Return Value

The number of entries in the color table of the `space` parameter if the color space is an indexed color space; otherwise, returns `0`.

## See Also

### Examining a Color Space

- [CGColorSpaceGetBaseColorSpace](cgcolorspace/basecolorspace.md) — Returns the base color space of a pattern or indexed color space.
- [CGColorSpaceGetNumberOfComponents](cgcolorspace/numberofcomponents.md) — Returns the number of color components in a color space.
- [CGColorSpaceGetModel](cgcolorspace/model.md) — Returns the color space model of the provided color space.
- [CGColorSpaceModel](cgcolorspacemodel.md) — Models for color spaces.
- [CGColorSpaceCopyICCData](<cgcolorspace/copyiccdata().md>) — Returns a copy of the ICC profile data of the provided color space.
- [CGColorSpaceCopyPropertyList](<cgcolorspace/copypropertylist().md>) — Returns a copy of the color space’s properties.
- [CGColorSpaceCopyICCProfile](cgcolorspace/iccdata.md) — Returns a copy of the ICC profile of the provided color space. _(deprecated)_
- [CGColorSpaceCopyName](cgcolorspace/name.md) — Returns the name used to create the specified color space.
- [CGColorSpaceSupportsOutput](cgcolorspace/supportsoutput.md) — Returns a Boolean indicating whether the color space can be used as a destination color space.
- [CGColorSpaceIsWideGamutRGB](cgcolorspace/iswidegamutrgb.md) — Returns whether the RGB color space covers a significant portion of the NTSC color gamut.
- [CGColorSpaceGetColorTable](cgcolorspacegetcolortable.md) — Copies the entries in the color table of an indexed color space.

---
title: CGColorSpaceModel
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorspacemodel
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorspacemodel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorspacemodel.json'
content_hash: 'sha256:5e08763112f331fe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGColorSpaceModel

<sub>Enumeration</sub>

Models for color spaces.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CGColorSpaceModel
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCGColorSpaceModelUnknown](cgcolorspacemodel/unknown.md) — An unknown color space model.
- [kCGColorSpaceModelMonochrome](cgcolorspacemodel/monochrome.md) — A monochrome color space model.
- [kCGColorSpaceModelRGB](cgcolorspacemodel/rgb.md) — An RGB color space model.
- [kCGColorSpaceModelCMYK](cgcolorspacemodel/cmyk.md) — A CMYK color space model.
- [kCGColorSpaceModelLab](cgcolorspacemodel/lab.md) — A Lab color space model.
- [kCGColorSpaceModelDeviceN](cgcolorspacemodel/devicen.md) — A DeviceN color space model.
- [kCGColorSpaceModelIndexed](cgcolorspacemodel/indexed.md) — An indexed color space model.
- [kCGColorSpaceModelPattern](cgcolorspacemodel/pattern.md) — A pattern color space model.
- [kCGColorSpaceModelXYZ](cgcolorspacemodel/xyz.md) — An XYZ color space model.

### Initializers

- [init(rawValue:)](<cgcolorspacemodel/init(rawvalue_).md>)

## See Also

### Examining a Color Space

- [CGColorSpaceGetBaseColorSpace](cgcolorspace/basecolorspace.md) — Returns the base color space of a pattern or indexed color space.
- [CGColorSpaceGetNumberOfComponents](cgcolorspace/numberofcomponents.md) — Returns the number of color components in a color space.
- [CGColorSpaceGetModel](cgcolorspace/model.md) — Returns the color space model of the provided color space.
- [colorTable](cgcolorspace/colortable.md) — The entries in the color table of an indexed color space.
- [CGColorSpaceCopyICCData](<cgcolorspace/copyiccdata().md>) — Returns a copy of the ICC profile data of the provided color space.
- [CGColorSpaceCopyPropertyList](<cgcolorspace/copypropertylist().md>) — Returns a copy of the color space’s properties.
- [CGColorSpaceCopyICCProfile](cgcolorspace/iccdata.md) — Returns a copy of the ICC profile of the provided color space. _(deprecated)_
- [CGColorSpaceCopyName](cgcolorspace/name.md) — Returns the name used to create the specified color space.
- [CGColorSpaceSupportsOutput](cgcolorspace/supportsoutput.md) — Returns a Boolean indicating whether the color space can be used as a destination color space.
- [CGColorSpaceIsWideGamutRGB](cgcolorspace/iswidegamutrgb.md) — Returns whether the RGB color space covers a significant portion of the NTSC color gamut.

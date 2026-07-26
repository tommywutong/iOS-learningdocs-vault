---
title: CGColorSpace
framework: Core Graphics
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorspace
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorspace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorspace.json'
content_hash: 'sha256:a61f95280c9d03ce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGColorSpace

<sub>Class</sub>

A profile that specifies how to interpret a color value for display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CGColorSpace
```

## Overview

A color space is multi-dimensional, and each dimension represents a specific color component. For example, the colors in an RGB color space have three dimensions or components—red, green, and blue. The intensity of each component is represented by floating point values—their range and meaning depends on the color space in question.

Different types of devices (scanners, monitors, printers) operate within different color spaces (RGB, CMYK, grayscale). Additionally, two devices of the same type (for example, color displays from different manufacturers) may operate within the same kind of color space, yet still produce a different range of colors, or gamut. Color spaces that are correctly specified ensure that an image has a consistent appearance regardless of the output device.

Core Graphics supports several kinds of color spaces:

- Calibrated color spaces ensure that colors appear the same when displayed on different devices. The visual appearance of the color is preserved, as far as the capabilities of the device allow.
- Device-dependent color spaces are tied to the system of color representation of a particular device. Device color spaces are not recommended when high-fidelity color preservation is important.
- Special color spaces—indexed and pattern. An indexed color space contains a color table with up to 256 entries and a base color space to which the color table entries are mapped. Each entry in the color table specifies one color in the base color space. A pattern color space is used when stroking or filling with a pattern.

## Relationships

- **Conforms To**: [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md), [Copyable](../swift/copyable.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating Color Spaces

- [CGColorSpaceCreateCalibratedGray](<cgcolorspace/init(calibratedgraywhitepoint_blackpoint_gamma_).md>) — Creates a calibrated grayscale color space.
- [CGColorSpaceCreateCalibratedRGB](<cgcolorspace/init(calibratedrgbwhitepoint_blackpoint_gamma_matrix_).md>) — Creates a calibrated RGB color space.
- [CGColorSpaceCreateICCBased](<cgcolorspace/init(iccbasedncomponents_range_profile_alternate_).md>) — Creates a device-independent color space that is defined according to the ICC color profile specification.
- [CGColorSpaceCreateIndexed](<cgcolorspace/init(indexedbasespace_last_colortable_).md>) — Creates an indexed color space, consisting of colors specified by a color lookup table.
- [CGColorSpaceCreateLab](<cgcolorspace/init(labwhitepoint_blackpoint_range_).md>) — Creates a device-independent color space that is relative to human color perception, according to the CIE L*a*b* standard.
- [CGColorSpaceCreatePattern](<cgcolorspace/init(patternbasespace_).md>) — Creates a pattern color space.
- [CGColorSpaceCreateWithName](<cgcolorspace/init(name_).md>) — Creates a specified type of Quartz color space.
- [CGColorSpaceCreateWithPlatformColorSpace](<cgcolorspace/init(platformcolorspaceref_).md>) — Creates a platform-specific color space. _(deprecated)_
- [CGColorSpaceCreateWithICCData](<cgcolorspace/init(iccdata_).md>) — Creates an ICC-based color space using the ICC profile contained in the specified data.
- [CGColorSpaceCreateWithPropertyList](<cgcolorspace/init(propertylistplist_).md>) — Creates a color space from a property list.
- [CGColorSpaceCreateDeviceRGB](<cgcolorspacecreatedevicergb().md>) — Creates a device-dependent RGB color space.
- [CGColorSpaceCreateDeviceCMYK](<cgcolorspacecreatedevicecmyk().md>) — Creates a device-dependent CMYK color space.
- [CGColorSpaceCreateDeviceGray](<cgcolorspacecreatedevicegray().md>) — Creates a device-dependent grayscale color space.
- [CGColorSpaceCreateWithICCProfile](<cgcolorspace/init(iccprofiledata_).md>) — Creates an ICC-based color space using the ICC profile contained in the specified data. _(deprecated)_

### Examining a Color Space

- [CGColorSpaceGetBaseColorSpace](cgcolorspace/basecolorspace.md) — Returns the base color space of a pattern or indexed color space.
- [CGColorSpaceGetNumberOfComponents](cgcolorspace/numberofcomponents.md) — Returns the number of color components in a color space.
- [CGColorSpaceGetModel](cgcolorspace/model.md) — Returns the color space model of the provided color space.
- [CGColorSpaceModel](cgcolorspacemodel.md) — Models for color spaces.
- [colorTable](cgcolorspace/colortable.md) — The entries in the color table of an indexed color space.
- [CGColorSpaceCopyICCData](<cgcolorspace/copyiccdata().md>) — Returns a copy of the ICC profile data of the provided color space.
- [CGColorSpaceCopyPropertyList](<cgcolorspace/copypropertylist().md>) — Returns a copy of the color space’s properties.
- [CGColorSpaceCopyICCProfile](cgcolorspace/iccdata.md) — Returns a copy of the ICC profile of the provided color space. _(deprecated)_
- [CGColorSpaceCopyName](cgcolorspace/name.md) — Returns the name used to create the specified color space.
- [CGColorSpaceSupportsOutput](cgcolorspace/supportsoutput.md) — Returns a Boolean indicating whether the color space can be used as a destination color space.
- [CGColorSpaceIsWideGamutRGB](cgcolorspace/iswidegamutrgb.md) — Returns whether the RGB color space covers a significant portion of the NTSC color gamut.

### Accessing System-Defined Color Spaces

- [kCGColorSpaceDisplayP3](cgcolorspace/displayp3.md) — The Display P3 color space, created by Apple.
- [kCGColorSpaceDisplayP3_HLG](cgcolorspace/displayp3_hlg.md) — The Display P3 color space, using the HLG transfer function.
- [kCGColorSpaceDisplayP3_PQ_EOTF](cgcolorspace/displayp3_pq_eotf.md) — The Display P3 color space, using the PQ transfer function. _(deprecated)_
- [kCGColorSpaceExtendedLinearDisplayP3](cgcolorspace/extendedlineardisplayp3.md) — The Display P3 color space with a linear transfer function and extended-range values.
- [kCGColorSpaceSRGB](cgcolorspace/srgb.md) — The standard Red Green Blue (sRGB) color space.
- [kCGColorSpaceLinearSRGB](cgcolorspace/linearsrgb.md) — The sRGB color space with a linear transfer function.
- [kCGColorSpaceExtendedSRGB](cgcolorspace/extendedsrgb.md) — The extended sRGB color space.
- [kCGColorSpaceExtendedLinearSRGB](cgcolorspace/extendedlinearsrgb.md) — The sRGB color space with a linear transfer function and extended-range values.
- [kCGColorSpaceGenericGrayGamma2_2](cgcolorspace/genericgraygamma2_2.md) — The generic gray color space that has an exponential transfer function with a power of 2.2.
- [kCGColorSpaceExtendedGray](cgcolorspace/extendedgray.md) — The extended gray color space.
- [kCGColorSpaceLinearGray](cgcolorspace/lineargray.md) — The gray color space using a linear transfer function.
- [kCGColorSpaceExtendedLinearGray](cgcolorspace/extendedlineargray.md) — The extended gray color space with a linear transfer function.
- [kCGColorSpaceGenericCMYK](cgcolorspace/genericcmyk.md) — The generic CMYK color space.
- [kCGColorSpaceGenericRGBLinear](cgcolorspace/genericrgblinear.md) — The generic RGB color space with a linear transfer function.
- [kCGColorSpaceGenericXYZ](cgcolorspace/genericxyz.md) — The XYZ color space, as defined by the CIE 1931 standard.
- [kCGColorSpaceGenericLab](cgcolorspace/genericlab.md) — The generic LAB color space.
- [kCGColorSpaceACESCGLinear](cgcolorspace/acescglinear.md) — The ACEScg color space.
- [kCGColorSpaceAdobeRGB1998](cgcolorspace/adobergb1998.md) — The Adobe RGB (1998) color space.
- [kCGColorSpaceDCIP3](cgcolorspace/dcip3.md) — The DCI P3 color space, which is the digital cinema standard.
- [kCGColorSpaceITUR_709](cgcolorspace/itur_709.md) — The recommendation of the International Telecommunication Union (ITU) Radiocommunication sector for the BT.709 color space.
- [kCGColorSpaceROMMRGB](cgcolorspace/rommrgb.md) — The Reference Output Medium Metric (ROMM) RGB color space.
- [kCGColorSpaceITUR_2020](cgcolorspace/itur_2020.md) — The recommendation of the International Telecommunication Union (ITU) Radiocommunication sector for the BT.2020 color space.
- [kCGColorSpaceITUR_2020_HLG](cgcolorspace/itur_2020_hlg.md) — The recommendation of the International Telecommunication Union (ITU) Radiocommunication sector for the BT.2020 color space, with the HLG transfer function. _(deprecated)_
- [kCGColorSpaceITUR_2020_PQ_EOTF](cgcolorspace/itur_2020_pq_eotf.md) — The recommendation of the International Telecommunication Union (ITU) Radiocommunication sector for the BT.2020 color space, with the PQ transfer function. _(deprecated)_
- [kCGColorSpaceExtendedLinearITUR_2020](cgcolorspace/extendedlinearitur_2020.md) — The recommendation of the International Telecommunication Union (ITU) Radiocommunication sector for the BT.2020 color space, with a linear transfer function and extended range values.
- [kCGColorSpaceCoreMedia709](cgcolorspace/coremedia709.md)
- [kCGColorSpaceDisplayP3_PQ](cgcolorspace/displayp3_pq.md)
- [kCGColorSpaceExtendedDisplayP3](cgcolorspace/extendeddisplayp3.md)
- [kCGColorSpaceExtendedITUR_2020](cgcolorspace/extendeditur_2020.md)
- [kCGColorSpaceITUR_2020_PQ](cgcolorspace/itur_2020_pq.md) _(deprecated)_
- [kCGColorSpaceITUR_2020_sRGBGamma](cgcolorspace/itur_2020_srgbgamma.md)
- [kCGColorSpaceITUR_2100_HLG](cgcolorspace/itur_2100_hlg.md)
- [kCGColorSpaceITUR_2100_PQ](cgcolorspace/itur_2100_pq.md)
- [kCGColorSpaceITUR_709_HLG](cgcolorspace/itur_709_hlg.md)
- [kCGColorSpaceITUR_709_PQ](cgcolorspace/itur_709_pq.md)
- [kCGColorSpaceLinearDisplayP3](cgcolorspace/lineardisplayp3.md)
- [kCGColorSpaceLinearITUR_2020](cgcolorspace/linearitur_2020.md)

### Working with Core Foundation Types

- [CGColorSpaceGetTypeID](cgcolorspace/typeid.md) — Returns the Core Foundation type identifier for Quartz color spaces.

### Data Types

- [CGColorRenderingIntent](cgcolorrenderingintent.md) — Handling options for colors that are not located within the destination color space of a graphics context.

### Instance Methods

- [CGColorSpaceIsHDR](<cgcolorspace/ishdr().md>)

## See Also

### Related Documentation

- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)

### Colors and Fonts

- [CGColor](cgcolor.md) — A set of components that define a color, with a color space specifying how to interpret them.
- [CGColorConversionInfo](cgcolorconversioninfo.md) — An object that describes how to convert between color spaces for use by other system services.
- [CGFont](cgfont.md) — A set of character glyphs and layout information for drawing text.

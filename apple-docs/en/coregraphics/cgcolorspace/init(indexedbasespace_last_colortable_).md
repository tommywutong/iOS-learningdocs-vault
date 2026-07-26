---
title: 'init(indexedBaseSpace:last:colorTable:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcolorspace/init(indexedbasespace:last:colortable:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorspace/init(indexedbasespace:last:colortable:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorspace/init%28indexedbasespace%3Alast%3Acolortable%3A%29.json'
content_hash: 'sha256:3e612baf9dafb79c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColorSpace](../cgcolorspace.md)

# init(indexedBaseSpace:last:colorTable:)

<sub>Initializer</sub>

Creates an indexed color space, consisting of colors specified by a color lookup table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(indexedBaseSpace baseSpace: CGColorSpace, last lastIndex: Int, colorTable: UnsafePointer<UInt8>)
```

## Parameters

- `baseSpace` — The color space on which the color table is based.

- `lastIndex` — The maximum valid index value for the color table. The value must be less than or equal to 255.

- `colorTable` — An array of `m*(lastIndex+1)` bytes, where `m` is the number of color components in the base color space. Each byte is an unsigned integer in the range `0` to `255` that is scaled to the range of the corresponding color component in the base color space.

## Return Value

A new indexed color space object, or `NULL` if unsuccessful. In Objective-C, you’re responsible for releasing this object by calling [CGColorSpaceRelease](../cgcolorspacerelease.md).

## Discussion

An indexed color space contains a color table with up to 255 entries, and a base color space to which the color table entries are mapped. Each entry in the color table specifies one color in the base color space. A value in an indexed color space is treated as an index into the color table of the color space. The data in the table is in meshed format. (For example, for an RGB color space the values are R, G, B, R, G, B, and so on.)

## See Also

### Creating Color Spaces

- [CGColorSpaceCreateCalibratedGray](<init(calibratedgraywhitepoint_blackpoint_gamma_).md>) — Creates a calibrated grayscale color space.
- [CGColorSpaceCreateCalibratedRGB](<init(calibratedrgbwhitepoint_blackpoint_gamma_matrix_).md>) — Creates a calibrated RGB color space.
- [CGColorSpaceCreateICCBased](<init(iccbasedncomponents_range_profile_alternate_).md>) — Creates a device-independent color space that is defined according to the ICC color profile specification.
- [CGColorSpaceCreateLab](<init(labwhitepoint_blackpoint_range_).md>) — Creates a device-independent color space that is relative to human color perception, according to the CIE L*a*b* standard.
- [CGColorSpaceCreatePattern](<init(patternbasespace_).md>) — Creates a pattern color space.
- [CGColorSpaceCreateWithName](<init(name_).md>) — Creates a specified type of Quartz color space.
- [CGColorSpaceCreateWithPlatformColorSpace](<init(platformcolorspaceref_).md>) — Creates a platform-specific color space. _(deprecated)_
- [CGColorSpaceCreateWithICCData](<init(iccdata_).md>) — Creates an ICC-based color space using the ICC profile contained in the specified data.
- [CGColorSpaceCreateWithPropertyList](<init(propertylistplist_).md>) — Creates a color space from a property list.
- [CGColorSpaceCreateDeviceRGB](<../cgcolorspacecreatedevicergb().md>) — Creates a device-dependent RGB color space.
- [CGColorSpaceCreateDeviceCMYK](<../cgcolorspacecreatedevicecmyk().md>) — Creates a device-dependent CMYK color space.
- [CGColorSpaceCreateDeviceGray](<../cgcolorspacecreatedevicegray().md>) — Creates a device-dependent grayscale color space.
- [CGColorSpaceCreateWithICCProfile](<init(iccprofiledata_).md>) — Creates an ICC-based color space using the ICC profile contained in the specified data. _(deprecated)_

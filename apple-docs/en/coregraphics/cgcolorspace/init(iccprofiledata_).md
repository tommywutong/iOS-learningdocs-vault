---
title: 'init(iccProfileData:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+（11.0 起废弃）, iPadOS 2.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.5+（10.13 起废弃）, tvOS（11.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（4.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coregraphics/cgcolorspace/init(iccprofiledata:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorspace/init(iccprofiledata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorspace/init%28iccprofiledata%3A%29.json'
content_hash: 'sha256:30fbb2fc791d5a82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColorSpace](../cgcolorspace.md)

# init(iccProfileData:)

<sub>Initializer</sub>

Creates an ICC-based color space using the ICC profile contained in the specified data.

> [!warning] Deprecated
> Use [CGColorSpaceCreateWithICCData](<init(iccdata_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(iccProfileData data: CFData)
```

## Parameters

- `data` — The data containing the ICC profile to set for the new color space.

## Return Value

A new color space based on the specified profile.

## See Also

### Creating Color Spaces

- [CGColorSpaceCreateCalibratedGray](<init(calibratedgraywhitepoint_blackpoint_gamma_).md>) — Creates a calibrated grayscale color space.
- [CGColorSpaceCreateCalibratedRGB](<init(calibratedrgbwhitepoint_blackpoint_gamma_matrix_).md>) — Creates a calibrated RGB color space.
- [CGColorSpaceCreateICCBased](<init(iccbasedncomponents_range_profile_alternate_).md>) — Creates a device-independent color space that is defined according to the ICC color profile specification.
- [CGColorSpaceCreateIndexed](<init(indexedbasespace_last_colortable_).md>) — Creates an indexed color space, consisting of colors specified by a color lookup table.
- [CGColorSpaceCreateLab](<init(labwhitepoint_blackpoint_range_).md>) — Creates a device-independent color space that is relative to human color perception, according to the CIE L*a*b* standard.
- [CGColorSpaceCreatePattern](<init(patternbasespace_).md>) — Creates a pattern color space.
- [CGColorSpaceCreateWithName](<init(name_).md>) — Creates a specified type of Quartz color space.
- [CGColorSpaceCreateWithPlatformColorSpace](<init(platformcolorspaceref_).md>) — Creates a platform-specific color space. _(deprecated)_
- [CGColorSpaceCreateWithICCData](<init(iccdata_).md>) — Creates an ICC-based color space using the ICC profile contained in the specified data.
- [CGColorSpaceCreateWithPropertyList](<init(propertylistplist_).md>) — Creates a color space from a property list.
- [CGColorSpaceCreateDeviceRGB](<../cgcolorspacecreatedevicergb().md>) — Creates a device-dependent RGB color space.
- [CGColorSpaceCreateDeviceCMYK](<../cgcolorspacecreatedevicecmyk().md>) — Creates a device-dependent CMYK color space.
- [CGColorSpaceCreateDeviceGray](<../cgcolorspacecreatedevicegray().md>) — Creates a device-dependent grayscale color space.

---
title: 'init(propertyListPlist:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcolorspace/init(propertylistplist:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorspace/init(propertylistplist:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorspace/init%28propertylistplist%3A%29.json'
content_hash: 'sha256:801ec71107ef88d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColorSpace](../cgcolorspace.md)

# init(propertyListPlist:)

<sub>Initializer</sub>

Creates a color space from a property list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(propertyListPlist plist: CFPropertyList)
```

## Parameters

- `plist` — The list of properties to use.

## See Also

### Related Documentation

- [CGColorSpaceCopyPropertyList](<copypropertylist().md>) — Returns a copy of the color space’s properties.

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
- [CGColorSpaceCreateDeviceRGB](<../cgcolorspacecreatedevicergb().md>) — Creates a device-dependent RGB color space.
- [CGColorSpaceCreateDeviceCMYK](<../cgcolorspacecreatedevicecmyk().md>) — Creates a device-dependent CMYK color space.
- [CGColorSpaceCreateDeviceGray](<../cgcolorspacecreatedevicegray().md>) — Creates a device-dependent grayscale color space.
- [CGColorSpaceCreateWithICCProfile](<init(iccprofiledata_).md>) — Creates an ICC-based color space using the ICC profile contained in the specified data. _(deprecated)_

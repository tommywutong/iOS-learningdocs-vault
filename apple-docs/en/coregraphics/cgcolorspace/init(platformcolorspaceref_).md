---
title: 'init(platformColorSpaceRef:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+（15.0 起废弃）, iPadOS 9.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, macOS 10.0+（12.0 起废弃）, tvOS 9.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（8.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coregraphics/cgcolorspace/init(platformcolorspaceref:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorspace/init(platformcolorspaceref:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorspace/init%28platformcolorspaceref%3A%29.json'
content_hash: 'sha256:ab7d9881ed6314b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColorSpace](../cgcolorspace.md)

# init(platformColorSpaceRef:)

<sub>Initializer</sub>

Creates a platform-specific color space.

> [!warning] Deprecated
> No longer supported

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(platformColorSpaceRef ref: UnsafeRawPointer)
```

## Parameters

- `ref` — A generic pointer to a platform-specific color space. In macOS, pass a `ColorSyncProfileRef`, which is a ColorSync profile. Quartz uses this pointer (and the underlying information) only during the function call.

## Return Value

A new color space, or `NULL` if unsuccessful. In Objective-C, you’re responsible for releasing this object by calling [CGColorSpaceRelease](../cgcolorspacerelease.md).

## Discussion

Colors in a device-dependent color space are not transformed or otherwise modified when displayed on an output device — that is, there is no attempt to maintain the visual appearance of a color. As a consequence, colors in a device color space often appear different when displayed on different output devices. For this reason, device color spaces are not recommended when color preservation is important.

## See Also

### Creating Color Spaces

- [CGColorSpaceCreateCalibratedGray](<init(calibratedgraywhitepoint_blackpoint_gamma_).md>) — Creates a calibrated grayscale color space.
- [CGColorSpaceCreateCalibratedRGB](<init(calibratedrgbwhitepoint_blackpoint_gamma_matrix_).md>) — Creates a calibrated RGB color space.
- [CGColorSpaceCreateICCBased](<init(iccbasedncomponents_range_profile_alternate_).md>) — Creates a device-independent color space that is defined according to the ICC color profile specification.
- [CGColorSpaceCreateIndexed](<init(indexedbasespace_last_colortable_).md>) — Creates an indexed color space, consisting of colors specified by a color lookup table.
- [CGColorSpaceCreateLab](<init(labwhitepoint_blackpoint_range_).md>) — Creates a device-independent color space that is relative to human color perception, according to the CIE L*a*b* standard.
- [CGColorSpaceCreatePattern](<init(patternbasespace_).md>) — Creates a pattern color space.
- [CGColorSpaceCreateWithName](<init(name_).md>) — Creates a specified type of Quartz color space.
- [CGColorSpaceCreateWithICCData](<init(iccdata_).md>) — Creates an ICC-based color space using the ICC profile contained in the specified data.
- [CGColorSpaceCreateWithPropertyList](<init(propertylistplist_).md>) — Creates a color space from a property list.
- [CGColorSpaceCreateDeviceRGB](<../cgcolorspacecreatedevicergb().md>) — Creates a device-dependent RGB color space.
- [CGColorSpaceCreateDeviceCMYK](<../cgcolorspacecreatedevicecmyk().md>) — Creates a device-dependent CMYK color space.
- [CGColorSpaceCreateDeviceGray](<../cgcolorspacecreatedevicegray().md>) — Creates a device-dependent grayscale color space.
- [CGColorSpaceCreateWithICCProfile](<init(iccprofiledata_).md>) — Creates an ICC-based color space using the ICC profile contained in the specified data. _(deprecated)_

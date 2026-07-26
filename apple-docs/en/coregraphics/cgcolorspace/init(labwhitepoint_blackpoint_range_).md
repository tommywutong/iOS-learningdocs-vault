---
title: 'init(labWhitePoint:blackPoint:range:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcolorspace/init(labwhitepoint:blackpoint:range:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorspace/init(labwhitepoint:blackpoint:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorspace/init%28labwhitepoint%3Ablackpoint%3Arange%3A%29.json'
content_hash: 'sha256:f26d5865edcd6fdd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColorSpace](../cgcolorspace.md)

# init(labWhitePoint:blackPoint:range:)

<sub>Initializer</sub>

Creates a device-independent color space that is relative to human color perception, according to the CIE L*a*b* standard.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(labWhitePoint whitePoint: UnsafePointer<CGFloat>, blackPoint: UnsafePointer<CGFloat>?, range: UnsafePointer<CGFloat>?)
```

## Parameters

- `whitePoint` — An array of 3 numbers that specify the tristimulus value, in the CIE 1931 XYZ-space, of the diffuse white point.

- `blackPoint` — An array of 3 numbers that specify the tristimulus value, in CIE 1931 XYZ-space, of the diffuse black point.

- `range` — An array of 4 numbers that specify the range of valid values for the a* and b* components of the color space. The a* component represents values running from green to red, and the b* component represents values running from blue to yellow.

## Return Value

A new L*a*b* color space, or `NULL` if unsuccessful. In Objective-C, you’re responsible for releasing this object by calling [CGColorSpaceRelease](../cgcolorspacerelease.md).

## Discussion

The CIE L*a*b* space is a nonlinear transformation of the Munsell color notation system (a system which specifies colors by hue, value, and saturation—or “chroma”—values), designed to match perceived color difference with quantitative distance in color space. The L* component represents the lightness value, the a* component represents values running from green to red, and the b* component represents values running from blue to yellow. This roughly corresponds to the way the human brain is thought to decode colors. Colors in a device-independent color space should appear the same when displayed on different devices, to the extent that the capabilities of the device allow.

## See Also

### Creating Color Spaces

- [CGColorSpaceCreateCalibratedGray](<init(calibratedgraywhitepoint_blackpoint_gamma_).md>) — Creates a calibrated grayscale color space.
- [CGColorSpaceCreateCalibratedRGB](<init(calibratedrgbwhitepoint_blackpoint_gamma_matrix_).md>) — Creates a calibrated RGB color space.
- [CGColorSpaceCreateICCBased](<init(iccbasedncomponents_range_profile_alternate_).md>) — Creates a device-independent color space that is defined according to the ICC color profile specification.
- [CGColorSpaceCreateIndexed](<init(indexedbasespace_last_colortable_).md>) — Creates an indexed color space, consisting of colors specified by a color lookup table.
- [CGColorSpaceCreatePattern](<init(patternbasespace_).md>) — Creates a pattern color space.
- [CGColorSpaceCreateWithName](<init(name_).md>) — Creates a specified type of Quartz color space.
- [CGColorSpaceCreateWithPlatformColorSpace](<init(platformcolorspaceref_).md>) — Creates a platform-specific color space. _(deprecated)_
- [CGColorSpaceCreateWithICCData](<init(iccdata_).md>) — Creates an ICC-based color space using the ICC profile contained in the specified data.
- [CGColorSpaceCreateWithPropertyList](<init(propertylistplist_).md>) — Creates a color space from a property list.
- [CGColorSpaceCreateDeviceRGB](<../cgcolorspacecreatedevicergb().md>) — Creates a device-dependent RGB color space.
- [CGColorSpaceCreateDeviceCMYK](<../cgcolorspacecreatedevicecmyk().md>) — Creates a device-dependent CMYK color space.
- [CGColorSpaceCreateDeviceGray](<../cgcolorspacecreatedevicegray().md>) — Creates a device-dependent grayscale color space.
- [CGColorSpaceCreateWithICCProfile](<init(iccprofiledata_).md>) — Creates an ICC-based color space using the ICC profile contained in the specified data. _(deprecated)_

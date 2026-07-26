---
title: 'hdr10(minLuminance:maxLuminance:opticalOutputScale:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 10.15+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/caedrmetadata/hdr10(minluminance:maxluminance:opticaloutputscale:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/caedrmetadata/hdr10(minluminance:maxluminance:opticaloutputscale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caedrmetadata/hdr10%28minluminance%3Amaxluminance%3Aopticaloutputscale%3A%29.json'
content_hash: 'sha256:a34c7bd7c81dfc07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEDRMetadata](../caedrmetadata.md)

# hdr10(minLuminance:maxLuminance:opticalOutputScale:)

<sub>Type Method</sub>

Creates EDR metadata for HDR10 content based on the luminance characteristics of a mastering display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class func hdr10(minLuminance minNits: Float, maxLuminance maxNits: Float, opticalOutputScale scale: Float) -> CAEDRMetadata
```

## Parameters

- `minNits` — The minimum nits (cd/m^2) of the mastering display.

- `maxNits` — The maximum nits (cd/m^2) of the mastering display.

- `scale` — A scale factor relating (display-referred linear) extended range buffer values to the optical output of a reference display.

## Return Value

A new EDR metadata object.

## Discussion

Any content greater than the maximum luminance (`maxNits`) may be clamped when displayed.

The values in the drawable’s texture are assumed to be proportional to the optical output (in cd/m^2) of the reference display. For example, if the optical output scale is 100, then a value of 1.0 is assumed to be 100 nits.

If the content is in a normalized pixel format, set `opticalOutputScale` to 10000.

## See Also

### Retrieving HDR10 Metadata

- [+ HDR10MetadataWithDisplayInfo:contentInfo:opticalOutputScale:](<hdr10(displayinfo_contentinfo_opticaloutputscale_).md>) — Creates EDR metadata for HDR10 content based on mastering display color information and content light levels.

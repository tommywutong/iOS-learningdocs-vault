---
title: hdrGainMapAsRGB
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimagerepresentationoption/hdrgainmapasrgb
source_url: 'https://developer.apple.com/documentation/coreimage/ciimagerepresentationoption/hdrgainmapasrgb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimagerepresentationoption/hdrgainmapasrgb.json'
content_hash: 'sha256:0f743b49ab60518d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageRepresentationOption](../ciimagerepresentationoption.md)

# hdrGainMapAsRGB

<sub>Type Property</sub>

An optional key and value to request the gain map channel to be color instead of monochrome.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let hdrGainMapAsRGB: CIImageRepresentationOption
```

## Discussion

This key affects how the gain map image is calculated from the SDR receiver and the [kCIImageRepresentationHDRImage](hdrimage.md) image value.

The value for this is a Boolean where:

- True: the gain map is created as a color ratio between the HDR and SDR images.
- False: the gain map is created as a brightness ratio between the HDR and SDR images.
- Not specified: the default behavior False.

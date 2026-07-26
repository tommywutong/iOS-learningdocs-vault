---
title: hdrGainMapImage
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.1+, iPadOS 14.1+, Mac Catalyst 14.1+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimagerepresentationoption/hdrgainmapimage
source_url: 'https://developer.apple.com/documentation/coreimage/ciimagerepresentationoption/hdrgainmapimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimagerepresentationoption/hdrgainmapimage.json'
content_hash: 'sha256:5b2c35eb607f2f6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageRepresentationOption](../ciimagerepresentationoption.md)

# hdrGainMapImage

<sub>Type Property</sub>

An optional key and value to save a gain map channel to a JPEG or HEIF.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let hdrGainMapImage: CIImageRepresentationOption
```

## Discussion

The value for this key needs to be a monochrome [CIImage](../ciimage.md) instance.

If the [kCIImageRepresentationHDRGainMapAsRGB](hdrgainmapasrgb.md) option it true, then it needs to be an RGB [CIImage](../ciimage.md) instance.

The `/CIImage/properties` should contain metadata information equivalent to what is returned when initializing an image using [kCIImageAuxiliaryHDRGainMap](../ciimageoption/auxiliaryhdrgainmap.md).

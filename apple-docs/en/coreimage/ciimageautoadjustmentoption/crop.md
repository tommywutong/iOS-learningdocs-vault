---
title: crop
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageautoadjustmentoption/crop
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageautoadjustmentoption/crop'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageautoadjustmentoption/crop.json'
content_hash: 'sha256:5585869c15b9c46c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageAutoAdjustmentOption](../ciimageautoadjustmentoption.md)

# crop

<sub>Type Property</sub>

A key used to specify whether to return a filter that crops the image to focus on detected features.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let crop: CIImageAutoAdjustmentOption
```

## Discussion

The value associated with this key is a `CFBoolean` value. If `true`, the returned filters include an operation that crops the image around the features specified with the [kCIImageAutoAdjustFeatures](features.md) option (or any features detected in the image, if that option is not present). Supply `false` to indicate not to return a crop filter. If you don’t specify this option, Core Image assumes its value is `false`.

## See Also

### Type Properties

- [kCIImageAutoAdjustEnhance](enhance.md) — A key used to specify whether to return enhancement filters.
- [kCIImageAutoAdjustFeatures](features.md) — A key used to specify an array of features that you want to apply enhancement and red eye filters to.
- [kCIImageAutoAdjustLevel](level.md) — A key used to specify whether to return a filter that rotates the image to keep a level perspective.
- [kCIImageAutoAdjustRedEye](redeye.md) — A key used to specify whether to return a red eye filter.

---
title: enhance
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageautoadjustmentoption/enhance
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageautoadjustmentoption/enhance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageautoadjustmentoption/enhance.json'
content_hash: 'sha256:a2ccabcf1342618d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageAutoAdjustmentOption](../ciimageautoadjustmentoption.md)

# enhance

<sub>Type Property</sub>

A key used to specify whether to return enhancement filters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let enhance: CIImageAutoAdjustmentOption
```

## Discussion

The value associated with this key is a `CFBoolean` value. Supply `false` to indicate not to return enhancement filters. If you don’t specify this option, Core Image assumes its value is `true`.

## See Also

### Type Properties

- [kCIImageAutoAdjustCrop](crop.md) — A key used to specify whether to return a filter that crops the image to focus on detected features.
- [kCIImageAutoAdjustFeatures](features.md) — A key used to specify an array of features that you want to apply enhancement and red eye filters to.
- [kCIImageAutoAdjustLevel](level.md) — A key used to specify whether to return a filter that rotates the image to keep a level perspective.
- [kCIImageAutoAdjustRedEye](redeye.md) — A key used to specify whether to return a red eye filter.

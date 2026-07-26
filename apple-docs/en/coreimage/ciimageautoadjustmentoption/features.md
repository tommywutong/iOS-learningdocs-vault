---
title: features
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageautoadjustmentoption/features
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageautoadjustmentoption/features'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageautoadjustmentoption/features.json'
content_hash: 'sha256:a30d26b0903e27bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageAutoAdjustmentOption](../ciimageautoadjustmentoption.md)

# features

<sub>Type Property</sub>

A key used to specify an array of features that you want to apply enhancement and red eye filters to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let features: CIImageAutoAdjustmentOption
```

## Discussion

The associated value is an array of `CIFeature` objects. If you don’t supply an array, the Core Image searches for features using the `CIDetector` class.

## See Also

### Type Properties

- [kCIImageAutoAdjustCrop](crop.md) — A key used to specify whether to return a filter that crops the image to focus on detected features.
- [kCIImageAutoAdjustEnhance](enhance.md) — A key used to specify whether to return enhancement filters.
- [kCIImageAutoAdjustLevel](level.md) — A key used to specify whether to return a filter that rotates the image to keep a level perspective.
- [kCIImageAutoAdjustRedEye](redeye.md) — A key used to specify whether to return a red eye filter.

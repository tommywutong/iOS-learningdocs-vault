---
title: level
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageautoadjustmentoption/level
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageautoadjustmentoption/level'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageautoadjustmentoption/level.json'
content_hash: 'sha256:0117d8ee76b0af12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageAutoAdjustmentOption](../ciimageautoadjustmentoption.md)

# level

<sub>Type Property</sub>

A key used to specify whether to return a filter that rotates the image to keep a level perspective.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let level: CIImageAutoAdjustmentOption
```

## Discussion

The value associated with this key is a `CFBoolean` value. If `true`, Core Image analyzes the image to determine whether it would benefit from rotation—for example, a landscape photo in which the horizon is not horizontal—and returns a filter to perform that rotation. Supply `false` to indicate not to return a rotation filter. If you don’t specify this option, Core Image assumes its value is `false`.

## See Also

### Type Properties

- [kCIImageAutoAdjustCrop](crop.md) — A key used to specify whether to return a filter that crops the image to focus on detected features.
- [kCIImageAutoAdjustEnhance](enhance.md) — A key used to specify whether to return enhancement filters.
- [kCIImageAutoAdjustFeatures](features.md) — A key used to specify an array of features that you want to apply enhancement and red eye filters to.
- [kCIImageAutoAdjustRedEye](redeye.md) — A key used to specify whether to return a red eye filter.

---
title: constrainedHigh
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cidynamicrangeoption/constrainedhigh
source_url: 'https://developer.apple.com/documentation/coreimage/cidynamicrangeoption/constrainedhigh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidynamicrangeoption/constrainedhigh.json'
content_hash: 'sha256:147386cb8622055f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIDynamicRangeOption](../cidynamicrangeoption.md)

# constrainedHigh

<sub>Type Property</sub>

Use extended dynamic range, but brightness is modulated to optimize for co-existence with other composited content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let constrainedHigh: CIDynamicRangeOption
```

## Discussion

For best results, images should contain `contentAverageLightLevel` metadata.

## See Also

### Enumeration Cases

- [kCIDynamicRangeStandard](standard.md) — Use Standard dynamic range.
- [kCIDynamicRangeHigh](high.md) — Use High dynamic range.

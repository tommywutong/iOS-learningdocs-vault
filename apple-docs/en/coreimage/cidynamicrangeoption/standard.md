---
title: standard
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cidynamicrangeoption/standard
source_url: 'https://developer.apple.com/documentation/coreimage/cidynamicrangeoption/standard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidynamicrangeoption/standard.json'
content_hash: 'sha256:58bd4020ae1f1f88'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIDynamicRangeOption](../cidynamicrangeoption.md)

# standard

<sub>Type Property</sub>

Use Standard dynamic range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let standard: CIDynamicRangeOption
```

## Discussion

Images with `contentHeadroom` metadata will be tone mapped to a maximum pixel value of 1.0.

## See Also

### Enumeration Cases

- [kCIDynamicRangeConstrainedHigh](constrainedhigh.md) — Use extended dynamic range, but brightness is modulated to optimize for co-existence with other composited content.
- [kCIDynamicRangeHigh](high.md) — Use High dynamic range.

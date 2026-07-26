---
title: high
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cidynamicrangeoption/high
source_url: 'https://developer.apple.com/documentation/coreimage/cidynamicrangeoption/high'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidynamicrangeoption/high.json'
content_hash: 'sha256:87719bdb7c02f858'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIDynamicRangeOption](../cidynamicrangeoption.md)

# high

<sub>Type Property</sub>

Use High dynamic range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let high: CIDynamicRangeOption
```

## Discussion

The provides the best HDR quality and needs to be reserved for situations where the user is focused on the media, such as larger views in an image editing/viewing app, or annotating/drawing with HDR colors

## See Also

### Enumeration Cases

- [kCIDynamicRangeStandard](standard.md) — Use Standard dynamic range.
- [kCIDynamicRangeConstrainedHigh](constrainedhigh.md) — Use extended dynamic range, but brightness is modulated to optimize for co-existence with other composited content.

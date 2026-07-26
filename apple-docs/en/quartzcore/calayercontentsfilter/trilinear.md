---
title: trilinear
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayercontentsfilter/trilinear
source_url: 'https://developer.apple.com/documentation/quartzcore/calayercontentsfilter/trilinear'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayercontentsfilter/trilinear.json'
content_hash: 'sha256:fb513c4e2503b444'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayerContentsFilter](../calayercontentsfilter.md)

# trilinear

<sub>Type Property</sub>

Trilinear minification filter. Enables mipmap generation. Some renderers may ignore this, or impose additional restrictions, such as source images requiring power-of-two dimensions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let trilinear: CALayerContentsFilter
```

## See Also

### Constants

- [kCAFilterLinear](linear.md) — Linear interpolation filter.
- [kCAFilterNearest](nearest.md) — Nearest neighbor interpolation filter.

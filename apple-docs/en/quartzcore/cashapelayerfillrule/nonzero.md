---
title: nonZero
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cashapelayerfillrule/nonzero
source_url: 'https://developer.apple.com/documentation/quartzcore/cashapelayerfillrule/nonzero'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cashapelayerfillrule/nonzero.json'
content_hash: 'sha256:2ccb180616c785b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAShapeLayerFillRule](../cashapelayerfillrule.md)

# nonZero

<sub>Type Property</sub>

Specifies the non-zero winding rule. Count each left-to-right path as +1 and each right-to-left path as -1. If the sum of all crossings is 0, the point is outside the path. If the sum is nonzero, the point is inside the path and the region containing it is filled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let nonZero: CAShapeLayerFillRule
```

## See Also

### Constants

- [kCAFillRuleEvenOdd](evenodd.md) — Specifies the even-odd winding rule. Count the total number of path crossings. If the number of crossings is even, the point is outside the path. If the number of crossings is odd, the point is inside the path and the region containing it should be filled.

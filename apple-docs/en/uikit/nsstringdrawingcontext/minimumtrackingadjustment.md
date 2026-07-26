---
title: minimumTrackingAdjustment
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/nsstringdrawingcontext/minimumtrackingadjustment
source_url: 'https://developer.apple.com/documentation/uikit/nsstringdrawingcontext/minimumtrackingadjustment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsstringdrawingcontext/minimumtrackingadjustment.json'
content_hash: 'sha256:6f80470d2627e13a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSStringDrawingContext](../nsstringdrawingcontext.md)

# minimumTrackingAdjustment

<sub>Instance Property</sub>

The smallest amount of space, in points, to maintain between characters.

<sub>watchOS</sub>

```swift
var minimumTrackingAdjustment: CGFloat { get set }
```

## Discussion

Changing the value of this property tells the renderer that it can change the tracking to a value no smaller than the indicated amount. For example, a value of `-0.5` indicates that characters can be tracked closer together by up to half a point. A value of 0 indicates that the standard spacing is used. A typical range of values for this property would be `-0.5` to `0.0`. The default value of this property is `0.0`.

## See Also

### Deprecated

- [actualTrackingAdjustment](actualtrackingadjustment.md) — The actual tracking value that the system applied during drawing. _(deprecated)_

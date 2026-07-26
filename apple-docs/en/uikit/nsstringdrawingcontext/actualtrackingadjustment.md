---
title: actualTrackingAdjustment
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/nsstringdrawingcontext/actualtrackingadjustment
source_url: 'https://developer.apple.com/documentation/uikit/nsstringdrawingcontext/actualtrackingadjustment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsstringdrawingcontext/actualtrackingadjustment.json'
content_hash: 'sha256:dbcd449eb05e133c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSStringDrawingContext](../nsstringdrawingcontext.md)

# actualTrackingAdjustment

<sub>Instance Property</sub>

The actual tracking value that the system applied during drawing.

<sub>watchOS</sub>

```swift
var actualTrackingAdjustment: CGFloat { get }
```

## Discussion

If you specified a custom value in the [minimumTrackingAdjustment](minimumtrackingadjustment.md) property, when drawing is complete, this property contains the actual tracking value that was used.

## See Also

### Deprecated

- [minimumTrackingAdjustment](minimumtrackingadjustment.md) — The smallest amount of space, in points, to maintain between characters. _(deprecated)_

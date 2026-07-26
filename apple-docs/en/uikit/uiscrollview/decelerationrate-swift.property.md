---
title: decelerationRate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/decelerationrate-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/decelerationrate-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/decelerationrate-swift.property.json'
content_hash: 'sha256:b7337d35ba3802dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# decelerationRate

<sub>Instance Property</sub>

A floating-point value that determines the rate of deceleration after the user lifts their finger.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var decelerationRate: UIScrollView.DecelerationRate { get set }
```

## Discussion

The default rate is [UIScrollViewDecelerationRateNormal](decelerationrate-swift.struct/normal.md). For possible deceleration rates, see [DecelerationRate](decelerationrate-swift.struct.md).

## See Also

### Managing the scrolling state

- [tracking](istracking.md) — A Boolean value that indicates whether the user has touched the content to initiate scrolling.
- [dragging](isdragging.md) — A Boolean value that indicates whether the user has begun scrolling the content.
- [decelerating](isdecelerating.md) — A Boolean value that indicates whether the content is moving in the scroll view after the user lifted their finger.
- [scrollAnimating](isscrollanimating.md) — A Boolean value that indicates whether the scroll view is currently animating a scroll update.
- [- stopScrollingAndZooming](<stopscrollingandzooming().md>) — Stops active scroll and zoom animations.
- [DecelerationRate](decelerationrate-swift.struct.md) — Deceleration rates for the scroll view.

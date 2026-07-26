---
title: isDragging
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/isdragging
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/isdragging'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/isdragging.json'
content_hash: 'sha256:c5b940fe659899eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# isDragging

<sub>Instance Property</sub>

A Boolean value that indicates whether the user has begun scrolling the content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isDragging: Bool { get }
```

## Discussion

The value held by this property might require some time or distance of scrolling before it returns [true](../../swift/true.md).

## See Also

### Managing the scrolling state

- [tracking](istracking.md) — A Boolean value that indicates whether the user has touched the content to initiate scrolling.
- [decelerating](isdecelerating.md) — A Boolean value that indicates whether the content is moving in the scroll view after the user lifted their finger.
- [scrollAnimating](isscrollanimating.md) — A Boolean value that indicates whether the scroll view is currently animating a scroll update.
- [- stopScrollingAndZooming](<stopscrollingandzooming().md>) — Stops active scroll and zoom animations.
- [decelerationRate](decelerationrate-swift.property.md) — A floating-point value that determines the rate of deceleration after the user lifts their finger.
- [DecelerationRate](decelerationrate-swift.struct.md) — Deceleration rates for the scroll view.

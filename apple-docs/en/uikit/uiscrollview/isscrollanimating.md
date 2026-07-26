---
title: isScrollAnimating
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, tvOS 17.4+, visionOS 1.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/isscrollanimating
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/isscrollanimating'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/isscrollanimating.json'
content_hash: 'sha256:6da5fe527d487b94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# isScrollAnimating

<sub>Instance Property</sub>

A Boolean value that indicates whether the scroll view is currently animating a scroll update.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isScrollAnimating: Bool { get }
```

## Discussion

Call [- stopScrollingAndZooming](<stopscrollingandzooming().md>) to stop the animation.

## See Also

### Managing the scrolling state

- [tracking](istracking.md) — A Boolean value that indicates whether the user has touched the content to initiate scrolling.
- [dragging](isdragging.md) — A Boolean value that indicates whether the user has begun scrolling the content.
- [decelerating](isdecelerating.md) — A Boolean value that indicates whether the content is moving in the scroll view after the user lifted their finger.
- [- stopScrollingAndZooming](<stopscrollingandzooming().md>) — Stops active scroll and zoom animations.
- [decelerationRate](decelerationrate-swift.property.md) — A floating-point value that determines the rate of deceleration after the user lifts their finger.
- [DecelerationRate](decelerationrate-swift.struct.md) — Deceleration rates for the scroll view.

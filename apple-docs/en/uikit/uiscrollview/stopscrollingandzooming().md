---
title: stopScrollingAndZooming()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, tvOS 17.4+, visionOS 1.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/stopscrollingandzooming()
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/stopscrollingandzooming()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/stopscrollingandzooming%28%29.json'
content_hash: 'sha256:3a403a6cdfcbd5e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# stopScrollingAndZooming()

<sub>Instance Method</sub>

Stops active scroll and zoom animations.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func stopScrollingAndZooming()
```

## Discussion

The scroll view’s content offset remains at the value it has when you call this method, unless:

- The scroll view is bouncing, in which case the content offset returns to the edge of the document.
- The scroll view is paging its content, in which case the content offset updates to a page boundary.

## See Also

### Managing the scrolling state

- [tracking](istracking.md) — A Boolean value that indicates whether the user has touched the content to initiate scrolling.
- [dragging](isdragging.md) — A Boolean value that indicates whether the user has begun scrolling the content.
- [decelerating](isdecelerating.md) — A Boolean value that indicates whether the content is moving in the scroll view after the user lifted their finger.
- [scrollAnimating](isscrollanimating.md) — A Boolean value that indicates whether the scroll view is currently animating a scroll update.
- [decelerationRate](decelerationrate-swift.property.md) — A floating-point value that determines the rate of deceleration after the user lifts their finger.
- [DecelerationRate](decelerationrate-swift.struct.md) — Deceleration rates for the scroll view.

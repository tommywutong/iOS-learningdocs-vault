---
title: isTracking
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/istracking
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/istracking'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/istracking.json'
content_hash: 'sha256:b3e1c2e8e2c0623b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# isTracking

<sub>Instance Property</sub>

A Boolean value that indicates whether the user has touched the content to initiate scrolling.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isTracking: Bool { get }
```

## Discussion

The value of this property is [true](../../swift/true.md) if the user has touched the content view but might not have yet have started dragging it.

## See Also

### Managing the scrolling state

- [dragging](isdragging.md) — A Boolean value that indicates whether the user has begun scrolling the content.
- [decelerating](isdecelerating.md) — A Boolean value that indicates whether the content is moving in the scroll view after the user lifted their finger.
- [scrollAnimating](isscrollanimating.md) — A Boolean value that indicates whether the scroll view is currently animating a scroll update.
- [- stopScrollingAndZooming](<stopscrollingandzooming().md>) — Stops active scroll and zoom animations.
- [decelerationRate](decelerationrate-swift.property.md) — A floating-point value that determines the rate of deceleration after the user lifts their finger.
- [DecelerationRate](decelerationrate-swift.struct.md) — Deceleration rates for the scroll view.

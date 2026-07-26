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
doc_path: /documentation/uikit/uicontrol/istracking
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/istracking'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/istracking.json'
content_hash: 'sha256:d6e927cf5fada554'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# isTracking

<sub>Instance Property</sub>

A Boolean value that indicates whether the control is currently tracking touch events.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isTracking: Bool { get }
```

## Discussion

While tracking of a touch event is in progress, the control sets the value of this property to [true](../../swift/true.md). When tracking ends or is canceled for any reason, it sets this property to [false](../../swift/false.md).

## See Also

### Tracking touches and redrawing controls

- [- beginTrackingWithTouch:withEvent:](<begintracking(__with_).md>) — Notifies the control when a touch event enters the control’s bounds.
- [- continueTrackingWithTouch:withEvent:](<continuetracking(__with_).md>) — Notifies the control when a touch event for the control updates.
- [- endTrackingWithTouch:withEvent:](<endtracking(__with_).md>) — Notifies the control when a touch event associated with the control ends.
- [- cancelTrackingWithEvent:](<canceltracking(with_).md>) — Notifies the control to cancel tracking related to the specified event.
- [touchInside](istouchinside.md) — A Boolean value that indicates whether a tracked touch event is currently inside the control’s bounds.

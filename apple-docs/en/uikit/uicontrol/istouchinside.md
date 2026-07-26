---
title: isTouchInside
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontrol/istouchinside
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/istouchinside'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/istouchinside.json'
content_hash: 'sha256:6a35fce3a962fff4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# isTouchInside

<sub>Instance Property</sub>

A Boolean value that indicates whether a tracked touch event is currently inside the control’s bounds.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isTouchInside: Bool { get }
```

## Return Value

[true](../../swift/true.md) if the location of the most recent touch event is inside the control’s bounds or [false](../../swift/false.md) if it is not.

## Discussion

While tracking of a touch event is ongoing, the control updates the value of this property to indicate whether the most recent touch is still inside the control’s bounds. The control uses this information to trigger specific events. For example, touch events entering or exiting a control trigger appropriate drag events.

## See Also

### Tracking touches and redrawing controls

- [- beginTrackingWithTouch:withEvent:](<begintracking(__with_).md>) — Notifies the control when a touch event enters the control’s bounds.
- [- continueTrackingWithTouch:withEvent:](<continuetracking(__with_).md>) — Notifies the control when a touch event for the control updates.
- [- endTrackingWithTouch:withEvent:](<endtracking(__with_).md>) — Notifies the control when a touch event associated with the control ends.
- [- cancelTrackingWithEvent:](<canceltracking(with_).md>) — Notifies the control to cancel tracking related to the specified event.
- [tracking](istracking.md) — A Boolean value that indicates whether the control is currently tracking touch events.

---
title: 'endTracking(_:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontrol/endtracking(_:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/endtracking(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/endtracking%28_%3Awith%3A%29.json'
content_hash: 'sha256:758924338b4639f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# endTracking(_:with:)

<sub>Instance Method</sub>

Notifies the control when a touch event associated with the control ends.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func endTracking(_ touch: UITouch?, with event: UIEvent?)
```

## Parameters

- `touch` — The touch object containing the final touch information.

- `event` — The event object containing the touch event.

## Discussion

This method is called at the end of a sequence of touch events inside the control’s bounds. Subclasses can override this method and use it to perform any actions relevant to the completion of the touch sequence. You should also use it to perform any cleanup associated with tracking the event.

If you override this method, you must call `super` at some point in your implementation. The default implementation updates the [tracking](istracking.md) property of the control.

## See Also

### Tracking touches and redrawing controls

- [- beginTrackingWithTouch:withEvent:](<begintracking(__with_).md>) — Notifies the control when a touch event enters the control’s bounds.
- [- continueTrackingWithTouch:withEvent:](<continuetracking(__with_).md>) — Notifies the control when a touch event for the control updates.
- [- cancelTrackingWithEvent:](<canceltracking(with_).md>) — Notifies the control to cancel tracking related to the specified event.
- [tracking](istracking.md) — A Boolean value that indicates whether the control is currently tracking touch events.
- [touchInside](istouchinside.md) — A Boolean value that indicates whether a tracked touch event is currently inside the control’s bounds.

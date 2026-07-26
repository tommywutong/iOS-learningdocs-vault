---
title: 'cancelTracking(with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontrol/canceltracking(with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/canceltracking(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/canceltracking%28with%3A%29.json'
content_hash: 'sha256:6a4a77b92f509aa2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# cancelTracking(with:)

<sub>Instance Method</sub>

Notifies the control to cancel tracking related to the specified event.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func cancelTracking(with event: UIEvent?)
```

## Parameters

- `event` — An event object related to touches that occurred in the control. This parameter might be `nil`, indicating that the cancelation was caused by something other than an event, such as the view being removed from the window.

## Discussion

The control calls this method when a control-related touch event is canceled. The default implementation cancels any ongoing tracking and updates the control’s state information. Subclasses can override this method and use it to perform any actions relevant to the cancellation of the touch sequence. You should also use it to perform any cleanup associated with tracking the event.

If you override this method, you must call `super` at some point in your implementation.

## See Also

### Tracking touches and redrawing controls

- [- beginTrackingWithTouch:withEvent:](<begintracking(__with_).md>) — Notifies the control when a touch event enters the control’s bounds.
- [- continueTrackingWithTouch:withEvent:](<continuetracking(__with_).md>) — Notifies the control when a touch event for the control updates.
- [- endTrackingWithTouch:withEvent:](<endtracking(__with_).md>) — Notifies the control when a touch event associated with the control ends.
- [tracking](istracking.md) — A Boolean value that indicates whether the control is currently tracking touch events.
- [touchInside](istouchinside.md) — A Boolean value that indicates whether a tracked touch event is currently inside the control’s bounds.

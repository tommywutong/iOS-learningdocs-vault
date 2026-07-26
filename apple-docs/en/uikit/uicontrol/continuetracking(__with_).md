---
title: 'continueTracking(_:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontrol/continuetracking(_:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/continuetracking(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/continuetracking%28_%3Awith%3A%29.json'
content_hash: 'sha256:15d9c0d99a1ddee2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# continueTracking(_:with:)

<sub>Instance Method</sub>

Notifies the control when a touch event for the control updates.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func continueTracking(_ touch: UITouch, with event: UIEvent?) -> Bool
```

## Parameters

- `touch` — The touch object containing updated information.

- `event` — The event object containing the touch event.

## Return Value

[true](../../swift/true.md) if the control should continue tracking touch events or [false](../../swift/false.md) if it should stop. This value is used to update the [tracking](istracking.md) property of the control.

## Discussion

This method is called repeatedly while a touch event is being tracked inside the control’s bounds. The default implementation of this method always returns [true](../../swift/true.md). Subclasses can override this method and use it to update their state based on changes to the touch event. If you want to continue tracking the touch event, return [true](../../swift/true.md). If you want to stop tracking the touch event, return [false](../../swift/false.md).

## See Also

### Tracking touches and redrawing controls

- [- beginTrackingWithTouch:withEvent:](<begintracking(__with_).md>) — Notifies the control when a touch event enters the control’s bounds.
- [- endTrackingWithTouch:withEvent:](<endtracking(__with_).md>) — Notifies the control when a touch event associated with the control ends.
- [- cancelTrackingWithEvent:](<canceltracking(with_).md>) — Notifies the control to cancel tracking related to the specified event.
- [tracking](istracking.md) — A Boolean value that indicates whether the control is currently tracking touch events.
- [touchInside](istouchinside.md) — A Boolean value that indicates whether a tracked touch event is currently inside the control’s bounds.

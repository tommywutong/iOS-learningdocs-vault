---
title: 'ignore(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigesturerecognizer/ignore(_:for:)-5f685'
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/ignore(_:for:)-5f685'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/ignore%28_%3Afor%3A%29-5f685.json'
content_hash: 'sha256:e68676d3d87fc3d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# ignore(_:for:)

<sub>Instance Method</sub>

Tells the gesture recognizer to ignore a specific touch of the given event.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func ignore(_ touch: UITouch, for event: UIEvent)
```

## Parameters

- `touch` — A [UITouch](../uitouch.md) object that is part of the current multi-touch sequence and associated with `event`.

- `event` — A [UIEvent](../uievent.md) object that includes a reference to `touch`.

## Discussion

If a touch isn’t part of this gesture you may pass it to this method, causing it to be ignored. `UIGestureRecognizer` does not cancel ignored touches on the associated view. This method is intended to be called, not overridden.

## See Also

### Implementing subclasses

- [- touchesBegan:withEvent:](<touchesbegan(__with_).md>) — Sent to the gesture recognizer when one or more fingers touch down in the associated view.
- [- touchesMoved:withEvent:](<touchesmoved(__with_).md>) — Sent to the gesture recognizer when one or more fingers move in the associated view.
- [- touchesEnded:withEvent:](<touchesended(__with_).md>) — Sent to the gesture recognizer when one or more fingers lift from the associated view.
- [- touchesCancelled:withEvent:](<touchescancelled(__with_).md>) — Sent to the gesture recognizer when a system event (such as an incoming phone call) cancels a touch event.
- [- touchesEstimatedPropertiesUpdated:](<touchesestimatedpropertiesupdated(__).md>) — Sent to the gesture recognizer when the estimated properties for a touch have changed so that they are no longer estimated, or an update is no longer expected.
- [- reset](<reset().md>) — Overridden to reset internal state when a gesture recognition attempt completes.
- [- canBePreventedByGestureRecognizer:](<canbeprevented(by_).md>) — Overridden to indicate that the specified gesture recognizer can prevent the receiver from recognizing a gesture.
- [- canPreventGestureRecognizer:](<canprevent(__).md>) — Overridden to indicate that the receiver can prevent the specified gesture recognizer from recognizing its gesture.
- [- shouldReceiveEvent:](<shouldreceive(__).md>)
- [- shouldRequireFailureOfGestureRecognizer:](<shouldrequirefailure(of_).md>) — Overridden to indicate that the receiver requires the specified gesture recognizer to fail.
- [- shouldBeRequiredToFailByGestureRecognizer:](<shouldberequiredtofail(by_).md>) — Overridden to indicate that the receiver should be required to fail by the specified gesture recognizer.
- [- ignorePress:forEvent:](<ignore(__for_)-8qqor.md>) — Tells the gesture recognizer to ignore a specific press of the given event.
- [- pressesBegan:withEvent:](<pressesbegan(__with_).md>) — Sent to the receiver when a physical button is pressed in the associated view.
- [- pressesChanged:withEvent:](<presseschanged(__with_).md>) — Sent to the receiver when the [force](../uipress/force.md) of the press has changed in the associated view.
- [- pressesEnded:withEvent:](<pressesended(__with_).md>) — Sent to the receiver when a button is released from the associated view.

---
title: 'touchesCancelled(_:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigesturerecognizer/touchescancelled(_:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/touchescancelled(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/touchescancelled%28_%3Awith%3A%29.json'
content_hash: 'sha256:4b7ca3b0ec4b93de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# touchesCancelled(_:with:)

<sub>Instance Method</sub>

Sent to the gesture recognizer when a system event (such as an incoming phone call) cancels a touch event.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func touchesCancelled(_ touches: Set<UITouch>, with event: UIEvent)
```

## Parameters

- `touches` — A set of [UITouch](../uitouch.md) instances in the event represented by `event` that represent the touches in the [UITouchPhaseCancelled](../uitouch/phase-swift.enum/cancelled.md) phase.

- `event` — A [UIEvent](../uievent.md) object representing the event to which the touches belong.

## Discussion

This method has the same exact signature as the corresponding one declared by [UIResponder](../uiresponder.md). Through this method a gesture recognizer receives touch objects (in their [UITouchPhaseCancelled](../uitouch/phase-swift.enum/cancelled.md) phase) before the view attached to the gesture recognizer receives them. `UIGestureRecognizer` objects are not in the responder chain, yet observe touches hit-tested to their view and their view’s subviews. After observation, the delivery of touch objects to the attached view, or their disposition otherwise, is affected by the [cancelsTouchesInView](cancelstouchesinview.md), [delaysTouchesBegan](delaystouchesbegan.md), and [delaysTouchesEnded](delaystouchesended.md) properties.

Upon receiving this message, the gesture recognizer for a continuous gesture should set its state to [UIGestureRecognizerStateCancelled](state-swift.enum/cancelled.md); a gesture recognizer for a discrete gesture should set its state to [UIGestureRecognizerStateFailed](state-swift.enum/failed.md).

## See Also

### Implementing subclasses

- [- touchesBegan:withEvent:](<touchesbegan(__with_).md>) — Sent to the gesture recognizer when one or more fingers touch down in the associated view.
- [- touchesMoved:withEvent:](<touchesmoved(__with_).md>) — Sent to the gesture recognizer when one or more fingers move in the associated view.
- [- touchesEnded:withEvent:](<touchesended(__with_).md>) — Sent to the gesture recognizer when one or more fingers lift from the associated view.
- [- touchesEstimatedPropertiesUpdated:](<touchesestimatedpropertiesupdated(__).md>) — Sent to the gesture recognizer when the estimated properties for a touch have changed so that they are no longer estimated, or an update is no longer expected.
- [- reset](<reset().md>) — Overridden to reset internal state when a gesture recognition attempt completes.
- [- ignoreTouch:forEvent:](<ignore(__for_)-5f685.md>) — Tells the gesture recognizer to ignore a specific touch of the given event.
- [- canBePreventedByGestureRecognizer:](<canbeprevented(by_).md>) — Overridden to indicate that the specified gesture recognizer can prevent the receiver from recognizing a gesture.
- [- canPreventGestureRecognizer:](<canprevent(__).md>) — Overridden to indicate that the receiver can prevent the specified gesture recognizer from recognizing its gesture.
- [- shouldReceiveEvent:](<shouldreceive(__).md>)
- [- shouldRequireFailureOfGestureRecognizer:](<shouldrequirefailure(of_).md>) — Overridden to indicate that the receiver requires the specified gesture recognizer to fail.
- [- shouldBeRequiredToFailByGestureRecognizer:](<shouldberequiredtofail(by_).md>) — Overridden to indicate that the receiver should be required to fail by the specified gesture recognizer.
- [- ignorePress:forEvent:](<ignore(__for_)-8qqor.md>) — Tells the gesture recognizer to ignore a specific press of the given event.
- [- pressesBegan:withEvent:](<pressesbegan(__with_).md>) — Sent to the receiver when a physical button is pressed in the associated view.
- [- pressesChanged:withEvent:](<presseschanged(__with_).md>) — Sent to the receiver when the [force](../uipress/force.md) of the press has changed in the associated view.
- [- pressesEnded:withEvent:](<pressesended(__with_).md>) — Sent to the receiver when a button is released from the associated view.

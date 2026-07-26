---
title: 'pressesCancelled(_:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigesturerecognizer/pressescancelled(_:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/pressescancelled(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/pressescancelled%28_%3Awith%3A%29.json'
content_hash: 'sha256:65b25e20422ad53e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# pressesCancelled(_:with:)

<sub>Instance Method</sub>

Sent to the receiver when a system event (such as a low-memory warning) cancels a press event.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func pressesCancelled(_ presses: Set<UIPress>, with event: UIPressesEvent)
```

## Parameters

- `presses` — A set of [UIPress](../uipress.md) instances in the event represented by `event` that represent the touches in the [UIPressPhaseCancelled](../uipress/phase-swift.enum/cancelled.md) phase.

- `event` — A [UIEvent](../uievent.md) object that includes a reference to `press`.

## Discussion

This method has the same signature as the corresponding one declared by [UIResponder](../uiresponder.md). With this method a gesture recognizer receives press objects (in their [UIPressPhaseCancelled](../uipress/phase-swift.enum/cancelled.md) phase) before the view attached to the gesture recognizer receives them. `UIGestureRecognizer` objects are not in the responder chain, yet they observe presses hit-tested to their view and their view’s subviews.

If the gesture recognizer is interpreting a continuous gesture, it should set its state to [UIGestureRecognizerStateBegan](state-swift.enum/began.md) upon receiving this message. If at any point in its handling of the press objects the gesture recognizer determines that the press event sequence is not its gesture, it should set its state to [UIGestureRecognizerStateCancelled](state-swift.enum/cancelled.md).

## See Also

### Implementing subclasses

- [- touchesBegan:withEvent:](<touchesbegan(__with_).md>) — Sent to the gesture recognizer when one or more fingers touch down in the associated view.
- [- touchesMoved:withEvent:](<touchesmoved(__with_).md>) — Sent to the gesture recognizer when one or more fingers move in the associated view.
- [- touchesEnded:withEvent:](<touchesended(__with_).md>) — Sent to the gesture recognizer when one or more fingers lift from the associated view.
- [- touchesCancelled:withEvent:](<touchescancelled(__with_).md>) — Sent to the gesture recognizer when a system event (such as an incoming phone call) cancels a touch event.
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

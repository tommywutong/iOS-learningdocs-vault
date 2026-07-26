---
title: reset()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigesturerecognizer/reset()
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/reset()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/reset%28%29.json'
content_hash: 'sha256:9918a8d294a62094'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# reset()

<sub>Instance Method</sub>

Overridden to reset internal state when a gesture recognition attempt completes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func reset()
```

## Discussion

The runtime calls this method after the gesture-recognizer state has been set to [UIGestureRecognizerStateEnded](state-swift.enum/ended.md), [UIGestureRecognizerStateRecognized](state-swift.enum/recognized.md), [UIGestureRecognizerStateCancelled](state-swift.enum/cancelled.md), or [UIGestureRecognizerStateFailed](state-swift.enum/failed.md)—in other words, any of the terminal states for a gesture recognition attempt. Subclasses should reset any internal state in preparation for a new attempt at gesture recognition. After this method is called, the gesture recognizer receives no further updates for touches that have begun but haven’t ended.

## See Also

### Related Documentation

- [state](state-swift.property.md) — The current state of the gesture recognizer.

### Implementing subclasses

- [- touchesBegan:withEvent:](<touchesbegan(__with_).md>) — Sent to the gesture recognizer when one or more fingers touch down in the associated view.
- [- touchesMoved:withEvent:](<touchesmoved(__with_).md>) — Sent to the gesture recognizer when one or more fingers move in the associated view.
- [- touchesEnded:withEvent:](<touchesended(__with_).md>) — Sent to the gesture recognizer when one or more fingers lift from the associated view.
- [- touchesCancelled:withEvent:](<touchescancelled(__with_).md>) — Sent to the gesture recognizer when a system event (such as an incoming phone call) cancels a touch event.
- [- touchesEstimatedPropertiesUpdated:](<touchesestimatedpropertiesupdated(__).md>) — Sent to the gesture recognizer when the estimated properties for a touch have changed so that they are no longer estimated, or an update is no longer expected.
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

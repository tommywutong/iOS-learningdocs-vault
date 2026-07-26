---
title: 'canPrevent(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigesturerecognizer/canprevent(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/canprevent(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/canprevent%28_%3A%29.json'
content_hash: 'sha256:130649505fa80d8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# canPrevent(_:)

<sub>Instance Method</sub>

Overridden to indicate that the receiver can prevent the specified gesture recognizer from recognizing its gesture.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func canPrevent(_ preventedGestureRecognizer: UIGestureRecognizer) -> Bool
```

## Parameters

- `preventedGestureRecognizer` — An instance of a subclass of `UIGestureRecognizer`.

## Return Value

[true](../../swift/true.md) to indicate that the receiver can block `preventedGestureRecognizer` from recognizing its gesture, otherwise [false](../../swift/false.md).

## Discussion

Overriding these methods enables the same behavior as implementing the [UIGestureRecognizerDelegate](../uigesturerecognizerdelegate.md) methods [- gestureRecognizerShouldBegin:](<../uigesturerecognizerdelegate/gesturerecognizershouldbegin(__).md>) and [- gestureRecognizer:shouldReceiveTouch:](<../uigesturerecognizerdelegate/gesturerecognizer(__shouldreceive_)-16fuh.md>). However, by overriding them, subclasses can define class-wide prevention rules. For example, a [UITapGestureRecognizer](../uitapgesturerecognizer.md) object never prevents another `UITapGestureRecognizer` object with a higher tap count.

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
- [- shouldReceiveEvent:](<shouldreceive(__).md>)
- [- shouldRequireFailureOfGestureRecognizer:](<shouldrequirefailure(of_).md>) — Overridden to indicate that the receiver requires the specified gesture recognizer to fail.
- [- shouldBeRequiredToFailByGestureRecognizer:](<shouldberequiredtofail(by_).md>) — Overridden to indicate that the receiver should be required to fail by the specified gesture recognizer.
- [- ignorePress:forEvent:](<ignore(__for_)-8qqor.md>) — Tells the gesture recognizer to ignore a specific press of the given event.
- [- pressesBegan:withEvent:](<pressesbegan(__with_).md>) — Sent to the receiver when a physical button is pressed in the associated view.
- [- pressesChanged:withEvent:](<presseschanged(__with_).md>) — Sent to the receiver when the [force](../uipress/force.md) of the press has changed in the associated view.
- [- pressesEnded:withEvent:](<pressesended(__with_).md>) — Sent to the receiver when a button is released from the associated view.

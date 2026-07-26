---
title: 'touchesEstimatedPropertiesUpdated(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigesturerecognizer/touchesestimatedpropertiesupdated(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/touchesestimatedpropertiesupdated(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/touchesestimatedpropertiesupdated%28_%3A%29.json'
content_hash: 'sha256:f9fa5d20350765fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# touchesEstimatedPropertiesUpdated(_:)

<sub>Instance Method</sub>

Sent to the gesture recognizer when the estimated properties for a touch have changed so that they are no longer estimated, or an update is no longer expected.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func touchesEstimatedPropertiesUpdated(_ touches: Set<UITouch>)
```

## Parameters

- `touches` — The array of [UITouch](../uitouch.md) objects containing updated properties.

## Discussion

The default implementation of this method does nothing. Subclasses may override it and use it to process updates to touches.

UIKit calls this method to report updates to properties that were previously declared to be estimates through [- touchesBegan:withEvent:](<touchesbegan(__with_).md>),  [- touchesMoved:withEvent:](<touchesmoved(__with_).md>) or [- touchesEnded:withEvent:](<../uiresponder/touchesended(__with_).md>), and where declared to expect updates by having at least one property set in [estimatedPropertiesExpectingUpdates](../uitouch/estimatedpropertiesexpectingupdates.md).

Use the [estimationUpdateIndex](../uitouch/estimationupdateindex.md) property to correlate the previous state of the touch with the updated state incoming in this method. The updated values are denoted by having a cleared state in the [estimatedPropertiesExpectingUpdates](../uitouch/estimatedpropertiesexpectingupdates.md) bit mask. Although most properties end up with a cleared [estimatedProperties](../uitouch/estimatedproperties.md) flag, a property can stay in the estimated state because of hardware considerations. This behavior allows the client to decide to replace the estimate with a more domain-specific estimate, based on the other touches it receives.

## See Also

### Implementing subclasses

- [- touchesBegan:withEvent:](<touchesbegan(__with_).md>) — Sent to the gesture recognizer when one or more fingers touch down in the associated view.
- [- touchesMoved:withEvent:](<touchesmoved(__with_).md>) — Sent to the gesture recognizer when one or more fingers move in the associated view.
- [- touchesEnded:withEvent:](<touchesended(__with_).md>) — Sent to the gesture recognizer when one or more fingers lift from the associated view.
- [- touchesCancelled:withEvent:](<touchescancelled(__with_).md>) — Sent to the gesture recognizer when a system event (such as an incoming phone call) cancels a touch event.
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

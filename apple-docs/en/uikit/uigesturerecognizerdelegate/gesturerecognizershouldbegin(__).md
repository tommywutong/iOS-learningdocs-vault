---
title: 'gestureRecognizerShouldBegin(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizershouldbegin(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizershouldbegin(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizershouldbegin%28_%3A%29.json'
content_hash: 'sha256:b894ee0aaf33f9ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizerDelegate](../uigesturerecognizerdelegate.md)

# gestureRecognizerShouldBegin(_:)

<sub>Instance Method</sub>

Asks the delegate if a gesture recognizer should begin interpreting touches.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func gestureRecognizerShouldBegin(_ gestureRecognizer: UIGestureRecognizer) -> Bool
```

## Parameters

- `gestureRecognizer` — An instance of a subclass of the abstract base class [UIGestureRecognizer](../uigesturerecognizer.md). This gesture-recognizer object is about to begin processing touches to determine if its gesture is occurring.

## Return Value

[true](../../swift/true.md) (the default) to tell the gesture recognizer to proceed with interpreting touches, [false](../../swift/false.md) to prevent it from attempting to recognize its gesture.

## Discussion

This method is called when a gesture recognizer attempts to transition out of the [UIGestureRecognizerStatePossible](../uigesturerecognizer/state-swift.enum/possible.md) state. Returning [false](../../swift/false.md) causes the gesture recognizer to transition to the [UIGestureRecognizerStateFailed](../uigesturerecognizer/state-swift.enum/failed.md) state.

## See Also

### Regulating gesture recognition

- [- gestureRecognizer:shouldReceiveTouch:](<gesturerecognizer(__shouldreceive_)-16fuh.md>) — Asks the delegate if a gesture recognizer should receive an object representing a touch.
- [- gestureRecognizer:shouldReceivePress:](<gesturerecognizer(__shouldreceive_)-73vzu.md>) — Asks the delegate if a gesture recognizer should receive an object representing a press.
- [- gestureRecognizer:shouldReceiveEvent:](<gesturerecognizer(__shouldreceive_)-evxd.md>) — Asks the delegate if a gesture recognizer should receive an object representing a touch or press event.

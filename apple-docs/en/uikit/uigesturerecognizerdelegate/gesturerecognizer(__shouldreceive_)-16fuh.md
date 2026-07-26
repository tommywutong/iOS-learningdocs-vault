---
title: 'gestureRecognizer(_:shouldReceive:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-16fuh'
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-16fuh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer%28_%3Ashouldreceive%3A%29-16fuh.json'
content_hash: 'sha256:98c7026acc597651'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizerDelegate](../uigesturerecognizerdelegate.md)

# gestureRecognizer(_:shouldReceive:)

<sub>Instance Method</sub>

Asks the delegate if a gesture recognizer should receive an object representing a touch.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldReceive touch: UITouch) -> Bool
```

## Parameters

- `gestureRecognizer` — An instance of a subclass of the abstract base class [UIGestureRecognizer](../uigesturerecognizer.md).

- `touch` — A [UITouch](../uitouch.md) object from the current multi-touch sequence.

## Return Value

[true](../../swift/true.md) (the default) to allow the gesture recognizer to examine the touch object, [false](../../swift/false.md) to prevent the gesture recognizer from seeing this touch object.

## Discussion

UIKit calls this method before calling the [- touchesBegan:withEvent:](<../uigesturerecognizer/touchesbegan(__with_).md>) method of the gesture recognizer.

## See Also

### Regulating gesture recognition

- [- gestureRecognizerShouldBegin:](<gesturerecognizershouldbegin(__).md>) — Asks the delegate if a gesture recognizer should begin interpreting touches.
- [- gestureRecognizer:shouldReceivePress:](<gesturerecognizer(__shouldreceive_)-73vzu.md>) — Asks the delegate if a gesture recognizer should receive an object representing a press.
- [- gestureRecognizer:shouldReceiveEvent:](<gesturerecognizer(__shouldreceive_)-evxd.md>) — Asks the delegate if a gesture recognizer should receive an object representing a touch or press event.

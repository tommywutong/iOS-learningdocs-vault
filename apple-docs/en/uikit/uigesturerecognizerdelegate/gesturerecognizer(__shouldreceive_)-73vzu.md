---
title: 'gestureRecognizer(_:shouldReceive:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-73vzu'
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-73vzu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer%28_%3Ashouldreceive%3A%29-73vzu.json'
content_hash: 'sha256:3f78cb94e31c89b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizerDelegate](../uigesturerecognizerdelegate.md)

# gestureRecognizer(_:shouldReceive:)

<sub>Instance Method</sub>

Asks the delegate if a gesture recognizer should receive an object representing a press.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldReceive press: UIPress) -> Bool
```

## Parameters

- `gestureRecognizer` — An instance of a subclass of the abstract base class [UIGestureRecognizer](../uigesturerecognizer.md).

- `press` — A [UIPress](../uipress.md) object from the current press sequence.

## Return Value

[true](../../swift/true.md) (the default) to allow the gesture recognizer to examine the press object, or [false](../../swift/false.md) to prevent the gesture recognizer from seeing this press object.

## Discussion

UIKit calls this method before the [- pressesBegan:withEvent:](<../uigesturerecognizer/pressesbegan(__with_).md>) method of the gesture recognizer.

## See Also

### Regulating gesture recognition

- [- gestureRecognizerShouldBegin:](<gesturerecognizershouldbegin(__).md>) — Asks the delegate if a gesture recognizer should begin interpreting touches.
- [- gestureRecognizer:shouldReceiveTouch:](<gesturerecognizer(__shouldreceive_)-16fuh.md>) — Asks the delegate if a gesture recognizer should receive an object representing a touch.
- [- gestureRecognizer:shouldReceiveEvent:](<gesturerecognizer(__shouldreceive_)-evxd.md>) — Asks the delegate if a gesture recognizer should receive an object representing a touch or press event.

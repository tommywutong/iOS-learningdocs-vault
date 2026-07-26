---
title: 'gestureRecognizer(_:shouldReceive:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, tvOS 13.4+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-evxd'
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-evxd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer%28_%3Ashouldreceive%3A%29-evxd.json'
content_hash: 'sha256:ecf9758eb062ebc3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizerDelegate](../uigesturerecognizerdelegate.md)

# gestureRecognizer(_:shouldReceive:)

<sub>Instance Method</sub>

Asks the delegate if a gesture recognizer should receive an object representing a touch or press event.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldReceive event: UIEvent) -> Bool
```

## Parameters

- `gestureRecognizer` — An instance of a subclass of the abstract base class [UIGestureRecognizer](../uigesturerecognizer.md).

- `event` — A [UIEvent](../uievent.md) object from the current press or touch sequence.

## Return Value

Return [false](../../swift/false.md) to prevent the gesture recognizer from seeing this event.

## Discussion

UIKit calls this method once before either the [- gestureRecognizer:shouldReceivePress:](<gesturerecognizer(__shouldreceive_)-73vzu.md>) method or the [- gestureRecognizer:shouldReceiveTouch:](<gesturerecognizer(__shouldreceive_)-16fuh.md>) method of the gesture recognizer.

## See Also

### Regulating gesture recognition

- [- gestureRecognizerShouldBegin:](<gesturerecognizershouldbegin(__).md>) — Asks the delegate if a gesture recognizer should begin interpreting touches.
- [- gestureRecognizer:shouldReceiveTouch:](<gesturerecognizer(__shouldreceive_)-16fuh.md>) — Asks the delegate if a gesture recognizer should receive an object representing a touch.
- [- gestureRecognizer:shouldReceivePress:](<gesturerecognizer(__shouldreceive_)-73vzu.md>) — Asks the delegate if a gesture recognizer should receive an object representing a press.

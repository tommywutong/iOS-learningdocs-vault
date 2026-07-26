---
title: 'location(ofTouch:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigesturerecognizer/location(oftouch:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/location(oftouch:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/location%28oftouch%3Ain%3A%29.json'
content_hash: 'sha256:3283c0f5f9db49d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# location(ofTouch:in:)

<sub>Instance Method</sub>

Returns the location of one of the gesture’s touches in the local coordinate system of a given view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func location(ofTouch touchIndex: Int, in view: UIView?) -> CGPoint
```

## Parameters

- `touchIndex` — The index of a [UITouch](../uitouch.md) object in a private array maintained by the receiver. This touch object represents a touch of the current gesture.

- `view` — A [UIView](../uiview.md) object on which the gesture took place. Specify `nil` to indicate the window.

## Return Value

A point in the local coordinate system of `view` that identifies the location of the touch. If `nil` is specified for `view`, the method returns the touch location in the window’s base coordinate system.

## See Also

### Getting the touches and location of a gesture

- [- locationInView:](<location(in_).md>) — Returns the point computed as the location in a given view of the gesture represented by the gesture recognizer.
- [numberOfTouches](numberoftouches.md) — The number of touches involved in the gesture represented by the gesture recognizer.

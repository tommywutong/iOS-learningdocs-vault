---
title: 'location(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigesturerecognizer/location(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/location(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/location%28in%3A%29.json'
content_hash: 'sha256:08faba170dc8e7df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# location(in:)

<sub>Instance Method</sub>

Returns the point computed as the location in a given view of the gesture represented by the gesture recognizer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func location(in view: UIView?) -> CGPoint
```

## Parameters

- `view` — A [UIView](../uiview.md) object on which the gesture took place. Specify `nil` to indicate the window.

## Return Value

A point in the local coordinate system of `view` that identifies the location of the gesture. If `nil` is specified for `view`, the method returns the gesture location in the window’s base coordinate system.

## Discussion

The returned value is a generic single-point location for the gesture computed by the UIKit framework. It is usually the centroid of the touches involved in the gesture. For objects of the [UISwipeGestureRecognizer](../uiswipegesturerecognizer.md) and [UITapGestureRecognizer](../uitapgesturerecognizer.md) classes, the location returned by this method has a significance special to the gesture. This significance is documented in the reference for those classes.

## See Also

### Getting the touches and location of a gesture

- [- locationOfTouch:inView:](<location(oftouch_in_).md>) — Returns the location of one of the gesture’s touches in the local coordinate system of a given view.
- [numberOfTouches](numberoftouches.md) — The number of touches involved in the gesture represented by the gesture recognizer.

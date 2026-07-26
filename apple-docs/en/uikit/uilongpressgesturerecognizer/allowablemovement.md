---
title: allowableMovement
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilongpressgesturerecognizer/allowablemovement
source_url: 'https://developer.apple.com/documentation/uikit/uilongpressgesturerecognizer/allowablemovement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilongpressgesturerecognizer/allowablemovement.json'
content_hash: 'sha256:6214e583fad58ebb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILongPressGestureRecognizer](../uilongpressgesturerecognizer.md)

# allowableMovement

<sub>Instance Property</sub>

The maximum movement of the fingers on the view before the gesture fails.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var allowableMovement: CGFloat { get set }
```

## Discussion

The allowable distance, measured in points. The default distance is `10` points.

## See Also

### Configuring the gesture recognizer

- [minimumPressDuration](minimumpressduration.md) — The minimum time that the user must press on the view for the gesture to be recognized.
- [numberOfTouchesRequired](numberoftouchesrequired.md) — The number of fingers that must touch the view for gesture recognition.
- [numberOfTapsRequired](numberoftapsrequired.md) — The number of taps on the view necessary for gesture recognition.

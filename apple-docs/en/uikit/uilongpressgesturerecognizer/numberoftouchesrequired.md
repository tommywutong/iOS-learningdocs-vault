---
title: numberOfTouchesRequired
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilongpressgesturerecognizer/numberoftouchesrequired
source_url: 'https://developer.apple.com/documentation/uikit/uilongpressgesturerecognizer/numberoftouchesrequired'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilongpressgesturerecognizer/numberoftouchesrequired.json'
content_hash: 'sha256:98db7711156efed2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILongPressGestureRecognizer](../uilongpressgesturerecognizer.md)

# numberOfTouchesRequired

<sub>Instance Property</sub>

The number of fingers that must touch the view for gesture recognition.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var numberOfTouchesRequired: Int { get set }
```

## Discussion

The default number of fingers is `1`.

## See Also

### Configuring the gesture recognizer

- [minimumPressDuration](minimumpressduration.md) — The minimum time that the user must press on the view for the gesture to be recognized.
- [numberOfTapsRequired](numberoftapsrequired.md) — The number of taps on the view necessary for gesture recognition.
- [allowableMovement](allowablemovement.md) — The maximum movement of the fingers on the view before the gesture fails.

---
title: numberOfTapsRequired
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilongpressgesturerecognizer/numberoftapsrequired
source_url: 'https://developer.apple.com/documentation/uikit/uilongpressgesturerecognizer/numberoftapsrequired'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilongpressgesturerecognizer/numberoftapsrequired.json'
content_hash: 'sha256:ef8d49974e8828de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILongPressGestureRecognizer](../uilongpressgesturerecognizer.md)

# numberOfTapsRequired

<sub>Instance Property</sub>

The number of taps on the view necessary for gesture recognition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var numberOfTapsRequired: Int { get set }
```

## Discussion

The default number of taps is `0`.

## See Also

### Configuring the gesture recognizer

- [minimumPressDuration](minimumpressduration.md) — The minimum time that the user must press on the view for the gesture to be recognized.
- [numberOfTouchesRequired](numberoftouchesrequired.md) — The number of fingers that must touch the view for gesture recognition.
- [allowableMovement](allowablemovement.md) — The maximum movement of the fingers on the view before the gesture fails.

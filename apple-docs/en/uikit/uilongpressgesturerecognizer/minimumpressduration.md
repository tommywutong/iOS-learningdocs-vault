---
title: minimumPressDuration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilongpressgesturerecognizer/minimumpressduration
source_url: 'https://developer.apple.com/documentation/uikit/uilongpressgesturerecognizer/minimumpressduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilongpressgesturerecognizer/minimumpressduration.json'
content_hash: 'sha256:bab41bf5fa72863a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILongPressGestureRecognizer](../uilongpressgesturerecognizer.md)

# minimumPressDuration

<sub>Instance Property</sub>

The minimum time that the user must press on the view for the gesture to be recognized.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var minimumPressDuration: TimeInterval { get set }
```

## Discussion

The time interval is in seconds. The default duration is `0.5` seconds.

## See Also

### Configuring the gesture recognizer

- [numberOfTouchesRequired](numberoftouchesrequired.md) — The number of fingers that must touch the view for gesture recognition.
- [numberOfTapsRequired](numberoftapsrequired.md) — The number of taps on the view necessary for gesture recognition.
- [allowableMovement](allowablemovement.md) — The maximum movement of the fingers on the view before the gesture fails.

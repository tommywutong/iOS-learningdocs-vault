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
doc_path: /documentation/uikit/uitapgesturerecognizer/numberoftouchesrequired
source_url: 'https://developer.apple.com/documentation/uikit/uitapgesturerecognizer/numberoftouchesrequired'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitapgesturerecognizer/numberoftouchesrequired.json'
content_hash: 'sha256:53013c256f17d694'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITapGestureRecognizer](../uitapgesturerecognizer.md)

# numberOfTouchesRequired

<sub>Instance Property</sub>

The number of fingers that the user must tap for gesture recognition.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var numberOfTouchesRequired: Int { get set }
```

## Discussion

The default value is 1.

## See Also

### Configuring the gesture

- [buttonMaskRequired](buttonmaskrequired.md) — The bit mask of the buttons the user must press for gesture recognition.
- [numberOfTapsRequired](numberoftapsrequired.md) — The number of taps necessary for gesture recognition.

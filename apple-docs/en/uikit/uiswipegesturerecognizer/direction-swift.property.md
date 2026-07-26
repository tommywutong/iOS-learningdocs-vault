---
title: direction
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiswipegesturerecognizer/direction-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiswipegesturerecognizer/direction-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiswipegesturerecognizer/direction-swift.property.json'
content_hash: 'sha256:ad0503045c238e2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISwipeGestureRecognizer](../uiswipegesturerecognizer.md)

# direction

<sub>Instance Property</sub>

The permitted direction of the swipe for this gesture recognizer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var direction: UISwipeGestureRecognizer.Direction { get set }
```

## Discussion

The default direction is [UISwipeGestureRecognizerDirectionRight](direction-swift.struct/right.md). See descriptions of [Direction](direction-swift.struct.md) constants for more information.

## See Also

### Related Documentation

- [Event Handling Guide for UIKit Apps](https://developer.apple.com/library/archive/documentation/EventHandling/Conceptual/EventHandlingiPhoneOS/index.html#//apple_ref/doc/uid/TP40009541)

### Configuring the gesture

- [numberOfTouchesRequired](numberoftouchesrequired.md) — The number of touches necessary for swipe recognition.
- [Direction](direction-swift.struct.md) — The direction of the swipe.

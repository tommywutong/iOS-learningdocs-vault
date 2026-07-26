---
title: rotation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uirotationgesturerecognizer/rotation
source_url: 'https://developer.apple.com/documentation/uikit/uirotationgesturerecognizer/rotation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uirotationgesturerecognizer/rotation.json'
content_hash: 'sha256:ba98fc7d0491ceb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIRotationGestureRecognizer](../uirotationgesturerecognizer.md)

# rotation

<sub>Instance Property</sub>

The rotation of the gesture in radians.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var rotation: CGFloat { get set }
```

## Discussion

You may set the rotation value to an arbitrary value; however, setting the rotation resets the velocity.

The rotation value is a single value that varies over time. It isn’t the delta value from the last time that the rotation was reported. Apply the rotation value to the state of the view when the gesture is first recognized — don’t concatenate the value each time the handler is called.

## See Also

### Interpreting the gesture

- [velocity](velocity.md) — The velocity of the rotation gesture in radians per second.

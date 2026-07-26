---
title: scale
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipinchgesturerecognizer/scale
source_url: 'https://developer.apple.com/documentation/uikit/uipinchgesturerecognizer/scale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipinchgesturerecognizer/scale.json'
content_hash: 'sha256:2f853da064c134ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPinchGestureRecognizer](../uipinchgesturerecognizer.md)

# scale

<sub>Instance Property</sub>

The scale factor relative to the points of the two touches in screen coordinates.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var scale: CGFloat { get set }
```

## Discussion

You may set the scale factor, but doing so resets the velocity.

The scale value is an absolute value that varies over time. It isn’t the delta value from the last time that the scale was reported. Apply the scale value to the state of the view when the gesture is first recognized — don’t concatenate the value each time the handler is called.

## See Also

### Interpreting the pinching gesture

- [velocity](velocity.md) — The velocity of the pinch in scale factor per second.

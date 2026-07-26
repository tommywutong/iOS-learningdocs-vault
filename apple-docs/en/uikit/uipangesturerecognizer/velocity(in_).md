---
title: 'velocity(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipangesturerecognizer/velocity(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipangesturerecognizer/velocity(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipangesturerecognizer/velocity%28in%3A%29.json'
content_hash: 'sha256:ab31a963ebf6f432'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPanGestureRecognizer](../uipangesturerecognizer.md)

# velocity(in:)

<sub>Instance Method</sub>

Interprets the velocity of the pan gesture in the coordinate system of the specified view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func velocity(in view: UIView?) -> CGPoint
```

## Parameters

- `view` — The view in whose coordinate system the velocity of the pan gesture is computed.

## Return Value

The velocity of the pan gesture, which is expressed in points per second. The velocity is broken into horizontal and vertical components.

## See Also

### Tracking the location and velocity of the gesture

- [- translationInView:](<translation(in_).md>) — Interprets the pan gesture in the coordinate system of the specified view.
- [- setTranslation:inView:](<settranslation(__in_).md>) — Sets the translation value in the coordinate system of the specified view.

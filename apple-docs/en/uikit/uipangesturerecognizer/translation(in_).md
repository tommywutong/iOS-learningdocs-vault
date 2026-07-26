---
title: 'translation(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipangesturerecognizer/translation(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipangesturerecognizer/translation(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipangesturerecognizer/translation%28in%3A%29.json'
content_hash: 'sha256:1fa5cad6c94b9240'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPanGestureRecognizer](../uipangesturerecognizer.md)

# translation(in:)

<sub>Instance Method</sub>

Interprets the pan gesture in the coordinate system of the specified view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func translation(in view: UIView?) -> CGPoint
```

## Parameters

- `view` — The view in whose coordinate system the translation of the pan gesture should be computed. If you want to adjust a view’s location to keep it under the user’s finger, request the translation in that view’s superview’s coordinate system.

## Return Value

A point identifying the new location of a view in the coordinate system of its designated superview.

## Discussion

The x and y values report the total translation over time. They aren’t delta values from the last time that the translation was reported. Apply the translation value to the state of the view when the gesture is first recognized — don’t concatenate the value each time the handler is called.

## See Also

### Tracking the location and velocity of the gesture

- [- setTranslation:inView:](<settranslation(__in_).md>) — Sets the translation value in the coordinate system of the specified view.
- [- velocityInView:](<velocity(in_).md>) — Interprets the velocity of the pan gesture in the coordinate system of the specified view.

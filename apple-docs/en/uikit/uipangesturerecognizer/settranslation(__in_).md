---
title: 'setTranslation(_:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipangesturerecognizer/settranslation(_:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipangesturerecognizer/settranslation(_:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipangesturerecognizer/settranslation%28_%3Ain%3A%29.json'
content_hash: 'sha256:ce4eb0f80a205d0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPanGestureRecognizer](../uipangesturerecognizer.md)

# setTranslation(_:in:)

<sub>Instance Method</sub>

Sets the translation value in the coordinate system of the specified view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setTranslation(_ translation: CGPoint, in view: UIView?)
```

## Parameters

- `translation` — A point that identifies the new translation value.

- `view` — A view in whose coordinate system the translation is to occur.

## Discussion

Changing the translation value resets the velocity of the pan.

## See Also

### Tracking the location and velocity of the gesture

- [- translationInView:](<translation(in_).md>) — Interprets the pan gesture in the coordinate system of the specified view.
- [- velocityInView:](<velocity(in_).md>) — Interprets the velocity of the pan gesture in the coordinate system of the specified view.

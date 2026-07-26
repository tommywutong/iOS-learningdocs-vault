---
title: cancelsTouchesInView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigesturerecognizer/cancelstouchesinview
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/cancelstouchesinview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/cancelstouchesinview.json'
content_hash: 'sha256:a4586fd78153ed1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# cancelsTouchesInView

<sub>Instance Property</sub>

A Boolean value that determines whether touches are delivered to a view when a gesture is recognized.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var cancelsTouchesInView: Bool { get set }
```

## Discussion

When this property is [true](../../swift/true.md) (the default) and the gesture recognizer recognizes its gesture, the touches of that gesture that are pending aren’t delivered to the view and previously delivered touches are canceled through a [- touchesCancelled:withEvent:](<../uiresponder/touchescancelled(__with_).md>) message sent to the view. If a gesture recognizer doesn’t recognize its gesture or if the value of this property is [false](../../swift/false.md), the view receives all touches in the multi-touch sequence.

## See Also

### Canceling and delaying touches

- [delaysTouchesBegan](delaystouchesbegan.md) — A Boolean value that determines whether the gesture recognizer delays sending touches in a begin phase to its view.
- [delaysTouchesEnded](delaystouchesended.md) — A Boolean value that determines whether the gesture recognizer delays sending touches in an end phase to its view.

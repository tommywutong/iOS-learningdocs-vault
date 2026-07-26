---
title: delaysTouchesBegan
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigesturerecognizer/delaystouchesbegan
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/delaystouchesbegan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/delaystouchesbegan.json'
content_hash: 'sha256:a9e2033e189bb96d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# delaysTouchesBegan

<sub>Instance Property</sub>

A Boolean value that determines whether the gesture recognizer delays sending touches in a begin phase to its view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var delaysTouchesBegan: Bool { get set }
```

## Discussion

When the value of this property is [false](../../swift/false.md) (the default), views analyze touch events in [UITouchPhaseBegan](../uitouch/phase-swift.enum/began.md) and [UITouchPhaseMoved](../uitouch/phase-swift.enum/moved.md) in parallel with the gesture recognizer. When the value of the property is [true](../../swift/true.md), the window suspends delivery of touch objects in the [UITouchPhaseBegan](../uitouch/phase-swift.enum/began.md) phase to the view. If the gesture recognizer subsequently recognizes its gesture, these touch objects are discarded. If the gesture recognizer, however, doesn’t recognize its gesture, the window delivers these objects to the view in a [- touchesBegan:withEvent:](<../uiresponder/touchesbegan(__with_).md>) message (and possibly a follow-up [- touchesMoved:withEvent:](<../uiresponder/touchesmoved(__with_).md>) message to inform it of the touches’ current locations). Set this property to [true](../../swift/true.md) to prevent views from processing any touches in the [UITouchPhaseBegan](../uitouch/phase-swift.enum/began.md) phase that may be recognized as part of this gesture.

## See Also

### Canceling and delaying touches

- [cancelsTouchesInView](cancelstouchesinview.md) — A Boolean value that determines whether touches are delivered to a view when a gesture is recognized.
- [delaysTouchesEnded](delaystouchesended.md) — A Boolean value that determines whether the gesture recognizer delays sending touches in an end phase to its view.

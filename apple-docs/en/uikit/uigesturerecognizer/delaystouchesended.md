---
title: delaysTouchesEnded
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigesturerecognizer/delaystouchesended
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/delaystouchesended'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/delaystouchesended.json'
content_hash: 'sha256:c0cad0fe99122dac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# delaysTouchesEnded

<sub>Instance Property</sub>

A Boolean value that determines whether the gesture recognizer delays sending touches in an end phase to its view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var delaysTouchesEnded: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md) (the default) and the gesture recognizer is analyzing touch events, the window suspends delivery of touch objects in the [UITouchPhaseEnded](../uitouch/phase-swift.enum/ended.md) phase to the attached view. If the gesture recognizer subsequently recognizes its gesture, these touch objects are canceled (with a [- touchesCancelled:withEvent:](<../uiresponder/touchescancelled(__with_).md>) message). If the gesture recognizer doesn’t recognize its gesture, the window delivers these objects in an invocation of the view’s [- touchesEnded:withEvent:](<../uiresponder/touchesended(__with_).md>) method. Set this property to [false](../../swift/false.md) to have touch objects in the [UITouchPhaseEnded](../uitouch/phase-swift.enum/ended.md) delivered to the view while the gesture recognizer is analyzing the same touches.

## See Also

### Canceling and delaying touches

- [cancelsTouchesInView](cancelstouchesinview.md) — A Boolean value that determines whether touches are delivered to a view when a gesture is recognized.
- [delaysTouchesBegan](delaystouchesbegan.md) — A Boolean value that determines whether the gesture recognizer delays sending touches in a begin phase to its view.

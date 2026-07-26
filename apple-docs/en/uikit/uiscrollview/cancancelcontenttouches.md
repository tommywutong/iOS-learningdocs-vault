---
title: canCancelContentTouches
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/cancancelcontenttouches
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/cancancelcontenttouches'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/cancancelcontenttouches.json'
content_hash: 'sha256:ec390684ed5a50dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# canCancelContentTouches

<sub>Instance Property</sub>

A Boolean value that controls whether touches in the content view always lead to tracking.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var canCancelContentTouches: Bool { get set }
```

## Discussion

If the value of this property is [true](../../swift/true.md) and a view in the content has begun tracking a finger touching it, and if the user drags the finger enough to initiate a scroll, the view receives a [- touchesCancelled:withEvent:](<../uiresponder/touchescancelled(__with_).md>) message and the scroll view handles the touch as a scroll. If the value of this property is [false](../../swift/false.md), the scroll view doesn’t scroll regardless of finger movement once the content view starts tracking.

## See Also

### Managing touches

- [- touchesShouldBegin:withEvent:inContentView:](<touchesshouldbegin(__with_in_).md>) — Overridden by subclasses to customize the default behavior when a finger touches down in displayed content.
- [- touchesShouldCancelInContentView:](<touchesshouldcancel(in_).md>) — Returns whether to cancel touches related to the content subview and start dragging.
- [delaysContentTouches](delayscontenttouches.md) — A Boolean value that determines whether the scroll view delays the handling of touch-down gestures.
- [directionalPressGestureRecognizer](directionalpressgesturerecognizer.md) — The underlying gesture recognizer for directional button presses.

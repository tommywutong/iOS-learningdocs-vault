---
title: delaysContentTouches
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/delayscontenttouches
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/delayscontenttouches'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/delayscontenttouches.json'
content_hash: 'sha256:0a3aa1de71de9e89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# delaysContentTouches

<sub>Instance Property</sub>

A Boolean value that determines whether the scroll view delays the handling of touch-down gestures.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var delaysContentTouches: Bool { get set }
```

## Discussion

If the value of this property is [true](../../swift/true.md), the scroll view delays handling the touch-down gesture until it can determine if scrolling is the intent. If the value is [false](../../swift/false.md) , the scroll view immediately calls [- touchesShouldBegin:withEvent:inContentView:](<touchesshouldbegin(__with_in_).md>). The default value is [true](../../swift/true.md).

See the class description for a fuller discussion.

## See Also

### Managing touches

- [- touchesShouldBegin:withEvent:inContentView:](<touchesshouldbegin(__with_in_).md>) — Overridden by subclasses to customize the default behavior when a finger touches down in displayed content.
- [- touchesShouldCancelInContentView:](<touchesshouldcancel(in_).md>) — Returns whether to cancel touches related to the content subview and start dragging.
- [canCancelContentTouches](cancancelcontenttouches.md) — A Boolean value that controls whether touches in the content view always lead to tracking.
- [directionalPressGestureRecognizer](directionalpressgesturerecognizer.md) — The underlying gesture recognizer for directional button presses.

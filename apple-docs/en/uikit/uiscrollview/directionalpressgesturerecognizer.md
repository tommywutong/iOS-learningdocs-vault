---
title: directionalPressGestureRecognizer
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS 9.0+（11.0 起废弃）, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiscrollview/directionalpressgesturerecognizer
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/directionalpressgesturerecognizer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/directionalpressgesturerecognizer.json'
content_hash: 'sha256:24d26597fa4839b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# directionalPressGestureRecognizer

<sub>Instance Property</sub>

The underlying gesture recognizer for directional button presses.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var directionalPressGestureRecognizer: UIGestureRecognizer { get }
```

## Discussion

The [directionalPressGestureRecognizer](directionalpressgesturerecognizer.md) is disabled by default. If you want to perform scrolling in direct response to up, down, left, and right arrow button presses, instead of scrolling indirectly in response to focus updates, enable this gesture recognizer.

## See Also

### Managing touches

- [- touchesShouldBegin:withEvent:inContentView:](<touchesshouldbegin(__with_in_).md>) — Overridden by subclasses to customize the default behavior when a finger touches down in displayed content.
- [- touchesShouldCancelInContentView:](<touchesshouldcancel(in_).md>) — Returns whether to cancel touches related to the content subview and start dragging.
- [canCancelContentTouches](cancancelcontenttouches.md) — A Boolean value that controls whether touches in the content view always lead to tracking.
- [delaysContentTouches](delayscontenttouches.md) — A Boolean value that determines whether the scroll view delays the handling of touch-down gestures.

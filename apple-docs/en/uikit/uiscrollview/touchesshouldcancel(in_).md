---
title: 'touchesShouldCancel(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscrollview/touchesshouldcancel(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/touchesshouldcancel(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/touchesshouldcancel%28in%3A%29.json'
content_hash: 'sha256:b141b0f6866083af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# touchesShouldCancel(in:)

<sub>Instance Method</sub>

Returns whether to cancel touches related to the content subview and start dragging.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func touchesShouldCancel(in view: UIView) -> Bool
```

## Parameters

- `view` — The view object in the content that’s being touched.

## Return Value

[true](../../swift/true.md) to cancel further touch messages to `view`, [false](../../swift/false.md) to have `view` continue to receive those messages. The default returned value is [true](../../swift/true.md) if `view` is not a [UIControl](../uicontrol.md) object; otherwise, it returns [false](../../swift/false.md).

## Discussion

The scroll view calls this method just after it starts sending tracking messages to the content view. If it receives [false](../../swift/false.md) from this method, it stops dragging and forwards the touch events to the content subview. The scroll view doesn’t call this method if the value of the [canCancelContentTouches](cancancelcontenttouches.md) property is [false](../../swift/false.md).

## See Also

### Managing touches

- [- touchesShouldBegin:withEvent:inContentView:](<touchesshouldbegin(__with_in_).md>) — Overridden by subclasses to customize the default behavior when a finger touches down in displayed content.
- [canCancelContentTouches](cancancelcontenttouches.md) — A Boolean value that controls whether touches in the content view always lead to tracking.
- [delaysContentTouches](delayscontenttouches.md) — A Boolean value that determines whether the scroll view delays the handling of touch-down gestures.
- [directionalPressGestureRecognizer](directionalpressgesturerecognizer.md) — The underlying gesture recognizer for directional button presses.

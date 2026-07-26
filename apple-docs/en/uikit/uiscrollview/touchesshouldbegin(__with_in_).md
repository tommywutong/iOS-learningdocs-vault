---
title: 'touchesShouldBegin(_:with:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscrollview/touchesshouldbegin(_:with:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/touchesshouldbegin(_:with:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/touchesshouldbegin%28_%3Awith%3Ain%3A%29.json'
content_hash: 'sha256:3b9c1a18375bdc9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# touchesShouldBegin(_:with:in:)

<sub>Instance Method</sub>

Overridden by subclasses to customize the default behavior when a finger touches down in displayed content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func touchesShouldBegin(_ touches: Set<UITouch>, with event: UIEvent?, in view: UIView) -> Bool
```

## Parameters

- `touches` — A set of [UITouch](../uitouch.md) instances that represent the touches for the starting phase of the event represented by `event`.

- `event` — An object representing the event to which the touch objects in `touches` belong.

- `view` — The subview in the content where the touch-down gesture occurred.

## Return Value

Return [false](../../swift/false.md) if you don’t want the scroll view to send event messages to `view`. If you want `view` to receive those messages, return [true](../../swift/true.md) (the default).

## Discussion

The default behavior of [UIScrollView](../uiscrollview.md) is to invoke the [UIResponder](../uiresponder.md) event-handling methods of the target subview that the touches occur in.

## See Also

### Managing touches

- [- touchesShouldCancelInContentView:](<touchesshouldcancel(in_).md>) — Returns whether to cancel touches related to the content subview and start dragging.
- [canCancelContentTouches](cancancelcontenttouches.md) — A Boolean value that controls whether touches in the content view always lead to tracking.
- [delaysContentTouches](delayscontenttouches.md) — A Boolean value that determines whether the scroll view delays the handling of touch-down gestures.
- [directionalPressGestureRecognizer](directionalpressgesturerecognizer.md) — The underlying gesture recognizer for directional button presses.

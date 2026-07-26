---
title: 'gestureRecognizerShouldBegin(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/gesturerecognizershouldbegin(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/gesturerecognizershouldbegin(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/gesturerecognizershouldbegin%28_%3A%29.json'
content_hash: 'sha256:0c6e7e25a2645828'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# gestureRecognizerShouldBegin(_:)

<sub>Instance Method</sub>

Asks the view if the gesture recognizer should continue tracking touch events.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func gestureRecognizerShouldBegin(_ gestureRecognizer: UIGestureRecognizer) -> Bool
```

## Parameters

- `gestureRecognizer` — The gesture recognizer that’s attempting to transition out of the [UIGestureRecognizerStatePossible](../uigesturerecognizer/state-swift.enum/possible.md) state.

## Return Value

[true](../../swift/true.md) if the gesture recognizer should continue tracking touch events and use them to trigger a gesture or [false](../../swift/false.md) if it should transition to the [UIGestureRecognizerStateFailed](../uigesturerecognizer/state-swift.enum/failed.md) state.

## Discussion

Subclasses may override this method and use it to prevent the recognition of particular gestures. For example, the [UISlider](../uislider.md) class uses this method to prevent swipes parallel to the slider’s travel direction and that start in the thumb.

At the time this method is called, the gesture recognizer is in the [UIGestureRecognizerStatePossible](../uigesturerecognizer/state-swift.enum/possible.md) state and thinks it has the events needed to move to the [UIGestureRecognizerStateBegan](../uigesturerecognizer/state-swift.enum/began.md) state.

The default implementation of this method returns [true](../../swift/true.md).

> [!note] Note
> In iOS 17, Messages allows you to interactively resize iMessage apps with a vertical pan gesture. Messages handles any conflicts between resize gestures and your custom gestures. If your app uses manual touch handling, override those methods in your app’s [UIView](../uiview.md). You can either change your manual touch handling code to use a gesture recognizer instead, or your [UIView](../uiview.md) can override [- gestureRecognizerShouldBegin:](<../uigesturerecognizerdelegate/gesturerecognizershouldbegin(__).md>) and return NO when your iMessage app doesn’t own the gesture.

## See Also

### Managing gesture recognizers

- [- addGestureRecognizer:](<addgesturerecognizer(__).md>) — Attaches a gesture recognizer to the view.
- [- removeGestureRecognizer:](<removegesturerecognizer(__).md>) — Detaches a gesture recognizer from the receiving view.
- [gestureRecognizers](gesturerecognizers.md) — The gesture-recognizer objects currently attached to the view.

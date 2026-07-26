---
title: 'onLongPressGesture(minimumDuration:maximumDistance:inputKinds:perform:onPressingChanged:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/view/onlongpressgesture(minimumduration:maximumdistance:inputkinds:perform:onpressingchanged:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onlongpressgesture(minimumduration:maximumdistance:inputkinds:perform:onpressingchanged:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onlongpressgesture%28minimumduration%3Amaximumdistance%3Ainputkinds%3Aperform%3Aonpressingchanged%3A%29.json'
content_hash: 'sha256:307178c532ca2232'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onLongPressGesture(minimumDuration:maximumDistance:inputKinds:perform:onPressingChanged:)

<sub>Instance Method</sub>

Adds an action to perform when this view recognizes a long press gesture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated func onLongPressGesture(minimumDuration: Double = 0.5, maximumDistance: CGFloat = 10, inputKinds: GestureInputKinds = .all, perform action: @escaping () -> Void, onPressingChanged: ((Bool) -> Void)? = nil) -> some View

```

## Parameters

- `minimumDuration` — The minimum duration of the long press that must elapse before the gesture succeeds.

- `maximumDistance` — The maximum distance that the fingers or cursor performing the long press can move before the gesture fails.

- `inputKinds` — A set of input kinds that this gesture recognizes. If not specified, the gesture will recognize all applicable input kinds that a person can use to perform it.

- `action` — The action to perform when a long press is recognized.

- `onPressingChanged` — A closure to run when the pressing state of the gesture changes, passing the current state as a parameter.

## See Also

### Recognizing long-press gestures

- [onLongPressGesture(minimumDuration:maximumDistance:perform:onPressingChanged:)](<onlongpressgesture(minimumduration_maximumdistance_perform_onpressingchanged_).md>) — Adds an action to perform when this view recognizes a long press gesture.
- [onLongPressGesture(minimumDuration:perform:onPressingChanged:)](<onlongpressgesture(minimumduration_perform_onpressingchanged_).md>) — Adds an action to perform when this view recognizes a long press gesture.
- [onLongTouchGesture(minimumDuration:perform:onTouchingChanged:)](<onlongtouchgesture(minimumduration_perform_ontouchingchanged_).md>) — Adds an action to perform when this view recognizes a remote long touch gesture. A long touch gesture is when the finger is on the remote touch surface without actually pressing.
- [LongPressGesture](../longpressgesture.md) — A gesture that succeeds when the user performs a long press.

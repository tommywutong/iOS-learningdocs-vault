---
title: 'onLongPressGesture(minimumDuration:maximumDistance:perform:onPressingChanged:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/onlongpressgesture(minimumduration:maximumdistance:perform:onpressingchanged:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onlongpressgesture(minimumduration:maximumdistance:perform:onpressingchanged:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onlongpressgesture%28minimumduration%3Amaximumdistance%3Aperform%3Aonpressingchanged%3A%29.json'
content_hash: 'sha256:25b52d61947a933f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onLongPressGesture(minimumDuration:maximumDistance:perform:onPressingChanged:)

<sub>Instance Method</sub>

Adds an action to perform when this view recognizes a long press gesture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func onLongPressGesture(minimumDuration: Double = 0.5, maximumDistance: CGFloat = 10, perform action: @escaping () -> Void, onPressingChanged: ((Bool) -> Void)? = nil) -> some View

```

## Parameters

- `minimumDuration` — The minimum duration of the long press that must elapse before the gesture succeeds.

- `maximumDistance` — The maximum distance that the fingers or cursor performing the long press can move before the gesture fails.

- `action` — The action to perform when a long press is recognized.

- `onPressingChanged` — A closure to run when the pressing state of the gesture changes, passing the current state as a parameter.

## See Also

### Recognizing long-press gestures

- [onLongPressGesture(minimumDuration:maximumDistance:inputKinds:perform:onPressingChanged:)](<onlongpressgesture(minimumduration_maximumdistance_inputkinds_perform_onpressingchanged_).md>) — Adds an action to perform when this view recognizes a long press gesture. _(beta)_
- [onLongPressGesture(minimumDuration:perform:onPressingChanged:)](<onlongpressgesture(minimumduration_perform_onpressingchanged_).md>) — Adds an action to perform when this view recognizes a long press gesture.
- [onLongTouchGesture(minimumDuration:perform:onTouchingChanged:)](<onlongtouchgesture(minimumduration_perform_ontouchingchanged_).md>) — Adds an action to perform when this view recognizes a remote long touch gesture. A long touch gesture is when the finger is on the remote touch surface without actually pressing.
- [LongPressGesture](../longpressgesture.md) — A gesture that succeeds when the user performs a long press.

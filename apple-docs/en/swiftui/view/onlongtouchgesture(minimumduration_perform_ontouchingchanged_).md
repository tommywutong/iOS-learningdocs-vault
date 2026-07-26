---
title: 'onLongTouchGesture(minimumDuration:perform:onTouchingChanged:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 16.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/onlongtouchgesture(minimumduration:perform:ontouchingchanged:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onlongtouchgesture(minimumduration:perform:ontouchingchanged:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onlongtouchgesture%28minimumduration%3Aperform%3Aontouchingchanged%3A%29.json'
content_hash: 'sha256:fa35dac5a49e4084'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onLongTouchGesture(minimumDuration:perform:onTouchingChanged:)

<sub>Instance Method</sub>

Adds an action to perform when this view recognizes a remote long touch gesture. A long touch gesture is when the finger is on the remote touch surface without actually pressing.

<sub>tvOS</sub>

```swift
nonisolated func onLongTouchGesture(minimumDuration: Double = 0.5, perform action: @escaping () -> Void, onTouchingChanged: ((Bool) -> Void)? = nil) -> some View

```

## Parameters

- `minimumDuration` — The minimum duration of the long touch that must elapse before the gesture succeeds.

- `action` — The action to perform when a long touch is recognized

- `onTouchingChanged` — A closure to run when the touching state of the gesture changes, passing the current state as a parameter.

## See Also

### Recognizing long-press gestures

- [onLongPressGesture(minimumDuration:maximumDistance:perform:onPressingChanged:)](<onlongpressgesture(minimumduration_maximumdistance_perform_onpressingchanged_).md>) — Adds an action to perform when this view recognizes a long press gesture.
- [onLongPressGesture(minimumDuration:maximumDistance:inputKinds:perform:onPressingChanged:)](<onlongpressgesture(minimumduration_maximumdistance_inputkinds_perform_onpressingchanged_).md>) — Adds an action to perform when this view recognizes a long press gesture. _(beta)_
- [onLongPressGesture(minimumDuration:perform:onPressingChanged:)](<onlongpressgesture(minimumduration_perform_onpressingchanged_).md>) — Adds an action to perform when this view recognizes a long press gesture.
- [LongPressGesture](../longpressgesture.md) — A gesture that succeeds when the user performs a long press.

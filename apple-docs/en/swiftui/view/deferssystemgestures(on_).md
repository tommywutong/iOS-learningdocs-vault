---
title: 'defersSystemGestures(on:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/deferssystemgestures(on:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/deferssystemgestures(on:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/deferssystemgestures%28on%3A%29.json'
content_hash: 'sha256:a0dc0cb0aa36e80f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# defersSystemGestures(on:)

<sub>Instance Method</sub>

Sets the screen edge from which you want your gesture to take precedence over the system gesture.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
nonisolated func defersSystemGestures(on edges: Edge.Set) -> some View

```

## Parameters

- `edges` — A value that indicates the screen edge from which you want your gesture to take precedence over the system gesture.

## Discussion

The following code defers the vertical screen edges system gestures of a given canvas.

```swift
struct DeferredView: View {
    var body: some View {
        Canvas()
            .defersSystemGestures(on: .vertical)
    }
}
```

## See Also

### Defining custom gestures

- [highPriorityGesture(_:including:)](<highprioritygesture(__including_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [highPriorityGesture(_:isEnabled:)](<highprioritygesture(__isenabled_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [highPriorityGesture(_:name:isEnabled:)](<highprioritygesture(__name_isenabled_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [handGestureShortcut(_:isEnabled:)](<handgestureshortcut(__isenabled_).md>) — Assigns a hand gesture shortcut to the modified control.
- [Gesture](../gesture.md) — An instance that matches a sequence of events to a gesture, and returns a stream of values for each of its states.
- [AnyGesture](../anygesture.md) — A type-erased gesture.
- [HandActivationBehavior](../handactivationbehavior.md) — An activation behavior specific to hand-driven input.
- [HandGestureShortcut](../handgestureshortcut.md) — Hand gesture shortcuts describe finger and wrist movements that the user can perform in order to activate a button or toggle.

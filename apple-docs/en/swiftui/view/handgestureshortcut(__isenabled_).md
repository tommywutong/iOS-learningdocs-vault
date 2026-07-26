---
title: 'handGestureShortcut(_:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/handgestureshortcut(_:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/handgestureshortcut(_:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/handgestureshortcut%28_%3Aisenabled%3A%29.json'
content_hash: 'sha256:867fb6ca7bb5ba1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# handGestureShortcut(_:isEnabled:)

<sub>Instance Method</sub>

Assigns a hand gesture shortcut to the modified control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
nonisolated func handGestureShortcut(_ shortcut: HandGestureShortcut, isEnabled: Bool = true) -> some View

```

## Parameters

- `shortcut` — The shortcut to associate with this control.

- `isEnabled` — A Boolean value that indicates whether the shortcut is is enabled for this control.

## Discussion

Performing the control’s shortcut while the control is anywhere in the frontmost scene is equivalent to direct interaction with the control to perform its primary action.

The following example lets users of a watchOS music app toggle playback by double-tapping their thumb and index finger together:

```swift
struct PlaybackControls: View {
    let model: TrackModel

    var body: some View {
        HStack {
            Button("Skip Back") {
                model.skipBack()
            }

            Button("Play/Pause") {
                model.playPause()
            }
            .handGestureShortcut(.primaryAction)

            Button("Skip Forward") {
                model.skipForward()
            }
        }
    }
}
```

The target of a hand gesture shortcut is resolved in a leading-to-trailing traversal of the active scene.

## See Also

### Defining custom gestures

- [highPriorityGesture(_:including:)](<highprioritygesture(__including_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [highPriorityGesture(_:isEnabled:)](<highprioritygesture(__isenabled_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [highPriorityGesture(_:name:isEnabled:)](<highprioritygesture(__name_isenabled_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [defersSystemGestures(on:)](<deferssystemgestures(on_).md>) — Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [Gesture](../gesture.md) — An instance that matches a sequence of events to a gesture, and returns a stream of values for each of its states.
- [AnyGesture](../anygesture.md) — A type-erased gesture.
- [HandActivationBehavior](../handactivationbehavior.md) — An activation behavior specific to hand-driven input.
- [HandGestureShortcut](../handgestureshortcut.md) — Hand gesture shortcuts describe finger and wrist movements that the user can perform in order to activate a button or toggle.

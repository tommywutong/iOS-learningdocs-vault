---
title: 'sensoryFeedback(_:trigger:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 26.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/sensoryfeedback(_:trigger:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/sensoryfeedback(_:trigger:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/sensoryfeedback%28_%3Atrigger%3A%29.json'
content_hash: 'sha256:a5339ce05626d88b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# sensoryFeedback(_:trigger:)

<sub>Instance Method</sub>

Plays the specified `feedback` when the provided `trigger` value changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func sensoryFeedback<T>(_ feedback: SensoryFeedback, trigger: T) -> some View where T : Equatable

```

## Parameters

- `feedback` — Which type of feedback to play.

- `trigger` — A value to monitor for changes to determine when to play.

## Discussion

For example, you could play feedback when a state value changes:

```swift
struct MyView: View {
    @State private var showAccessory = false

    var body: some View {
        ContentView()
            .sensoryFeedback(.selection, trigger: showAccessory)
            .onLongPressGesture {
                showAccessory.toggle()
            }

        if showAccessory {
            AccessoryView()
        }
    }
}
```

## See Also

### Providing haptic feedback

- [sensoryFeedback(trigger:_:)](<sensoryfeedback(trigger___).md>) — Plays feedback when returned from the `feedback` closure after the provided `trigger` value changes.
- [sensoryFeedback(_:trigger:condition:)](<sensoryfeedback(__trigger_condition_).md>) — Plays the specified `feedback` when the provided `trigger` value changes and the `condition` closure returns `true`.
- [SensoryFeedback](../sensoryfeedback.md) — Represents a type of haptic and/or audio feedback that can be played.

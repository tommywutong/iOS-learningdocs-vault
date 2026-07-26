---
title: 'sensoryFeedback(_:trigger:condition:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 26.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/sensoryfeedback(_:trigger:condition:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/sensoryfeedback(_:trigger:condition:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/sensoryfeedback%28_%3Atrigger%3Acondition%3A%29.json'
content_hash: 'sha256:aca89a87e77814ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# sensoryFeedback(_:trigger:condition:)

<sub>Instance Method</sub>

Plays the specified `feedback` when the provided `trigger` value changes and the `condition` closure returns `true`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func sensoryFeedback<T>(_ feedback: SensoryFeedback, trigger: T, condition: @escaping (T, T) -> Bool) -> some View where T : Equatable

```

## Parameters

- `feedback` — Which type of feedback to play.

- `trigger` — A value to monitor for changes to determine when to play.

- `condition` — A closure to determine whether to play the feedback when `trigger` changes.

## Discussion

For example, you could play feedback for certain state transitions:

```swift
struct MyView: View {
    @State private var phase = Phase.inactive

    var body: some View {
        ContentView(phase: $phase)
            .sensoryFeedback(.selection, trigger: phase) { old, new in
                old == .inactive || new == .expanded
            }
    }

    enum Phase {
        case inactive
        case preparing
        case active
        case expanded
    }
}
```

When the value changes, the new version of the closure will be called, so any captured values will have their values from the time that the observed value has its new value.

## See Also

### Providing haptic feedback

- [sensoryFeedback(_:trigger:)](<sensoryfeedback(__trigger_).md>) — Plays the specified `feedback` when the provided `trigger` value changes.
- [sensoryFeedback(trigger:_:)](<sensoryfeedback(trigger___).md>) — Plays feedback when returned from the `feedback` closure after the provided `trigger` value changes.
- [SensoryFeedback](../sensoryfeedback.md) — Represents a type of haptic and/or audio feedback that can be played.

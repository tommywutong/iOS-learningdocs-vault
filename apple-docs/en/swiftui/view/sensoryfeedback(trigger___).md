---
title: 'sensoryFeedback(trigger:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 26.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/sensoryfeedback(trigger:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/sensoryfeedback(trigger:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/sensoryfeedback%28trigger%3A_%3A%29.json'
content_hash: 'sha256:1c379c170e4da584'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# sensoryFeedback(trigger:_:)

<sub>Instance Method</sub>

Plays feedback when returned from the `feedback` closure after the provided `trigger` value changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func sensoryFeedback<T>(trigger: T, _ feedback: @escaping () -> SensoryFeedback?) -> some View where T : Equatable

```

## Parameters

- `trigger` — A value to monitor for changes to determine when to play.

- `feedback` — A closure to determine whether to play the feedback and what type of feedback to play when `trigger` changes.

## Discussion

For example, you could play different feedback for different state transitions:

```swift
struct MyView: View {
    @State private var isExpanded = false

    var body: some View {
        ContentView(isExpanded: $isExpanded)
            .sensoryFeedback(trigger: isExpanded) {
                isExpanded ? .impact : nil
            }
    }
}
```

When the value changes, the new version of the closure will be called, so any captured values will have their values from the time that the observed value has its new value.

## See Also

### Providing haptic feedback

- [sensoryFeedback(_:trigger:)](<sensoryfeedback(__trigger_).md>) — Plays the specified `feedback` when the provided `trigger` value changes.
- [sensoryFeedback(_:trigger:condition:)](<sensoryfeedback(__trigger_condition_).md>) — Plays the specified `feedback` when the provided `trigger` value changes and the `condition` closure returns `true`.
- [SensoryFeedback](../sensoryfeedback.md) — Represents a type of haptic and/or audio feedback that can be played.

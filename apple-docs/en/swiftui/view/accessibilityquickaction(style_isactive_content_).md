---
title: 'accessibilityQuickAction(style:isActive:content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityquickaction(style:isactive:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityquickaction(style:isactive:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityquickaction%28style%3Aisactive%3Acontent%3A%29.json'
content_hash: 'sha256:6e02a62b51a82ef5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityQuickAction(style:isActive:content:)

<sub>Instance Method</sub>

Adds a quick action to be shown by the system when active.

<sub>watchOS</sub>

```swift
nonisolated func accessibilityQuickAction<Style, Content>(style: Style, isActive: Binding<Bool>, @ContentBuilder content: () -> Content) -> some View where Style : AccessibilityQuickActionStyle, Content : View

```

## Discussion

The following example shows how to add a quick action to pause and resume a workout, with the [prompt](../accessibilityquickactionstyle/prompt.md) style.

```swift
@State private var isPaused = false
@State private var isQuickActionActive = false

var body: some View {
    WorkoutView(isPaused: $isPaused)
        .accessibilityQuickAction(style: .prompt, isActive: $isQuickActionActive) {
            Button(isPaused ? "Resume" : "Pause") {
                isPaused.toggle()
            }
        }
}
```

The following example shows how to add a quick action to play and pause music, with the [outline](../accessibilityquickactionstyle/outline.md) style.

```swift
@State private var isPlaying = false
@State private var isQuickActionActive = false

var body: some View {
    PlayButton(isPlaying: $isPlaying)
        .contentShape(.focusEffect, Circle())
        .accessibilityQuickAction(style: .outline, isActive: $isQuickActionActive) {
            Button(isPlaying ? "Pause" : "Play") {
                isPlaying.toggle()
            }
        }
}
```

## See Also

### Offering Quick Actions to people

- [accessibilityQuickAction(style:content:)](<accessibilityquickaction(style_content_).md>) — Adds a quick action to be shown by the system when active.
- [AccessibilityQuickActionStyle](../accessibilityquickactionstyle.md) — A type that describes the presentation style of an accessibility quick action.

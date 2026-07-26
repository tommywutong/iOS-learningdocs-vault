---
title: prompt
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessibilityquickactionstyle/prompt
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilityquickactionstyle/prompt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilityquickactionstyle/prompt.json'
content_hash: 'sha256:566bc2a62a0c69dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AccessibilityQuickActionStyle](../accessibilityquickactionstyle.md)

# prompt

<sub>Type Property</sub>

A presentation style that displays a prompt to the user when the accessibility quick action is active.

<sub>watchOS</sub>

```swift
@export(implementation) static var prompt: AccessibilityQuickActionPromptStyle { get }
```

## Discussion

The following example shows how to add an [accessibilityQuickAction(style:content:)](<../view/accessibilityquickaction(style_content_).md>) to pause and resume a workout.

```swift
@State private var isPaused = false

var body: some View {
    WorkoutView(isPaused: $isPaused)
        .accessibilityQuickAction(style: .prompt) {
            Button(isPaused ? "Resume" : "Pause") {
                isPaused.toggle()
            }
        }
}
```

## See Also

### Getting built-in menu styles

- [outline](outline.md) — A presentation style that animates an outline around the view when the accessibility quick action is active.

---
title: outline
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessibilityquickactionstyle/outline
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilityquickactionstyle/outline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilityquickactionstyle/outline.json'
content_hash: 'sha256:5383df2a8a5af8c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AccessibilityQuickActionStyle](../accessibilityquickactionstyle.md)

# outline

<sub>Type Property</sub>

A presentation style that animates an outline around the view when the accessibility quick action is active.

<sub>watchOS</sub>

```swift
@export(implementation) static var outline: AccessibilityQuickActionOutlineStyle { get }
```

## Discussion

Use the [contentShape(_:_:eoFill:)](<../view/contentshape(____eofill_).md>) modifier to provide a shape for [focusEffect](../contentshapekinds/focuseffect.md) if necessary.

The following example shows how to add an [accessibilityQuickAction(style:content:)](<../view/accessibilityquickaction(style_content_).md>) to play and pause music.

```swift
@State private var isPlaying = false

var body: some View {
    PlayButton(isPlaying: $isPlaying)
        .contentShape(.focusEffect, Circle())
        .accessibilityQuickAction(style: .outline) {
            Button(isPlaying ? "Pause" : "Play") {
                isPlaying.toggle()
            }
        }
}
```

## See Also

### Getting built-in menu styles

- [prompt](prompt.md) — A presentation style that displays a prompt to the user when the accessibility quick action is active.

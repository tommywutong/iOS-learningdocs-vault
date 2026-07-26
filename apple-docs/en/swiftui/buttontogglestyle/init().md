---
title: init()
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/buttontogglestyle/init()
source_url: 'https://developer.apple.com/documentation/swiftui/buttontogglestyle/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/buttontogglestyle/init%28%29.json'
content_hash: 'sha256:cc38da68a6c35f9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ButtonToggleStyle](../buttontogglestyle.md)

# init()

<sub>Initializer</sub>

Creates a button toggle style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated init()
```

## Discussion

Don’t call this initializer directly. Instead, use the [button](../togglestyle/button.md) static variable to create this style:

```swift
Toggle(isOn: $isFlagged) {
    Label("Flag", systemImage: "flag.fill")
}
.toggleStyle(.button)
```

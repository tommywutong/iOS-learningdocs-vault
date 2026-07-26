---
title: init()
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/checkboxtogglestyle/init()
source_url: 'https://developer.apple.com/documentation/swiftui/checkboxtogglestyle/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/checkboxtogglestyle/init%28%29.json'
content_hash: 'sha256:e20869b275ecc397'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CheckboxToggleStyle](../checkboxtogglestyle.md)

# init()

<sub>Initializer</sub>

Creates a checkbox toggle style.

<sub>macOS</sub>

```swift
nonisolated init()
```

## Discussion

Don’t call this initializer directly. Instead, use the [checkbox](../togglestyle/checkbox.md) static variable to create this style:

```swift
Toggle("Close windows when quitting an app", isOn: $doesClose)
    .toggleStyle(.checkbox)
```

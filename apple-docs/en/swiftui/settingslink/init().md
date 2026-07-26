---
title: init()
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/settingslink/init()
source_url: 'https://developer.apple.com/documentation/swiftui/settingslink/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/settingslink/init%28%29.json'
content_hash: 'sha256:a997f5beb9b691ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SettingsLink](../settingslink.md)

# init()

<sub>Initializer</sub>

Creates a settings link with the default system label.

<sub>macOS</sub>

```swift
nonisolated init() where Label == DefaultSettingsLinkLabel
```

## Discussion

The display of the label may be customized using the `labelStyle(_:)` modifier.

## See Also

### Creating a settings link

- [init(label:)](<init(label_).md>) — Creates a settings link with a custom label.

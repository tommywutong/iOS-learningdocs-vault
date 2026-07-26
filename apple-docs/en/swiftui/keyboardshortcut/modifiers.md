---
title: modifiers
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/keyboardshortcut/modifiers
source_url: 'https://developer.apple.com/documentation/swiftui/keyboardshortcut/modifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/keyboardshortcut/modifiers.json'
content_hash: 'sha256:fd5d50e21dd930d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [KeyboardShortcut](../keyboardshortcut.md)

# modifiers

<sub>Instance Property</sub>

The modifier keys that the user presses in conjunction with a key equivalent to activate the shortcut.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var modifiers: EventModifiers
```

## See Also

### Creating a shortcut

- [init(_:modifiers:)](<init(__modifiers_).md>) — Creates a new keyboard shortcut with the given key equivalent and set of modifier keys.
- [key](key.md) — The key equivalent that the user presses in conjunction with any specified modifier keys to activate the shortcut.

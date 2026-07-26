---
title: 'init(_:modifiers:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/keyboardshortcut/init(_:modifiers:)'
source_url: 'https://developer.apple.com/documentation/swiftui/keyboardshortcut/init(_:modifiers:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/keyboardshortcut/init%28_%3Amodifiers%3A%29.json'
content_hash: 'sha256:f299e68858118aae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [KeyboardShortcut](../keyboardshortcut.md)

# init(_:modifiers:)

<sub>Initializer</sub>

Creates a new keyboard shortcut with the given key equivalent and set of modifier keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
init(_ key: KeyEquivalent, modifiers: EventModifiers = .command)
```

## Discussion

The localization configuration defaults to [automatic](localization-swift.struct/automatic.md).

## See Also

### Creating a shortcut

- [key](key.md) — The key equivalent that the user presses in conjunction with any specified modifier keys to activate the shortcut.
- [modifiers](modifiers.md) — The modifier keys that the user presses in conjunction with a key equivalent to activate the shortcut.

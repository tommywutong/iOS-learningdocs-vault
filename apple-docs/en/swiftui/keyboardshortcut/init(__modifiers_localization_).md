---
title: 'init(_:modifiers:localization:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/keyboardshortcut/init(_:modifiers:localization:)'
source_url: 'https://developer.apple.com/documentation/swiftui/keyboardshortcut/init(_:modifiers:localization:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/keyboardshortcut/init%28_%3Amodifiers%3Alocalization%3A%29.json'
content_hash: 'sha256:925b7d51cd6754c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [KeyboardShortcut](../keyboardshortcut.md)

# init(_:modifiers:localization:)

<sub>Initializer</sub>

Creates a new keyboard shortcut with the given key equivalent and set of modifier keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
init(_ key: KeyEquivalent, modifiers: EventModifiers = .command, localization: KeyboardShortcut.Localization)
```

## Discussion

Use the `localization` parameter to specify a localization strategy for this shortcut.

## See Also

### Creating a localized shortcut

- [localization](localization-swift.property.md) — The localization strategy to apply to this shortcut.
- [Localization](localization-swift.struct.md) — Options for how a keyboard shortcut participates in automatic localization.

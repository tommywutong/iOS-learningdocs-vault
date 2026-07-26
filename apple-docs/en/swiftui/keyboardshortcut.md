---
title: KeyboardShortcut
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/keyboardshortcut
source_url: 'https://developer.apple.com/documentation/swiftui/keyboardshortcut'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/keyboardshortcut.json'
content_hash: 'sha256:799d51a595f3366d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# KeyboardShortcut

<sub>Structure</sub>

Keyboard shortcuts describe combinations of keys on a keyboard that the user can press in order to activate a button or toggle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct KeyboardShortcut
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting standard shortcuts

- [cancelAction](keyboardshortcut/cancelaction.md) — The standard keyboard shortcut for cancelling the in-progress action or dismissing a prompt, consisting of the Escape (⎋) key and no modifiers.
- [defaultAction](keyboardshortcut/defaultaction.md) — The standard keyboard shortcut for the default button, consisting of the Return (↩) key and no modifiers.

### Creating a shortcut

- [init(_:modifiers:)](<keyboardshortcut/init(__modifiers_).md>) — Creates a new keyboard shortcut with the given key equivalent and set of modifier keys.
- [key](keyboardshortcut/key.md) — The key equivalent that the user presses in conjunction with any specified modifier keys to activate the shortcut.
- [modifiers](keyboardshortcut/modifiers.md) — The modifier keys that the user presses in conjunction with a key equivalent to activate the shortcut.

### Creating a localized shortcut

- [init(_:modifiers:localization:)](<keyboardshortcut/init(__modifiers_localization_).md>) — Creates a new keyboard shortcut with the given key equivalent and set of modifier keys.
- [localization](keyboardshortcut/localization-swift.property.md) — The localization strategy to apply to this shortcut.
- [Localization](keyboardshortcut/localization-swift.struct.md) — Options for how a keyboard shortcut participates in automatic localization.

## See Also

### Creating keyboard shortcuts

- [keyboardShortcut(_:)](<view/keyboardshortcut(__).md>) — Assigns a keyboard shortcut to the modified control.
- [keyboardShortcut(_:modifiers:)](<view/keyboardshortcut(__modifiers_).md>) — Defines a keyboard shortcut and assigns it to the modified control.
- [keyboardShortcut(_:modifiers:localization:)](<view/keyboardshortcut(__modifiers_localization_).md>) — Defines a keyboard shortcut and assigns it to the modified control.
- [keyboardShortcut](environmentvalues/keyboardshortcut.md) — The keyboard shortcut that buttons in this environment will be triggered with.
- [KeyEquivalent](keyequivalent.md) — Key equivalents consist of a letter, punctuation, or function key that can be combined with an optional set of modifier keys to specify a keyboard shortcut.
- [EventModifiers](eventmodifiers.md) — A set of key modifiers that you can add to a gesture.

---
title: 'keyboardShortcut(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/keyboardshortcut(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/keyboardshortcut(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/keyboardshortcut%28_%3A%29.json'
content_hash: 'sha256:c52bdce15ee9d4a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# keyboardShortcut(_:)

<sub>Instance Method</sub>

Assigns a keyboard shortcut to the modified control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func keyboardShortcut(_ shortcut: KeyboardShortcut) -> some View

```

## Discussion

Pressing the control’s shortcut while the control is anywhere in the frontmost window or scene, or anywhere in the macOS main menu, is equivalent to direct interaction with the control to perform its primary action.

The target of a keyboard shortcut is resolved in a leading-to-trailing traversal of one or more view hierarchies. On macOS, the system looks in the key window first, then the main window, and then the command groups; on other platforms, the system looks in the active scene, and then the command groups.

If multiple controls are associated with the same shortcut, the first one found is used.

## See Also

### Creating keyboard shortcuts

- [keyboardShortcut(_:modifiers:)](<keyboardshortcut(__modifiers_).md>) — Defines a keyboard shortcut and assigns it to the modified control.
- [keyboardShortcut(_:modifiers:localization:)](<keyboardshortcut(__modifiers_localization_).md>) — Defines a keyboard shortcut and assigns it to the modified control.
- [keyboardShortcut](../environmentvalues/keyboardshortcut.md) — The keyboard shortcut that buttons in this environment will be triggered with.
- [KeyboardShortcut](../keyboardshortcut.md) — Keyboard shortcuts describe combinations of keys on a keyboard that the user can press in order to activate a button or toggle.
- [KeyEquivalent](../keyequivalent.md) — Key equivalents consist of a letter, punctuation, or function key that can be combined with an optional set of modifier keys to specify a keyboard shortcut.
- [EventModifiers](../eventmodifiers.md) — A set of key modifiers that you can add to a gesture.

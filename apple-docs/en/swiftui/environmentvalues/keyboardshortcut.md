---
title: keyboardShortcut
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/keyboardshortcut
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/keyboardshortcut'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/keyboardshortcut.json'
content_hash: 'sha256:4fa224ea6147c0e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# keyboardShortcut

<sub>Instance Property</sub>

The keyboard shortcut that buttons in this environment will be triggered with.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var keyboardShortcut: KeyboardShortcut? { get }
```

## Discussion

This is particularly useful in button styles when a button’s appearance depends on the shortcut associated with it. On macOS, for example, when a button is bound to the Return key, it is typically drawn with a special emphasis. This happens automatically when using the built-in button styles, and can be implemented manually in custom styles using this environment key:

```swift
private struct MyButtonStyle: ButtonStyle {
    @Environment(\.keyboardShortcut)
    private var shortcut: KeyboardShortcut?

    func makeBody(configuration: Configuration) -> some View {
        let labelFont = Font.body
            .weight(shortcut == .defaultAction ? .bold : .regular)
        configuration.label
            .font(labelFont)
    }
}
```

If no keyboard shortcut has been applied to the view or its ancestor, then the environment value will be `nil`.

## See Also

### Creating keyboard shortcuts

- [keyboardShortcut(_:)](<../view/keyboardshortcut(__).md>) — Assigns a keyboard shortcut to the modified control.
- [keyboardShortcut(_:modifiers:)](<../view/keyboardshortcut(__modifiers_).md>) — Defines a keyboard shortcut and assigns it to the modified control.
- [keyboardShortcut(_:modifiers:localization:)](<../view/keyboardshortcut(__modifiers_localization_).md>) — Defines a keyboard shortcut and assigns it to the modified control.
- [KeyboardShortcut](../keyboardshortcut.md) — Keyboard shortcuts describe combinations of keys on a keyboard that the user can press in order to activate a button or toggle.
- [KeyEquivalent](../keyequivalent.md) — Key equivalents consist of a letter, punctuation, or function key that can be combined with an optional set of modifier keys to specify a keyboard shortcut.
- [EventModifiers](../eventmodifiers.md) — A set of key modifiers that you can add to a gesture.

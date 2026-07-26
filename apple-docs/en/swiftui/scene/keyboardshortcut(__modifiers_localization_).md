---
title: 'keyboardShortcut(_:modifiers:localization:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/keyboardshortcut(_:modifiers:localization:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/keyboardshortcut(_:modifiers:localization:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/keyboardshortcut%28_%3Amodifiers%3Alocalization%3A%29.json'
content_hash: 'sha256:e1d3782563069d33'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# keyboardShortcut(_:modifiers:localization:)

<sub>Instance Method</sub>

Defines a keyboard shortcut for opening new scene windows.

<sub>macOS</sub>

```swift
nonisolated func keyboardShortcut(_ key: KeyEquivalent, modifiers: EventModifiers = .command, localization: KeyboardShortcut.Localization = .automatic) -> some Scene

```

## Parameters

- `key` — The key equivalent the user presses to present the scene.

- `modifiers` — The modifier keys required to perform the shortcut.

- `localization` — The localization style to apply to the shortcut.

## Return Value

A scene that can be presented with a keyboard shortcut.

## Discussion

A scene’s keyboard shortcut is bound to the command it adds for creating new windows (in the case of `WindowGroup` and `DocumentGroup`) or bringing a singleton window forward (in the case of `Window` and, on macOS, `Settings`). Pressing the keyboard shortcut is equivalent to selecting the menu command.

In cases where a command already has a keyboard shortcut, the scene’s keyboard shortcut is used instead. For example, `WindowGroup` normally creates a File \> New Window menu command whose keyboard shortcut is `⌘N`. The following code changes it to `⌥⌘N`:

```swift
WindowGroup {
    ContentView()
}
.keyboardShortcut("n", modifiers: [.option, .command])
```

### Localization

Provide a `localization` value to specify how this shortcut should be localized.

Given that `key` is always defined in relation to the US-English keyboard layout, it might be hard to reach on different international layouts. For example the shortcut `⌘[` works well for the US layout but is hard to reach for German users, where `[` is available by pressing `⌥5`, making users type `⌥⌘5`. The automatic keyboard shortcut remapping re-assigns the shortcut to an appropriate replacement, `⌘Ö` in this case.

Providing the option [custom](../keyboardshortcut/localization-swift.struct/custom.md) disables the automatic localization for this shortcut to tell the system that internationalization is taken care of in a different way.

## See Also

### Setting commands

- [commands(content:)](<commands(content_).md>) — Adds commands to the scene.
- [commandsRemoved()](<commandsremoved().md>) — Removes all commands defined by the modified scene.
- [commandsReplaced(content:)](<commandsreplaced(content_).md>) — Replaces all commands defined by the modified scene with the commands from the builder.
- [keyboardShortcut(_:)](<keyboardshortcut(__).md>) — Defines a keyboard shortcut for opening new scene windows.

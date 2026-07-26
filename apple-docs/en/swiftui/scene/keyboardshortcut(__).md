---
title: 'keyboardShortcut(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/keyboardshortcut(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/keyboardshortcut(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/keyboardshortcut%28_%3A%29.json'
content_hash: 'sha256:8a78481769b062ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# keyboardShortcut(_:)

<sub>Instance Method</sub>

Defines a keyboard shortcut for opening new scene windows.

<sub>macOS</sub>

```swift
nonisolated func keyboardShortcut(_ shortcut: KeyboardShortcut?) -> some Scene

```

## Parameters

- `shortcut` — The keyboard shortcut for presenting the scene, or `nil`.

## Return Value

A scene that can be presented with a keyboard shortcut.

## Discussion

A scene’s keyboard shortcut is bound to the command it adds for creating new windows (in the case of `WindowGroup` and `DocumentGroup`) or bringing a singleton window forward (in the case of `Window` and, on macOS, `Settings` and `UtilityWindow`). Pressing the keyboard shortcut is equivalent to selecting the menu command.

In cases where a command already has a keyboard shortcut, the scene’s keyboard shortcut is used instead. For example, `WindowGroup` normally creates a File \> New Window menu command whose keyboard shortcut is `⌘N`. The following code changes it to something based on dynamic state:

```swift
@main
struct Notes: App {
    @State private var newWindowShortcut: KeyboardShortcut? = ...

    var body: some Scene {
        WindowGroup {
            ContentView($newWindowShortcut)
        }
        .keyboardShortcut(newWindowShortcut)
    }
}
```

If `shortcut` is `nil`, the scene’s presentation command will not be associated with a keyboard shortcut, even if SwiftUI normally assigns one automatically.

## See Also

### Setting commands

- [commands(content:)](<commands(content_).md>) — Adds commands to the scene.
- [commandsRemoved()](<commandsremoved().md>) — Removes all commands defined by the modified scene.
- [commandsReplaced(content:)](<commandsreplaced(content_).md>) — Replaces all commands defined by the modified scene with the commands from the builder.
- [keyboardShortcut(_:modifiers:localization:)](<keyboardshortcut(__modifiers_localization_).md>) — Defines a keyboard shortcut for opening new scene windows.

---
title: commandsRemoved()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scene/commandsremoved()
source_url: 'https://developer.apple.com/documentation/swiftui/scene/commandsremoved()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/commandsremoved%28%29.json'
content_hash: 'sha256:49370b2f53291648'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# commandsRemoved()

<sub>Instance Method</sub>

Removes all commands defined by the modified scene.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func commandsRemoved() -> some Scene

```

## Return Value

A scene that excludes any commands defined by its children.

## Discussion

`WindowGroup`, `Window`, and other scene types all have an associated set of commands that they include by default. Apply this modifier to a scene to exclude those commands.

For example, the following code adds a scene for presenting the details of an individual data model in a separate window. To ensure that the window can only appear programmatically, we remove the scene’s commands, including File \> New Note Window.

```swift
@main
struct Example: App {
    var body: some Scene {
        ...

        WindowGroup("Note", id: "note", for: Note.ID.self) {
            NoteDetailView(id: $0)
        }
        .commandsRemoved()
    }
}
```

## See Also

### Defining commands

- [commands(content:)](<commands(content_).md>) — Adds commands to the scene.
- [commandsReplaced(content:)](<commandsreplaced(content_).md>) — Replaces all commands defined by the modified scene with the commands from the builder.
- [Commands](../commands.md) — Conforming types represent a group of related commands that can be exposed to the user via the main menu on macOS and key commands on iOS.
- [CommandMenu](../commandmenu.md) — Command menus are stand-alone, top-level containers for controls that perform related, app-specific commands.
- [CommandGroup](../commandgroup.md) — Groups of controls that you can add to existing command menus.
- [CommandsBuilder](../commandsbuilder.md) — Constructs command sets from multi-expression closures. Like `ContentBuilder`, it supports up to ten expressions in the closure body.
- [CommandGroupPlacement](../commandgroupplacement.md) — The standard locations that you can place new command groups relative to.

---
title: 'commandsReplaced(content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/commandsreplaced(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/commandsreplaced(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/commandsreplaced%28content%3A%29.json'
content_hash: 'sha256:9d3e072383e049e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# commandsReplaced(content:)

<sub>Instance Method</sub>

Replaces all commands defined by the modified scene with the commands from the builder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func commandsReplaced<Content>(@ContentBuilder content: () -> Content) -> some Scene where Content : Commands

```

## Parameters

- `content` — A `Commands` builder whose output will be used to replace the commands normally provided by the modified scene.

## Return Value

A scene that replaces any commands defined by its children with alternative content.

## Discussion

`WindowGroup`, `Window`, and other scene types all have an associated set of commands that they include by default. Apply this modifier to a scene to replace those commands with the output from the given builder.

For example, the following code adds a scene for showing the contents of the pasteboard in a dedicated window. We replace the scene’s default Window \> Clipboard menu command with a custom Edit \> Show Clipboard command that we place next to the other pasteboard commands.

```swift
@main
struct Example: App {
    @Environment(\.openWindow) var openWindow

    var body: some Scene {
        ...

        Window("Clipboard", id: "clipboard") {
            ClipboardContentView()
        }
        .commandsReplaced {
            CommandGroup(after: .pasteboard) {
                Section {
                    Button("Show Clipboard") {
                        openWindow(id: "clipboard")
                    }
                }
            }
        }
    }
}
```

## See Also

### Defining commands

- [commands(content:)](<commands(content_).md>) — Adds commands to the scene.
- [commandsRemoved()](<commandsremoved().md>) — Removes all commands defined by the modified scene.
- [Commands](../commands.md) — Conforming types represent a group of related commands that can be exposed to the user via the main menu on macOS and key commands on iOS.
- [CommandMenu](../commandmenu.md) — Command menus are stand-alone, top-level containers for controls that perform related, app-specific commands.
- [CommandGroup](../commandgroup.md) — Groups of controls that you can add to existing command menus.
- [CommandsBuilder](../commandsbuilder.md) — Constructs command sets from multi-expression closures. Like `ContentBuilder`, it supports up to ten expressions in the closure body.
- [CommandGroupPlacement](../commandgroupplacement.md) — The standard locations that you can place new command groups relative to.

---
title: 'commands(content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/commands(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/commands(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/commands%28content%3A%29.json'
content_hash: 'sha256:76f6aee45be7be15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# commands(content:)

<sub>Instance Method</sub>

Adds commands to the scene.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func commands<Content>(@ContentBuilder content: () -> Content) -> some Scene where Content : Commands

```

## Discussion

Commands are realized in different ways on different platforms. On macOS, the main menu uses the available command menus and groups to organize its main menu items. Each menu is represented as a top-level menu bar menu, and each command group has a corresponding set of menu items in one of the top-level menus, delimited by separator menu items.

On iPadOS, commands with keyboard shortcuts are exposed in the shortcut discoverability HUD that users see when they hold down the Command (⌘) key.

## See Also

### Defining commands

- [commandsRemoved()](<commandsremoved().md>) — Removes all commands defined by the modified scene.
- [commandsReplaced(content:)](<commandsreplaced(content_).md>) — Replaces all commands defined by the modified scene with the commands from the builder.
- [Commands](../commands.md) — Conforming types represent a group of related commands that can be exposed to the user via the main menu on macOS and key commands on iOS.
- [CommandMenu](../commandmenu.md) — Command menus are stand-alone, top-level containers for controls that perform related, app-specific commands.
- [CommandGroup](../commandgroup.md) — Groups of controls that you can add to existing command menus.
- [CommandsBuilder](../commandsbuilder.md) — Constructs command sets from multi-expression closures. Like `ContentBuilder`, it supports up to ten expressions in the closure body.
- [CommandGroupPlacement](../commandgroupplacement.md) — The standard locations that you can place new command groups relative to.

---
title: CommandMenu
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/commandmenu
source_url: 'https://developer.apple.com/documentation/swiftui/commandmenu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/commandmenu.json'
content_hash: 'sha256:13a7de942f190f63'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# CommandMenu

<sub>Structure</sub>

Command menus are stand-alone, top-level containers for controls that perform related, app-specific commands.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated struct CommandMenu<Content> where Content : View
```

## Overview

Command menus are realized as menu bar menus on macOS, inserted between the built-in View and Window menus in order of declaration. On iOS, iPadOS, and tvOS, SwiftUI creates key commands for each of a menu’s commands that has a keyboard shortcut.

## Relationships

- **Conforms To**: [Commands](commands.md)

## Topics

### Creating a command menu

- [init(_:content:)](<commandmenu/init(__content_).md>) — Creates a new menu with a localized name for a collection of app- specific commands, inserted in the standard location for app menus (after the View menu, in order with other menus declared without an explicit location).

## See Also

### Defining commands

- [commands(content:)](<scene/commands(content_).md>) — Adds commands to the scene.
- [commandsRemoved()](<scene/commandsremoved().md>) — Removes all commands defined by the modified scene.
- [commandsReplaced(content:)](<scene/commandsreplaced(content_).md>) — Replaces all commands defined by the modified scene with the commands from the builder.
- [Commands](commands.md) — Conforming types represent a group of related commands that can be exposed to the user via the main menu on macOS and key commands on iOS.
- [CommandGroup](commandgroup.md) — Groups of controls that you can add to existing command menus.
- [CommandsBuilder](commandsbuilder.md) — Constructs command sets from multi-expression closures. Like `ContentBuilder`, it supports up to ten expressions in the closure body.
- [CommandGroupPlacement](commandgroupplacement.md) — The standard locations that you can place new command groups relative to.

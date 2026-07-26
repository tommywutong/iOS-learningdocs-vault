---
title: CommandGroup
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/commandgroup
source_url: 'https://developer.apple.com/documentation/swiftui/commandgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/commandgroup.json'
content_hash: 'sha256:698e7792040d4ea5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# CommandGroup

<sub>Structure</sub>

Groups of controls that you can add to existing command menus.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated struct CommandGroup<Content> where Content : View
```

## Overview

In macOS, SwiftUI realizes command groups as collections of menu items in a menu bar menu. In iOS, iPadOS, and tvOS, SwiftUI creates key commands for each of a group’s commands that has a keyboard shortcut.

## Relationships

- **Conforms To**: [Commands](commands.md)

## Topics

### Creating a command group

- [init(after:addition:)](<commandgroup/init(after_addition_).md>) — A value describing the addition of the given views to the end of the indicated group.
- [init(before:addition:)](<commandgroup/init(before_addition_).md>) — A value describing the addition of the given views to the beginning of the indicated group.
- [init(replacing:addition:)](<commandgroup/init(replacing_addition_).md>) — A value describing the complete replacement of the contents of the indicated group with the given views.

## See Also

### Defining commands

- [commands(content:)](<scene/commands(content_).md>) — Adds commands to the scene.
- [commandsRemoved()](<scene/commandsremoved().md>) — Removes all commands defined by the modified scene.
- [commandsReplaced(content:)](<scene/commandsreplaced(content_).md>) — Replaces all commands defined by the modified scene with the commands from the builder.
- [Commands](commands.md) — Conforming types represent a group of related commands that can be exposed to the user via the main menu on macOS and key commands on iOS.
- [CommandMenu](commandmenu.md) — Command menus are stand-alone, top-level containers for controls that perform related, app-specific commands.
- [CommandsBuilder](commandsbuilder.md) — Constructs command sets from multi-expression closures. Like `ContentBuilder`, it supports up to ten expressions in the closure body.
- [CommandGroupPlacement](commandgroupplacement.md) — The standard locations that you can place new command groups relative to.

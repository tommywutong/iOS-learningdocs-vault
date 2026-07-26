---
title: Commands
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/commands
source_url: 'https://developer.apple.com/documentation/swiftui/commands'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/commands.json'
content_hash: 'sha256:7f8004ab27485567'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Commands

<sub>Protocol</sub>

Conforming types represent a group of related commands that can be exposed to the user via the main menu on macOS and key commands on iOS.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency protocol Commands
```

## Overview

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Relationships

- **Conforming Types**: [CommandGroup](commandgroup.md), [CommandMenu](commandmenu.md), [EmptyCommands](emptycommands.md), [EmptyView](emptyview.md), [Group](group.md), [ImportFromDevicesCommands](importfromdevicescommands.md), [InspectorCommands](inspectorcommands.md), [SidebarCommands](sidebarcommands.md), [TextEditingCommands](texteditingcommands.md), [TextFormattingCommands](textformattingcommands.md), [ToolbarCommands](toolbarcommands.md), [TupleContent](tuplecontent.md)

## Topics

### Implementing commands

- [body](commands/body-swift.property.md) — The contents of the command hierarchy.
- [Body](commands/body-swift.associatedtype.md) — The type of commands that represents the body of this command hierarchy.

## See Also

### Defining commands

- [commands(content:)](<scene/commands(content_).md>) — Adds commands to the scene.
- [commandsRemoved()](<scene/commandsremoved().md>) — Removes all commands defined by the modified scene.
- [commandsReplaced(content:)](<scene/commandsreplaced(content_).md>) — Replaces all commands defined by the modified scene with the commands from the builder.
- [CommandMenu](commandmenu.md) — Command menus are stand-alone, top-level containers for controls that perform related, app-specific commands.
- [CommandGroup](commandgroup.md) — Groups of controls that you can add to existing command menus.
- [CommandsBuilder](commandsbuilder.md) — Constructs command sets from multi-expression closures. Like `ContentBuilder`, it supports up to ten expressions in the closure body.
- [CommandGroupPlacement](commandgroupplacement.md) — The standard locations that you can place new command groups relative to.

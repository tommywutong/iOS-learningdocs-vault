---
title: CommandsBuilder
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/commandsbuilder
source_url: 'https://developer.apple.com/documentation/swiftui/commandsbuilder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/commandsbuilder.json'
content_hash: 'sha256:31cc59e4314877ad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# CommandsBuilder

<sub>Structure</sub>

Constructs command sets from multi-expression closures. Like `ContentBuilder`, it supports up to ten expressions in the closure body.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@resultBuilder struct CommandsBuilder
```

## Topics

### Building content

- [buildBlock()](<commandsbuilder/buildblock().md>) — Builds an empty command set from a block containing no statements.
- [buildBlock(_:)](<commandsbuilder/buildblock(__).md>) — Passes a single command group written as a child group through modified.
- [buildBlock(_:_:)](<commandsbuilder/buildblock(____).md>)
- [buildBlock(_:_:_:)](<commandsbuilder/buildblock(______).md>)
- [buildBlock(_:_:_:_:)](<commandsbuilder/buildblock(________).md>)
- [buildBlock(_:_:_:_:_:)](<commandsbuilder/buildblock(__________).md>)
- [buildBlock(_:_:_:_:_:_:)](<commandsbuilder/buildblock(____________).md>)
- [buildBlock(_:_:_:_:_:_:_:)](<commandsbuilder/buildblock(______________).md>)
- [buildBlock(_:_:_:_:_:_:_:_:)](<commandsbuilder/buildblock(________________).md>)
- [buildBlock(_:_:_:_:_:_:_:_:_:)](<commandsbuilder/buildblock(__________________).md>)
- [buildBlock(_:_:_:_:_:_:_:_:_:_:)](<commandsbuilder/buildblock(____________________).md>)

### Building conditionally

- [buildEither(first:)](<commandsbuilder/buildeither(first_).md>) — Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [buildEither(second:)](<commandsbuilder/buildeither(second_).md>) — Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [buildIf(_:)](<commandsbuilder/buildif(__).md>) — Produces an optional widget for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.
- [buildLimitedAvailability(_:)](<commandsbuilder/buildlimitedavailability(__).md>) — Processes commands for a conditional compiler-control statement that performs an availability check.
- [buildExpression(_:)](<commandsbuilder/buildexpression(__).md>) — Builds an expression within the builder.

## See Also

### Defining commands

- [commands(content:)](<scene/commands(content_).md>) — Adds commands to the scene.
- [commandsRemoved()](<scene/commandsremoved().md>) — Removes all commands defined by the modified scene.
- [commandsReplaced(content:)](<scene/commandsreplaced(content_).md>) — Replaces all commands defined by the modified scene with the commands from the builder.
- [Commands](commands.md) — Conforming types represent a group of related commands that can be exposed to the user via the main menu on macOS and key commands on iOS.
- [CommandMenu](commandmenu.md) — Command menus are stand-alone, top-level containers for controls that perform related, app-specific commands.
- [CommandGroup](commandgroup.md) — Groups of controls that you can add to existing command menus.
- [CommandGroupPlacement](commandgroupplacement.md) — The standard locations that you can place new command groups relative to.

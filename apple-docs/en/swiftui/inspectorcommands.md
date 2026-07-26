---
title: InspectorCommands
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/inspectorcommands
source_url: 'https://developer.apple.com/documentation/swiftui/inspectorcommands'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/inspectorcommands.json'
content_hash: 'sha256:0322b4963c47642e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# InspectorCommands

<sub>Structure</sub>

A built-in set of commands for manipulating inspectors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated struct InspectorCommands
```

## Overview

`InspectorCommands` include a command for toggling the presented state of the inspector with a keyboard shortcut of Control-Command-I.

These commands are optional and can be explicitly requested by passing a value of this type to the [commands(content:)](<scene/commands(content_).md>) modifier:

```swift
@State var presented = true
WindowGroup {
    MainView()
        .inspector(isPresented: $presented) {
            InspectorView()
        }
}
.commands {
    InspectorCommands()
}
```

## Relationships

- **Conforms To**: [Commands](commands.md)

## Topics

### Creating a command

- [init()](<inspectorcommands/init().md>) — A new value describing the built-in inspector-related commands.

## See Also

### Getting built-in command groups

- [SidebarCommands](sidebarcommands.md) — A built-in set of commands for manipulating window sidebars.
- [TextEditingCommands](texteditingcommands.md) — A built-in group of commands for searching, editing, and transforming selections of text.
- [TextFormattingCommands](textformattingcommands.md) — A built-in set of commands for transforming the styles applied to selections of text.
- [ToolbarCommands](toolbarcommands.md) — A built-in set of commands for manipulating window toolbars.
- [ImportFromDevicesCommands](importfromdevicescommands.md) — A built-in set of commands that enables importing content from nearby devices.
- [EmptyCommands](emptycommands.md) — An empty group of commands.

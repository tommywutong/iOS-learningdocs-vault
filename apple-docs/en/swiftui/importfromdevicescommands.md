---
title: ImportFromDevicesCommands
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 12.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/importfromdevicescommands
source_url: 'https://developer.apple.com/documentation/swiftui/importfromdevicescommands'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/importfromdevicescommands.json'
content_hash: 'sha256:16775ac81813048c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ImportFromDevicesCommands

<sub>Structure</sub>

A built-in set of commands that enables importing content from nearby devices.

<sub>macOS</sub>

```swift
nonisolated struct ImportFromDevicesCommands
```

## Overview

This set of commands adds items based on nearby devices and capabilities, like taking photos or scanning documents. Views can receive imported content from these menu items by using the [importsItemProviders(_:onImport:)](<view/importsitemproviders(__onimport_).md>) modifier.

These commands are optional and you can explicitly request them by passing a value of this type to the [commands(content:)](<scene/commands(content_).md>) modifier.

## Relationships

- **Conforms To**: [Commands](commands.md)

## Topics

### Creating the command group

- [init()](<importfromdevicescommands/init().md>) — Creates a new set of device import commands.

## See Also

### Getting built-in command groups

- [SidebarCommands](sidebarcommands.md) — A built-in set of commands for manipulating window sidebars.
- [TextEditingCommands](texteditingcommands.md) — A built-in group of commands for searching, editing, and transforming selections of text.
- [TextFormattingCommands](textformattingcommands.md) — A built-in set of commands for transforming the styles applied to selections of text.
- [ToolbarCommands](toolbarcommands.md) — A built-in set of commands for manipulating window toolbars.
- [InspectorCommands](inspectorcommands.md) — A built-in set of commands for manipulating inspectors.
- [EmptyCommands](emptycommands.md) — An empty group of commands.

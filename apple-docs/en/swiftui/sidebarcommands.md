---
title: SidebarCommands
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sidebarcommands
source_url: 'https://developer.apple.com/documentation/swiftui/sidebarcommands'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sidebarcommands.json'
content_hash: 'sha256:89f6403811b684ca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SidebarCommands

<sub>Structure</sub>

A built-in set of commands for manipulating window sidebars.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated struct SidebarCommands
```

## Overview

These commands are optional and can be explicitly requested by passing a value of this type to the [commands(content:)](<scene/commands(content_).md>) modifier.

## Relationships

- **Conforms To**: [Commands](commands.md)

## Topics

### Creating the command group

- [init()](<sidebarcommands/init().md>) — A new value describing the built-in sidebar-related commands.

## See Also

### Getting built-in command groups

- [TextEditingCommands](texteditingcommands.md) — A built-in group of commands for searching, editing, and transforming selections of text.
- [TextFormattingCommands](textformattingcommands.md) — A built-in set of commands for transforming the styles applied to selections of text.
- [ToolbarCommands](toolbarcommands.md) — A built-in set of commands for manipulating window toolbars.
- [ImportFromDevicesCommands](importfromdevicescommands.md) — A built-in set of commands that enables importing content from nearby devices.
- [InspectorCommands](inspectorcommands.md) — A built-in set of commands for manipulating inspectors.
- [EmptyCommands](emptycommands.md) — An empty group of commands.

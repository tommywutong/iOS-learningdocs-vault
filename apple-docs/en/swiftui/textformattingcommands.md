---
title: TextFormattingCommands
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/textformattingcommands
source_url: 'https://developer.apple.com/documentation/swiftui/textformattingcommands'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textformattingcommands.json'
content_hash: 'sha256:42555fa9a54de8d4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TextFormattingCommands

<sub>Structure</sub>

A built-in set of commands for transforming the styles applied to selections of text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated struct TextFormattingCommands
```

## Overview

These commands are optional and can be explicitly requested by passing a value of this type to the `Scene.commands(_:)` modifier.

## Relationships

- **Conforms To**: [Commands](commands.md)

## Topics

### Creating the command group

- [init()](<textformattingcommands/init().md>) — A new value describing the built-in text-formatting commands.

## See Also

### Getting built-in command groups

- [SidebarCommands](sidebarcommands.md) — A built-in set of commands for manipulating window sidebars.
- [TextEditingCommands](texteditingcommands.md) — A built-in group of commands for searching, editing, and transforming selections of text.
- [ToolbarCommands](toolbarcommands.md) — A built-in set of commands for manipulating window toolbars.
- [ImportFromDevicesCommands](importfromdevicescommands.md) — A built-in set of commands that enables importing content from nearby devices.
- [InspectorCommands](inspectorcommands.md) — A built-in set of commands for manipulating inspectors.
- [EmptyCommands](emptycommands.md) — An empty group of commands.

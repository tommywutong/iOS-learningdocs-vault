---
title: DefaultToolbarItem
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/defaulttoolbaritem
source_url: 'https://developer.apple.com/documentation/swiftui/defaulttoolbaritem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/defaulttoolbaritem.json'
content_hash: 'sha256:4436779f2d640a49'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DefaultToolbarItem

<sub>Structure</sub>

A toolbar item that represents a system component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct DefaultToolbarItem
```

## Overview

Place this item in your toolbar to control where the system-provided item, like search, will be positioned.

## Relationships

- **Conforms To**: [ToolbarContent](toolbarcontent.md)

## Topics

### Initializers

- [init(kind:placement:)](<defaulttoolbaritem/init(kind_placement_).md>) — Creates a system-defined toolbar item from a `ToolbarDefaultItemKind` at the given `placement`.

## See Also

### Populating a toolbar

- [toolbar(content:)](<view/toolbar(content_).md>) — Populates the toolbar or navigation bar with the specified items.
- [ToolbarItem](toolbaritem.md) — A model that represents an item which can be placed in the toolbar or navigation bar.
- [ToolbarItemGroup](toolbaritemgroup.md) — A model that represents a group of `ToolbarItem`s which can be placed in the toolbar or navigation bar.
- [ToolbarItemPlacement](toolbaritemplacement.md) — A structure that defines the placement of a toolbar item.
- [toolbarOverflowMenu(content:)](<view/toolbaroverflowmenu(content_).md>) — Configures the overflow menu of a toolbar. _(beta)_
- [ToolbarOverflowMenu](toolbaroverflowmenu.md) — The overflow menu of a toolbar. _(beta)_
- [ToolbarContent](toolbarcontent.md) — Conforming types represent items that can be placed in various locations in a toolbar.
- [ToolbarContentBuilder](toolbarcontentbuilder.md) — Constructs a toolbar item set from multi-expression closures.
- [ToolbarSpacer](toolbarspacer.md) — A standard space item in toolbars.

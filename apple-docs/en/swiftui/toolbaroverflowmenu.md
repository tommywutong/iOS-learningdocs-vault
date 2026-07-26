---
title: ToolbarOverflowMenu
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/toolbaroverflowmenu
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaroverflowmenu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaroverflowmenu.json'
content_hash: 'sha256:3bbaf39b907f82fe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ToolbarOverflowMenu

<sub>Structure</sub>

The overflow menu of a toolbar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated struct ToolbarOverflowMenu<Content> where Content : View
```

## Overview

An overflow menu represents actions that are always placed in the toolbar’s overflow menu, regardless of the toolbar mode, platform, or customizability.

```swift
ContentView()
    .toolbar {
        ToolbarOverflowMenu {
            Button("Action 1") { }
            Button("Action 2") { }
        }
    }
```

In iOS and visionOS, this content is placed into the overflow menu in the navigation bar.

## Relationships

- **Conforms To**: [CustomizableToolbarContent](customizabletoolbarcontent.md), [ToolbarContent](toolbarcontent.md)

## Topics

### Creating a toolbar overflow menu

- [init(content:)](<toolbaroverflowmenu/init(content_).md>) — Creates toolbar overflow menu content. _(beta)_

## See Also

### Populating a toolbar

- [toolbar(content:)](<view/toolbar(content_).md>) — Populates the toolbar or navigation bar with the specified items.
- [ToolbarItem](toolbaritem.md) — A model that represents an item which can be placed in the toolbar or navigation bar.
- [ToolbarItemGroup](toolbaritemgroup.md) — A model that represents a group of `ToolbarItem`s which can be placed in the toolbar or navigation bar.
- [ToolbarItemPlacement](toolbaritemplacement.md) — A structure that defines the placement of a toolbar item.
- [toolbarOverflowMenu(content:)](<view/toolbaroverflowmenu(content_).md>) — Configures the overflow menu of a toolbar. _(beta)_
- [ToolbarContent](toolbarcontent.md) — Conforming types represent items that can be placed in various locations in a toolbar.
- [ToolbarContentBuilder](toolbarcontentbuilder.md) — Constructs a toolbar item set from multi-expression closures.
- [ToolbarSpacer](toolbarspacer.md) — A standard space item in toolbars.
- [DefaultToolbarItem](defaulttoolbaritem.md) — A toolbar item that represents a system component.

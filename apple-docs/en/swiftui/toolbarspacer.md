---
title: ToolbarSpacer
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbarspacer
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarspacer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarspacer.json'
content_hash: 'sha256:5d26088079b0f66f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ToolbarSpacer

<sub>Structure</sub>

A standard space item in toolbars.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
nonisolated struct ToolbarSpacer
```

## Overview

A space item creates visual breaks in the toolbar between items. Spacers can have a standard fixed size or be flexible and push items apart.

Spacers can also be used in customizable toolbars:

```swift
ContentView()
    .toolbar(id: "main-toolbar") {
        ToolbarItem(id: "tag") {
           TagButton()
        }
        ToolbarItem(id: "share") {
           ShareButton()
        }
        ToolbarSpacer(.fixed)
        ToolbarItem(id: "more") {
           MoreButton()
        }
    }
```

Space items are customizable and can be added, removed, and rearranged by users. If a customizable toolbar supports a spacer of a given type, users can also add in multiple copies of that spacer from the customization panel.

## Relationships

- **Conforms To**: [CustomizableToolbarContent](customizabletoolbarcontent.md), [ToolbarContent](toolbarcontent.md)

## Topics

### Initializers

- [init(_:placement:)](<toolbarspacer/init(__placement_).md>) — Creates a toolbar spacer item with the specified sizing behavior and placement.

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
- [DefaultToolbarItem](defaulttoolbaritem.md) — A toolbar item that represents a system component.

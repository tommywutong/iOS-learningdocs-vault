---
title: ToolbarItem
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbaritem
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritem.json'
content_hash: 'sha256:c7a19c2fd1e131e3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ToolbarItem

<sub>Structure</sub>

A model that represents an item which can be placed in the toolbar or navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct ToolbarItem<ID, Content> where Content : View
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomizableToolbarContent](customizabletoolbarcontent.md), [Escapable](../swift/escapable.md), [Identifiable](../swift/identifiable.md), [ToolbarContent](toolbarcontent.md)

## Topics

### Creating a toolbar item

- [init(placement:content:)](<toolbaritem/init(placement_content_).md>) — Creates a toolbar item with the specified placement and content.
- [init(id:placement:content:)](<toolbaritem/init(id_placement_content_).md>) — Creates a toolbar item with the specified placement and content, which allows for user customization.
- [init(id:placement:showsByDefault:content:)](<toolbaritem/init(id_placement_showsbydefault_content_).md>) — Creates a toolbar item with the specified placement and content, which allows for user customization. _(deprecated)_

## See Also

### Populating a toolbar

- [toolbar(content:)](<view/toolbar(content_).md>) — Populates the toolbar or navigation bar with the specified items.
- [ToolbarItemGroup](toolbaritemgroup.md) — A model that represents a group of `ToolbarItem`s which can be placed in the toolbar or navigation bar.
- [ToolbarItemPlacement](toolbaritemplacement.md) — A structure that defines the placement of a toolbar item.
- [toolbarOverflowMenu(content:)](<view/toolbaroverflowmenu(content_).md>) — Configures the overflow menu of a toolbar. _(beta)_
- [ToolbarOverflowMenu](toolbaroverflowmenu.md) — The overflow menu of a toolbar. _(beta)_
- [ToolbarContent](toolbarcontent.md) — Conforming types represent items that can be placed in various locations in a toolbar.
- [ToolbarContentBuilder](toolbarcontentbuilder.md) — Constructs a toolbar item set from multi-expression closures.
- [ToolbarSpacer](toolbarspacer.md) — A standard space item in toolbars.
- [DefaultToolbarItem](defaulttoolbaritem.md) — A toolbar item that represents a system component.

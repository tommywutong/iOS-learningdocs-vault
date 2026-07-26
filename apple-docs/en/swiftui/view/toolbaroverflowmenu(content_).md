---
title: 'toolbarOverflowMenu(content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/view/toolbaroverflowmenu(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/toolbaroverflowmenu(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/toolbaroverflowmenu%28content%3A%29.json'
content_hash: 'sha256:ad4bd12aba01c0d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# toolbarOverflowMenu(content:)

<sub>Instance Method</sub>

Configures the overflow menu of a toolbar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated func toolbarOverflowMenu<C>(@ContentBuilder content: () -> C) -> some View where C : View

```

## Parameters

- `content` — The content of the overflow menu.

## Discussion

An overflow menu represents actions that are always placed in the toolbar’s overflow menu, regardless of the toolbar mode, platform, or customizability.

```swift
ContentView()
    .toolbarOverflowMenu {
        Button("Action 1") { }
        Button("Action 2") { }
    }
```

In iOS and visionOS, this content is placed into the overflow menu in the navigation bar.

## See Also

### Populating a toolbar

- [toolbar(content:)](<toolbar(content_).md>) — Populates the toolbar or navigation bar with the specified items.
- [ToolbarItem](../toolbaritem.md) — A model that represents an item which can be placed in the toolbar or navigation bar.
- [ToolbarItemGroup](../toolbaritemgroup.md) — A model that represents a group of `ToolbarItem`s which can be placed in the toolbar or navigation bar.
- [ToolbarItemPlacement](../toolbaritemplacement.md) — A structure that defines the placement of a toolbar item.
- [ToolbarOverflowMenu](../toolbaroverflowmenu.md) — The overflow menu of a toolbar. _(beta)_
- [ToolbarContent](../toolbarcontent.md) — Conforming types represent items that can be placed in various locations in a toolbar.
- [ToolbarContentBuilder](../toolbarcontentbuilder.md) — Constructs a toolbar item set from multi-expression closures.
- [ToolbarSpacer](../toolbarspacer.md) — A standard space item in toolbars.
- [DefaultToolbarItem](../defaulttoolbaritem.md) — A toolbar item that represents a system component.

---
title: 'contextMenu(forSelectionType:menu:primaryAction:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/contextmenu(forselectiontype:menu:primaryaction:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/contextmenu(forselectiontype:menu:primaryaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/contextmenu%28forselectiontype%3Amenu%3Aprimaryaction%3A%29.json'
content_hash: 'sha256:ba6ecda44d47a05b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# contextMenu(forSelectionType:menu:primaryAction:)

<sub>Instance Method</sub>

Adds an item-based context menu to a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func contextMenu<I, M>(forSelectionType itemType: I.Type = I.self, @ContentBuilder menu: @escaping (Set<I>) -> M, primaryAction: ((Set<I>) -> Void)? = nil) -> some View where I : Hashable, M : View

```

## Parameters

- `itemType` — The identifier type of the items. Ensure that this matches the container’s selection type.

- `menu` — A closure that produces the menu. A single parameter to the closure contains the set of items to act on. An empty set indicates menu activation over the empty area of the selectable container, while a non-empty set indicates menu activation over selected items. Use controls like [Button](../button.md), [Picker](../picker.md), and [Toggle](../toggle.md) to define the menu items. You can also create submenus using [Menu](../menu.md), or group items with [Section](../section.md). You can deactivate the context menu by returning nothing from the closure.

- `primaryAction` — A closure that defines the action to perform in response to the primary interaction. A single parameter to the closure contains the set of items to act on.

## Return Value

A view that can display an item-based context menu.

## Discussion

You can add an item-based context menu to a container that supports selection, like a [List](../list.md) or a [Table](../table.md). In the closure that you use to define the menu, you receive a collection of items that depends on the selection state of the container and the location where the person clicks or taps to activate the menu. The collection contains:

- The selected item or items, when people initiate the context menu from any selected item.
- Nothing, if people tap or click to activate the context menu from an empty part of the container. This is true even when one or more items is currently selected.

You can vary the menu contents according to the number of selected items. For example, the following code has a list that defines an empty area menu, a single item menu, and a multi-item menu:

```swift
struct ContextMenuItemExample: View {
    var items: [Item]
    @State private var selection = Set<Item.ID>()

    var body: some View {
        List(selection: $selection) {
            ForEach(items) { item in
                Text(item.name)
            }
        }
        .contextMenu(forSelectionType: Item.ID.self) { items in
            if items.isEmpty { // Empty area menu.
                Button("New Item") { }

            } else if items.count == 1 { // Single item menu.
                Button("Copy") { }
                Button("Delete", role: .destructive) { }

            } else { // Multi-item menu.
                Button("Copy") { }
                Button("New Folder With Selection") { }
                Button("Delete Selected", role: .destructive) { }
            }
        }
    }
}
```

The above example assumes that the `Item` type conforms to the [Identifiable](../../swift/identifiable.md) protocol, and relies on the associated `ID` type for both selection and context menu presentation.

If you add the modifier to a view hierarchy that doesn’t have a container that supports selection, the context menu never activates. To add a context menu that doesn’t depend on selection behavior, use [contextMenu(menuItems:)](<contextmenu(menuitems_).md>). To add a context menu to a specific row in a table, use [contextMenu(menuItems:)](<../tablerowcontent/contextmenu(menuitems_).md>).

### Add a primary action

Optionally, you can add a custom primary action to the context menu. In macOS, a single click on a row in a selectable container selects that row, and a double click performs the primary action. In iOS and iPadOS, tapping on the row activates the primary action. To select a row without performing an action, either enter edit mode or hold shift or command on a keyboard while tapping the row.

For example, you can modify the context menu from the previous example so that double clicking the row on macOS opens a new window for selected items. Get the [OpenWindowAction](../openwindowaction.md) from the environment:

```swift
@Environment(\.openWindow) private var openWindow
```

Then call [openWindow](../environmentvalues/openwindow.md) from inside the `primaryAction` closure for each item:

```swift
.contextMenu(forSelectionType: Item.ID.self) { items in
    // ...
} primaryAction: { items in
    for item in items {
        openWindow(value: item)
    }
}
```

The open window action depends on the declaration of a [WindowGroup](../windowgroup.md) scene in your [App](../app.md) that responds to the `Item` type:

```swift
WindowGroup("Item Detail", for: Item.self) { $item in
    // ...
}
```

## See Also

### Creating context menus

- [contextMenu(menuItems:)](<contextmenu(menuitems_).md>) — Adds a context menu to a view.
- [contextMenu(menuItems:preview:)](<contextmenu(menuitems_preview_).md>) — Adds a context menu with a custom preview to a view.

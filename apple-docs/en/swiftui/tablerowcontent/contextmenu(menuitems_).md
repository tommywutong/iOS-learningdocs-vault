---
title: 'contextMenu(menuItems:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablerowcontent/contextmenu(menuitems:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablerowcontent/contextmenu(menuitems:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablerowcontent/contextmenu%28menuitems%3A%29.json'
content_hash: 'sha256:2224f2b5479d0e72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableRowContent](../tablerowcontent.md)

# contextMenu(menuItems:)

<sub>Instance Method</sub>

Adds a context menu to a table row.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func contextMenu<M>(@ContentBuilder menuItems: () -> M) -> ModifiedContent<Self, _ContextMenuTableRowModifier<M>> where M : View
```

## Parameters

- `menuItems` — A closure that produces the menu’s contents. You can deactivate the context menu by returning nothing from the closure.

## Return Value

A row that can display a context menu.

## Discussion

Use this modifier to add a context menu to a table row. Compose the menu by returning controls like [Button](../button.md), [Toggle](../toggle.md), and [Picker](../picker.md) from the `menuItems` closure. You can also use [Menu](../menu.md) to define submenus, or [Section](../section.md) to group items.

The following example adds a context menu to each row in a table that people can use to send an email to the person represented by that row:

```swift
Table(of: Person.self) {
    TableColumn("Given Name", value: \.givenName)
    TableColumn("Family Name", value: \.familyName)
} rows: {
    ForEach(people) { person in
        TableRow(person)
            .contextMenu {
                Button("Send Email...") { }
            }
    }
}
```

If you want to display a preview beside the context menu, use [contextMenu(menuItems:preview:)](<contextmenu(menuitems_preview_).md>). If you want to display a context menu that’s based on the current selection, use [contextMenu(forSelectionType:menu:primaryAction:)](<../view/contextmenu(forselectiontype_menu_primaryaction_).md>). To add context menus to other kinds of views, use [contextMenu(menuItems:)](<../view/contextmenu(menuitems_).md>).

## See Also

### Adding a context menu to a row

- [contextMenu(menuItems:preview:)](<contextmenu(menuitems_preview_).md>) — Adds a context menu with a preview to a table row.

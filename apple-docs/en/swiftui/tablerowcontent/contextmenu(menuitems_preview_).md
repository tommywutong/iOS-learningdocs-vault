---
title: 'contextMenu(menuItems:preview:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablerowcontent/contextmenu(menuitems:preview:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablerowcontent/contextmenu(menuitems:preview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablerowcontent/contextmenu%28menuitems%3Apreview%3A%29.json'
content_hash: 'sha256:626ec4800d8df280'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableRowContent](../tablerowcontent.md)

# contextMenu(menuItems:preview:)

<sub>Instance Method</sub>

Adds a context menu with a preview to a table row.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func contextMenu<M, P>(@ContentBuilder menuItems: () -> M, @ContentBuilder preview: () -> P) -> ModifiedContent<Self, _ContextMenuPreviewTableRowModifier<M, P>> where M : View, P : View
```

## Parameters

- `menuItems` — A closure that produces the menu’s contents. You can deactivate the context menu by returning nothing from the closure.

- `preview` — A view that the system displays along with the menu.

## Return Value

A row that can display a context menu with a preview.

## Discussion

When you use this modifier to add a context menu to rows in a table, the system shows a preview beside the menu. Compose the menu by returning controls like [Button](../button.md), [Toggle](../toggle.md), and [Picker](../picker.md) from the `menuItems` closure. You can also use [Menu](../menu.md) to define submenus.

Define the preview by returning a view from the `preview` closure. The system sizes the preview to match the size of its content. For example, the following code adds a context menu with a preview to each row in a table that people can use to send an email to the person represented by that row:

```swift
Table(of: Person.self) {
    TableColumn("Given Name", value: \.givenName)
    TableColumn("Family Name", value: \.familyName)
} rows: {
    ForEach(people) { person in
        TableRow(person)
            .contextMenu {
                Button("Send Email...") { }
            } preview: {
                Image("envelope") // Loads the image from an asset catalog.
            }
    }
}
```

> [!note] Note
> This view modifier produces a context menu on macOS, but that platform doesn’t display the preview.

If you don’t need a preview, use [contextMenu(menuItems:)](<contextmenu(menuitems_).md>). If you want to display a context menu that’s based on the current selection, use [contextMenu(forSelectionType:menu:primaryAction:)](<../view/contextmenu(forselectiontype_menu_primaryaction_).md>). To add context menus to other kinds of views, see [contextMenu(menuItems:)](<../view/contextmenu(menuitems_).md>).

## See Also

### Adding a context menu to a row

- [contextMenu(menuItems:)](<contextmenu(menuitems_).md>) — Adds a context menu to a table row.

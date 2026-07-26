---
title: 'init(_:children:selection:columnCustomization:columns:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/table/init(_:children:selection:columncustomization:columns:)'
source_url: 'https://developer.apple.com/documentation/swiftui/table/init(_:children:selection:columncustomization:columns:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/table/init%28_%3Achildren%3Aselection%3Acolumncustomization%3Acolumns%3A%29.json'
content_hash: 'sha256:e269b8db066b1f82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Table](../table.md)

# init(_:children:selection:columnCustomization:columns:)

<sub>Initializer</sub>

Creates a hierarchical table that computes its rows based on a collection of identifiable data and key path to the children of that data, and supports selecting multiple rows.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init<Data>(_ data: Data, children: KeyPath<Data.Element, Data?>, selection: Binding<Set<Value.ID>>, columnCustomization: Binding<TableColumnCustomization<Value>>? = nil, @TableColumnBuilder<Value, Never> columns: () -> Columns) where Rows == TableOutlineGroupContent<Data>, Data : RandomAccessCollection, Columns.TableRowValue == Data.Element
```

## Parameters

- `data` — The identifiable data for computing the table rows.

- `children` — A key path to a property whose non-`nil` value gives the children of `data`, and whose `nil` value represents a leaf row of the hierarchy, which is not capable of having children.

- `selection` — A binding to a set that identifies selected rows IDs.

- `columnCustomization` — A binding to the state of columns.

- `columns` — The columns to display in the table.

## Discussion

Each column in the table that should participate in customization is required to have an identifier, specified with [customizationID(_:)](<../tablecolumncontent/customizationid(__).md>).

## See Also

### Creating a hierarchical table

- [init(_:children:columnCustomization:columns:)](<init(__children_columncustomization_columns_).md>) — Creates a hierarchical table that computes its rows based on a collection of identifiable data and key path to the children of that data.
- [init(_:children:selection:sortOrder:columnCustomization:columns:)](<init(__children_selection_sortorder_columncustomization_columns_).md>) — Creates a sortable, hierarchical table that computes its rows based on a collection of identifiable data and key path to the children of that data, and supports selecting multiple rows.
- [init(_:children:sortOrder:columnCustomization:columns:)](<init(__children_sortorder_columncustomization_columns_).md>) — Creates a sortable, hierarchical table that computes its rows based on a collection of identifiable data and key path to the children of that data.

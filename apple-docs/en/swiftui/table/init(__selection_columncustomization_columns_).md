---
title: 'init(_:selection:columnCustomization:columns:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/table/init(_:selection:columncustomization:columns:)'
source_url: 'https://developer.apple.com/documentation/swiftui/table/init(_:selection:columncustomization:columns:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/table/init%28_%3Aselection%3Acolumncustomization%3Acolumns%3A%29.json'
content_hash: 'sha256:b609521ee14847ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Table](../table.md)

# init(_:selection:columnCustomization:columns:)

<sub>Initializer</sub>

Creates a table that computes its rows based on a collection of identifiable data, that supports selecting multiple rows, and that has dynamically customizable columns.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init<Data>(_ data: Data, selection: Binding<Set<Value.ID>>, columnCustomization: Binding<TableColumnCustomization<Value>>, @TableColumnBuilder<Value, Never> columns: () -> Columns) where Rows == TableForEachContent<Data>, Data : RandomAccessCollection, Columns.TableRowValue == Data.Element
```

## Parameters

- `data` — The identifiable data for computing the table rows.

- `selection` — A binding to a set that identifies selected rows IDs.

- `columnCustomization` — A binding to the state of columns.

- `columns` — The columns to display in the table.

## Discussion

Each column in the table that should participate in customization is required to have an identifier, specified with [customizationID(_:)](<../tablecolumncontent/customizationid(__).md>).

## See Also

### Creating a table with customizable columns

- [init(_:columnCustomization:columns:)](<init(__columncustomization_columns_).md>) — Creates a table that computes its rows based on a collection of identifiable data and has dynamically customizable columns.
- [init(_:selection:sortOrder:columnCustomization:columns:)](<init(__selection_sortorder_columncustomization_columns_).md>) — Creates a sortable table that computes its rows based on a collection of identifiable data, supports selecting multiple rows, and has dynamically customizable columns.
- [init(_:sortOrder:columnCustomization:columns:)](<init(__sortorder_columncustomization_columns_).md>) — Creates a sortable table that computes its rows based on a collection of identifiable data and has dynamically customizable columns.

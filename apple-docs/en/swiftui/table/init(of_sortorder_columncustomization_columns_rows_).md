---
title: 'init(of:sortOrder:columnCustomization:columns:rows:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/table/init(of:sortorder:columncustomization:columns:rows:)'
source_url: 'https://developer.apple.com/documentation/swiftui/table/init(of:sortorder:columncustomization:columns:rows:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/table/init%28of%3Asortorder%3Acolumncustomization%3Acolumns%3Arows%3A%29.json'
content_hash: 'sha256:97b2132fee8ded14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Table](../table.md)

# init(of:sortOrder:columnCustomization:columns:rows:)

<sub>Initializer</sub>

Creates a sortable table with the given columns and rows and has dynamically customizable columns.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init<Sort>(of valueType: Value.Type = Value.self, sortOrder: Binding<[Sort]>, columnCustomization: Binding<TableColumnCustomization<Value>>, @TableColumnBuilder<Value, Sort> columns: () -> Columns, @TableRowBuilder<Value> rows: () -> Rows) where Sort : SortComparator, Columns.TableRowValue == Sort.Compared
```

## Parameters

- `valueType` — The type of value used to derive the table’s contents.

- `sortOrder` — A binding to the ordered sorting of columns.

- `columnCustomization` — A binding to the state of columns.

- `columns` — The columns to display in the table.

- `rows` — The rows to display in the table.

## Discussion

Each column in the table that should participate in customization is required to have an identifier, specified with [customizationID(_:)](<../tablecolumncontent/customizationid(__).md>).

## See Also

### Creating a table with dynamically customizable columns

- [init(of:columnCustomization:columns:rows:)](<init(of_columncustomization_columns_rows_).md>) — Creates a table with the given columns and rows that generates its contents using values of the given type and has dynamically customizable columns.
- [init(of:selection:columnCustomization:columns:rows:)](<init(of_selection_columncustomization_columns_rows_).md>) — Creates a table with the given columns and rows that supports selecting multiple rows that generates its data using values of the given type and has dynamically customizable columns.
- [init(of:selection:sortOrder:columnCustomization:columns:rows:)](<init(of_selection_sortorder_columncustomization_columns_rows_).md>) — Creates a sortable table with the given columns and rows that supports selecting multiple rows and dynamically customizable columns.

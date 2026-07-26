---
title: 'init(of:selection:sortOrder:columns:rows:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/table/init(of:selection:sortorder:columns:rows:)'
source_url: 'https://developer.apple.com/documentation/swiftui/table/init(of:selection:sortorder:columns:rows:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/table/init%28of%3Aselection%3Asortorder%3Acolumns%3Arows%3A%29.json'
content_hash: 'sha256:23f7ad56f44a6396'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Table](../table.md)

# init(of:selection:sortOrder:columns:rows:)

<sub>Initializer</sub>

Creates a sortable table with the given columns and rows that supports selecting multiple rows.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated init<Sort>(of valueType: Value.Type, selection: Binding<Set<Value.ID>>, sortOrder: Binding<[Sort]>, @TableColumnBuilder<Value, Sort> columns: () -> Columns, @TableRowBuilder<Value> rows: () -> Rows) where Sort : SortComparator, Columns.TableRowValue == Sort.Compared
```

## Parameters

- `valueType` — The type of value used to derive the table’s contents.

- `selection` — A binding to a set that identifies selected rows ids.

- `sortOrder` — A binding to the ordered sorting of columns.

- `columns` — The columns to display in the table.

- `rows` — The rows to display in the table.

## See Also

### Creating a sortable table from columns and rows

- [init(of:sortOrder:columns:rows:)](<init(of_sortorder_columns_rows_).md>) — Creates a sortable table with the given columns and rows.
- [init(sortOrder:columns:rows:)](<init(sortorder_columns_rows_).md>) — Creates a sortable table with the given columns and rows.
- [init(selection:sortOrder:columns:rows:)](<init(selection_sortorder_columns_rows_).md>) — Creates a sortable table with the given columns and rows that supports selecting multiple rows.

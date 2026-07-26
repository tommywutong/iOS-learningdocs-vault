---
title: 'init(_:selection:sortOrder:columns:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/table/init(_:selection:sortorder:columns:)'
source_url: 'https://developer.apple.com/documentation/swiftui/table/init(_:selection:sortorder:columns:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/table/init%28_%3Aselection%3Asortorder%3Acolumns%3A%29.json'
content_hash: 'sha256:7a1be092f9cea594'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Table](../table.md)

# init(_:selection:sortOrder:columns:)

<sub>Initializer</sub>

Creates a sortable table that computes its rows based on a collection of identifiable data, and supports selecting multiple rows.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init<Data, Sort>(_ data: Data, selection: Binding<Set<Value.ID>>, sortOrder: Binding<[Sort]>, @TableColumnBuilder<Value, Sort> columns: () -> Columns) where Rows == TableForEachContent<Data>, Data : RandomAccessCollection, Sort : SortComparator, Columns.TableRowValue == Data.Element, Data.Element == Sort.Compared
```

## Parameters

- `data` — The identifiable data for computing the table rows.

- `selection` — A binding to a set that identifies selected rows IDs.

- `sortOrder` — A binding to the ordered sorting of columns.

- `columns` — The columns to display in the table.

## See Also

### Creating a sortable table from columns

- [init(_:sortOrder:columns:)](<init(__sortorder_columns_).md>) — Creates a sortable table that computes its rows based on a collection of identifiable data.

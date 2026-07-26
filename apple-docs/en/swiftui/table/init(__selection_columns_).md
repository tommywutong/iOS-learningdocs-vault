---
title: 'init(_:selection:columns:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/table/init(_:selection:columns:)'
source_url: 'https://developer.apple.com/documentation/swiftui/table/init(_:selection:columns:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/table/init%28_%3Aselection%3Acolumns%3A%29.json'
content_hash: 'sha256:c1220b2272b89482'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Table](../table.md)

# init(_:selection:columns:)

<sub>Initializer</sub>

Creates a table that computes its rows based on a collection of identifiable data, and that supports selecting multiple rows.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init<Data>(_ data: Data, selection: Binding<Set<Value.ID>>, @TableColumnBuilder<Value, Never> columns: () -> Columns) where Rows == TableForEachContent<Data>, Data : RandomAccessCollection, Columns.TableRowValue == Data.Element
```

## Parameters

- `data` — The identifiable data for computing the table rows.

- `selection` — A binding to a set that identifies selected rows IDs.

- `columns` — The columns to display in the table.

## See Also

### Creating a table from columns

- [init(_:columns:)](<init(__columns_).md>) — Creates a table that computes its rows based on a collection of identifiable data.

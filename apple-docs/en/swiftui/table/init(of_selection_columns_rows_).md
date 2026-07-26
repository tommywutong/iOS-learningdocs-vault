---
title: 'init(of:selection:columns:rows:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/table/init(of:selection:columns:rows:)'
source_url: 'https://developer.apple.com/documentation/swiftui/table/init(of:selection:columns:rows:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/table/init%28of%3Aselection%3Acolumns%3Arows%3A%29.json'
content_hash: 'sha256:c8d274920501d2bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Table](../table.md)

# init(of:selection:columns:rows:)

<sub>Initializer</sub>

Creates a table with the given columns and rows that supports selecting multiple rows that generates its data using values of the given type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated init(of valueType: Value.Type, selection: Binding<Set<Value.ID>>, @TableColumnBuilder<Value, Never> columns: () -> Columns, @TableRowBuilder<Value> rows: () -> Rows)
```

## Parameters

- `valueType` — The type of value used to derive the table’s contents.

- `selection` — A binding to a set that identifies the selected rows IDs.

- `columns` — The columns to display in the table.

- `rows` — The rows to display in the table.

## See Also

### Creating a table from columns and rows

- [init(of:columns:rows:)](<init(of_columns_rows_).md>) — Creates a table with the given columns and rows that generates its contents using values of the given type.

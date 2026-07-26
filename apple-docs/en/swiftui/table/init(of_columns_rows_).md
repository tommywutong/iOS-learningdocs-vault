---
title: 'init(of:columns:rows:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/table/init(of:columns:rows:)'
source_url: 'https://developer.apple.com/documentation/swiftui/table/init(of:columns:rows:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/table/init%28of%3Acolumns%3Arows%3A%29.json'
content_hash: 'sha256:69bceecfbaa3d1fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Table](../table.md)

# init(of:columns:rows:)

<sub>Initializer</sub>

Creates a table with the given columns and rows that generates its contents using values of the given type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated init(of valueType: Value.Type, @TableColumnBuilder<Value, Never> columns: () -> Columns, @TableRowBuilder<Value> rows: () -> Rows)
```

## Parameters

- `valueType` — The type of value used to derive the table’s contents.

- `columns` — The columns to display in the table.

- `rows` — The rows to display in the table.

## See Also

### Creating a table from columns and rows

- [init(of:selection:columns:rows:)](<init(of_selection_columns_rows_).md>) — Creates a table with the given columns and rows that supports selecting multiple rows that generates its data using values of the given type.

---
title: 'init(_:id:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, visionOS 1.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablecolumnforeach/init(_:id:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumnforeach/init(_:id:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumnforeach/init%28_%3Aid%3Acontent%3A%29.json'
content_hash: 'sha256:b01e3cb579856525'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableColumnForEach](../tablecolumnforeach.md)

# init(_:id:content:)

<sub>Initializer</sub>

Creates an instance that uniquely identifies and creates table columns across updates based on the provided key path to the underlying data’s identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init(_ data: Data, id: KeyPath<Data.Element, ID>, @TableColumnBuilder<TableColumnForEach<Data, ID, RowValue, Sort, Content>.TableRowValue, TableColumnForEach<Data, ID, RowValue, Sort, Content>.TableColumnSortComparator> content: @escaping (Data.Element) -> Content)
```

## Parameters

- `data` — The data that the [TableColumnForEach](../tablecolumnforeach.md) instance uses to create table columns dynamically.

- `id` — The key path to the provided data’s identifier.

- `content` — The table column builder that creates columns dynamically for each element.

## See Also

### Creating the collection

- [init(_:content:)](<init(__content_).md>) — Creates an instance that uniquely identifies and creates table columns across updates based on the identity of the underlying data.

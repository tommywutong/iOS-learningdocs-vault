---
title: TableForEachContent
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tableforeachcontent
source_url: 'https://developer.apple.com/documentation/swiftui/tableforeachcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tableforeachcontent.json'
content_hash: 'sha256:daf179e453fdb254'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TableForEachContent

<sub>Structure</sub>

A type of table row content that creates table rows created by iterating over a collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated struct TableForEachContent<Data> where Data : RandomAccessCollection, Data.Element : Identifiable
```

## Overview

You don’t use this type directly. The various `Table.init(_:,...)` initializers create this type as the table’s `Rows` generic type.

To explicitly create dynamic collection-based rows, use [ForEach](foreach.md) instead.

## Relationships

- **Conforms To**: [TableRowContent](tablerowcontent.md)

## See Also

### Creating rows

- [TableRow](tablerow.md) — A row that represents a data value in a table.
- [TableRowContent](tablerowcontent.md) — A type used to represent table rows.
- [TableHeaderRowContent](tableheaderrowcontent.md) — A table row that displays a single view instead of columned content.
- [TupleTableRowContent](tupletablerowcontent.md) — A type of table column content that creates table rows created from a Swift tuple of table rows.
- [EmptyTableRowContent](emptytablerowcontent.md) — A table row content that doesn’t produce any rows.
- [DynamicTableRowContent](dynamictablerowcontent.md) — A type of table row content that generates table rows from an underlying collection of data.
- [TableRowBuilder](tablerowbuilder.md) — A result builder that creates table row content from closures.

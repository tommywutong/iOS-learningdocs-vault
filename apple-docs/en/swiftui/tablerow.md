---
title: TableRow
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tablerow
source_url: 'https://developer.apple.com/documentation/swiftui/tablerow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablerow.json'
content_hash: 'sha256:7cd6cde8dcf277e0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TableRow

<sub>Structure</sub>

A row that represents a data value in a table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated struct TableRow<Value> where Value : Identifiable
```

## Overview

Create instances of [TableRow](tablerow.md) in the closure you provide to the `rows` parameter in [Table](table.md) initializers that take columns and rows. The table provides the value of a row to each column of a table, which produces the cells for each row in the column.

## Relationships

- **Conforms To**: [TableRowContent](tablerowcontent.md)

## Topics

### Creating a row

- [init(_:)](<tablerow/init(__).md>) — Creates a table row for the given value.

## See Also

### Creating rows

- [TableRowContent](tablerowcontent.md) — A type used to represent table rows.
- [TableHeaderRowContent](tableheaderrowcontent.md) — A table row that displays a single view instead of columned content.
- [TupleTableRowContent](tupletablerowcontent.md) — A type of table column content that creates table rows created from a Swift tuple of table rows.
- [TableForEachContent](tableforeachcontent.md) — A type of table row content that creates table rows created by iterating over a collection.
- [EmptyTableRowContent](emptytablerowcontent.md) — A table row content that doesn’t produce any rows.
- [DynamicTableRowContent](dynamictablerowcontent.md) — A type of table row content that generates table rows from an underlying collection of data.
- [TableRowBuilder](tablerowbuilder.md) — A result builder that creates table row content from closures.

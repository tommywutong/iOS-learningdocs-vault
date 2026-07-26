---
title: TableHeaderRowContent
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tableheaderrowcontent
source_url: 'https://developer.apple.com/documentation/swiftui/tableheaderrowcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tableheaderrowcontent.json'
content_hash: 'sha256:cf19ce7f056f74fb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TableHeaderRowContent

<sub>Structure</sub>

A table row that displays a single view instead of columned content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated struct TableHeaderRowContent<Value, Content> where Value : Identifiable, Content : View
```

## Overview

You do not create this type directly. The framework creates it on your behalf.

## Relationships

- **Conforms To**: [TableRowContent](tablerowcontent.md)

## See Also

### Creating rows

- [TableRow](tablerow.md) — A row that represents a data value in a table.
- [TableRowContent](tablerowcontent.md) — A type used to represent table rows.
- [TupleTableRowContent](tupletablerowcontent.md) — A type of table column content that creates table rows created from a Swift tuple of table rows.
- [TableForEachContent](tableforeachcontent.md) — A type of table row content that creates table rows created by iterating over a collection.
- [EmptyTableRowContent](emptytablerowcontent.md) — A table row content that doesn’t produce any rows.
- [DynamicTableRowContent](dynamictablerowcontent.md) — A type of table row content that generates table rows from an underlying collection of data.
- [TableRowBuilder](tablerowbuilder.md) — A result builder that creates table row content from closures.

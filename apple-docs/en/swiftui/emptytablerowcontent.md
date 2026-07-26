---
title: EmptyTableRowContent
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/emptytablerowcontent
source_url: 'https://developer.apple.com/documentation/swiftui/emptytablerowcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/emptytablerowcontent.json'
content_hash: 'sha256:8da521020e167bf3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# EmptyTableRowContent

<sub>Structure</sub>

A table row content that doesn’t produce any rows.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated struct EmptyTableRowContent<Value> where Value : Identifiable
```

## Overview

You will rarely, if ever, need to create an `EmptyTableRowContent` directly. Instead, `EmptyTableRowContent` represents the absence of a row.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [TableRowContent](tablerowcontent.md)

## See Also

### Creating rows

- [TableRow](tablerow.md) — A row that represents a data value in a table.
- [TableRowContent](tablerowcontent.md) — A type used to represent table rows.
- [TableHeaderRowContent](tableheaderrowcontent.md) — A table row that displays a single view instead of columned content.
- [TupleTableRowContent](tupletablerowcontent.md) — A type of table column content that creates table rows created from a Swift tuple of table rows.
- [TableForEachContent](tableforeachcontent.md) — A type of table row content that creates table rows created by iterating over a collection.
- [DynamicTableRowContent](dynamictablerowcontent.md) — A type of table row content that generates table rows from an underlying collection of data.
- [TableRowBuilder](tablerowbuilder.md) — A result builder that creates table row content from closures.

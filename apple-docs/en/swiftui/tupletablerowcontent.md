---
title: TupleTableRowContent
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tupletablerowcontent
source_url: 'https://developer.apple.com/documentation/swiftui/tupletablerowcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tupletablerowcontent.json'
content_hash: 'sha256:72e5864b9644fd37'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TupleTableRowContent

<sub>Structure</sub>

A type of table column content that creates table rows created from a Swift tuple of table rows.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@frozen nonisolated struct TupleTableRowContent<Value, T> where Value : Identifiable
```

## Overview

Don’t use this type directly; instead, SwiftUI uses this type as the return value from the various `buildBlock` methods in [TableRowBuilder](tablerowbuilder.md). The size of the tuple corresponds to how many columns you create in the `rows` closure you provide to the [Table](table.md) initializer.

## Relationships

- **Conforms To**: [TableRowContent](tablerowcontent.md)

## Topics

### Accessing the value

- [value](tupletablerowcontent/value.md)

## See Also

### Creating rows

- [TableRow](tablerow.md) — A row that represents a data value in a table.
- [TableRowContent](tablerowcontent.md) — A type used to represent table rows.
- [TableHeaderRowContent](tableheaderrowcontent.md) — A table row that displays a single view instead of columned content.
- [TableForEachContent](tableforeachcontent.md) — A type of table row content that creates table rows created by iterating over a collection.
- [EmptyTableRowContent](emptytablerowcontent.md) — A table row content that doesn’t produce any rows.
- [DynamicTableRowContent](dynamictablerowcontent.md) — A type of table row content that generates table rows from an underlying collection of data.
- [TableRowBuilder](tablerowbuilder.md) — A result builder that creates table row content from closures.

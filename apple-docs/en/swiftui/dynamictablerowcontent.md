---
title: DynamicTableRowContent
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dynamictablerowcontent
source_url: 'https://developer.apple.com/documentation/swiftui/dynamictablerowcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dynamictablerowcontent.json'
content_hash: 'sha256:d4f596a1fd7ddae9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DynamicTableRowContent

<sub>Protocol</sub>

A type of table row content that generates table rows from an underlying collection of data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
protocol DynamicTableRowContent : TableRowContent
```

## Overview

This table row content type provides drag-and-drop support for tables. Use the [onInsert(of:perform:)](<dynamictablerowcontent/oninsert(of_perform_).md>) modifier to add an action to call when the table inserts new contents into its underlying collection.

## Relationships

- **Inherits From**: [TableRowContent](tablerowcontent.md)

- **Conforming Types**: [ForEach](foreach.md), [ModifiedContent](modifiedcontent.md)

## Topics

### Getting row data

- [data](dynamictablerowcontent/data-swift.property.md) — The collection of underlying data.
- [Data](dynamictablerowcontent/data-swift.associatedtype.md) — The type of the underlying collection of data.

### Inserting rows

- [onInsert(of:perform:)](<dynamictablerowcontent/oninsert(of_perform_).md>) — Sets the insert action for the dynamic table rows.
- [OnInsertTableRowModifier](oninserttablerowmodifier.md) — A table row modifier that adds the ability to insert data in some base row content.

### Supporting drag and drop

- [dropDestination(for:action:)](<dynamictablerowcontent/dropdestination(for_action_).md>) — Sets the insert action for the dynamic table rows.

## See Also

### Creating rows

- [TableRow](tablerow.md) — A row that represents a data value in a table.
- [TableRowContent](tablerowcontent.md) — A type used to represent table rows.
- [TableHeaderRowContent](tableheaderrowcontent.md) — A table row that displays a single view instead of columned content.
- [TupleTableRowContent](tupletablerowcontent.md) — A type of table column content that creates table rows created from a Swift tuple of table rows.
- [TableForEachContent](tableforeachcontent.md) — A type of table row content that creates table rows created by iterating over a collection.
- [EmptyTableRowContent](emptytablerowcontent.md) — A table row content that doesn’t produce any rows.
- [TableRowBuilder](tablerowbuilder.md) — A result builder that creates table row content from closures.

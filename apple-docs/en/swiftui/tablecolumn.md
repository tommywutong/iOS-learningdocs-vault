---
title: TableColumn
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tablecolumn
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumn.json'
content_hash: 'sha256:932231db852ffd34'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TableColumn

<sub>Structure</sub>

A column that displays a view for each row in a table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated struct TableColumn<RowValue, Sort, Content, Label> where RowValue : Identifiable, Sort : SortComparator, Content : View, Label : View
```

## Overview

You create a column with a label, content view, and optional key path. The table calls the content content builder with the value for each row in the table. The column uses a key path to map to a property of each row value, which sortable tables use to reflect the current sort order.

The following example creates a sortable column for a table with `Person` rows, displaying each person’s given name:

```swift
TableColumn("Given name", value: \.givenName) { person in
    Text(person.givenName)
}
```

For the common case of `String` properties, you can use the convenience initializer that doesn’t require an explicit content closure and displays that string verbatim as a [Text](text.md) view. This means you can write the previous example as:

```swift
TableColumn("Given name", value: \.givenName)
```

## Relationships

- **Conforms To**: [TableColumnContent](tablecolumncontent.md)

## Topics

### Creating an unsortable column

- [init(_:value:)](<tablecolumn/init(__value_).md>) — Creates an unsortable column that displays a string property that generates its label from a localized string resource.
- [init(_:content:)](<tablecolumn/init(__content_).md>) — Creates an unsortable column that generates its label from a localized string resource.

### Creating a sortable column

- [init(_:value:content:)](<tablecolumn/init(__value_content_).md>) — Creates a sortable column for Boolean values that generates its label from a localized string resource.
- [init(_:value:comparator:)](<tablecolumn/init(__value_comparator_).md>) — Creates a sortable column that displays a string property, and generates its label from a localized string resource.
- [init(_:value:comparator:content:)](<tablecolumn/init(__value_comparator_content_).md>) — Creates a sortable column that generates its label from a localized string resource.
- [init(_:sortUsing:content:)](<tablecolumn/init(__sortusing_content_).md>) — Creates a sortable column that generates its label from a localized string resource.

### Setting the column width

- [width(_:)](<tablecolumn/width(__).md>) — Creates a fixed width table column that isn’t user resizable.
- [width(min:ideal:max:)](<tablecolumn/width(min_ideal_max_).md>) — Creates a resizable table column with the provided constraints.
- [width()](<tablecolumn/width().md>) — Sets the column’s width. _(deprecated)_

## See Also

### Creating columns

- [TableColumnContent](tablecolumncontent.md) — A type used to represent columns within a table.
- [TableColumnAlignment](tablecolumnalignment.md) — Describes the alignment of the content of a table column.
- [TableColumnBuilder](tablecolumnbuilder.md) — A result builder that creates table column content from closures.
- [TableColumnForEach](tablecolumnforeach.md) — A structure that computes columns on demand from an underlying collection of identified data.

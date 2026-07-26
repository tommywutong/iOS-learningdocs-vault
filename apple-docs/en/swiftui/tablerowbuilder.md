---
title: TableRowBuilder
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tablerowbuilder
source_url: 'https://developer.apple.com/documentation/swiftui/tablerowbuilder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablerowbuilder.json'
content_hash: 'sha256:4131ded81cdb8329'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TableRowBuilder

<sub>Structure</sub>

A result builder that creates table row content from closures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@resultBuilder struct TableRowBuilder<Value> where Value : Identifiable
```

## Overview

The `buildBlock` methods in this type create [TableRowContent](tablerowcontent.md) instances based on the number and types of sources provided as parameters.

Don’t use this type directly; instead, SwiftUI annotates the `rows` parameter of the various [Table](table.md) initializers with the `@TableRowBuilder` annotation, implicitly calling this builder for you.

## Topics

### Building a row from sources

- [buildBlock(_:)](<tablerowbuilder/buildblock(__).md>) — Creates a single row result.
- [buildBlock(_:_:)](<tablerowbuilder/buildblock(____).md>) — Creates a row result from two sources.
- [buildBlock(_:_:_:)](<tablerowbuilder/buildblock(______).md>) — Creates a row result from three sources.
- [buildBlock(_:_:_:_:)](<tablerowbuilder/buildblock(________).md>) — Creates a row result from four sources.
- [buildBlock(_:_:_:_:_:)](<tablerowbuilder/buildblock(__________).md>) — Creates a row result from five sources.
- [buildBlock(_:_:_:_:_:_:)](<tablerowbuilder/buildblock(____________).md>) — Creates a row result from six sources.
- [buildBlock(_:_:_:_:_:_:_:)](<tablerowbuilder/buildblock(______________).md>) — Creates a row result from seven sources.
- [buildBlock(_:_:_:_:_:_:_:_:)](<tablerowbuilder/buildblock(________________).md>) — Creates a row result from eight sources.
- [buildBlock(_:_:_:_:_:_:_:_:_:)](<tablerowbuilder/buildblock(__________________).md>) — Creates a row result from nine sources.
- [buildBlock(_:_:_:_:_:_:_:_:_:_:)](<tablerowbuilder/buildblock(____________________).md>) — Creates a row result from ten sources.

### Building a row from conditionals

- [buildIf(_:)](<tablerowbuilder/buildif(__).md>) — Creates a row result for conditional statements.
- [buildEither(first:)](<tablerowbuilder/buildeither(first_).md>) — Creates a row result for the first of two row content alternatives.
- [buildEither(second:)](<tablerowbuilder/buildeither(second_).md>) — Creates a row result for the second of two row content alternatives.
- [buildExpression(_:)](<tablerowbuilder/buildexpression(__).md>) — Builds an expression within the builder.

## See Also

### Creating rows

- [TableRow](tablerow.md) — A row that represents a data value in a table.
- [TableRowContent](tablerowcontent.md) — A type used to represent table rows.
- [TableHeaderRowContent](tableheaderrowcontent.md) — A table row that displays a single view instead of columned content.
- [TupleTableRowContent](tupletablerowcontent.md) — A type of table column content that creates table rows created from a Swift tuple of table rows.
- [TableForEachContent](tableforeachcontent.md) — A type of table row content that creates table rows created by iterating over a collection.
- [EmptyTableRowContent](emptytablerowcontent.md) — A table row content that doesn’t produce any rows.
- [DynamicTableRowContent](dynamictablerowcontent.md) — A type of table row content that generates table rows from an underlying collection of data.

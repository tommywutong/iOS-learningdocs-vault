---
title: TableColumnBuilder
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tablecolumnbuilder
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumnbuilder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumnbuilder.json'
content_hash: 'sha256:2957460bb025586a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TableColumnBuilder

<sub>Structure</sub>

A result builder that creates table column content from closures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@resultBuilder struct TableColumnBuilder<RowValue, Sort> where RowValue : Identifiable, Sort : SortComparator
```

## Overview

The `buildBlock` methods in this type create [TableColumnContent](tablecolumncontent.md) instances based on the number and types of sources provided as parameters.

Don’t use this type directly; instead, SwiftUI annotates the `columns` parameter of the various [Table](table.md) initializers with the `@TableColumnBuilder` annotation, implicitly calling this builder for you.

## Topics

### Building a column

- [buildBlock(_:)](<tablecolumnbuilder/buildblock(__).md>) — Creates a single, unsortable column result.
- [buildBlock(_:_:)](<tablecolumnbuilder/buildblock(____).md>) — Creates an unsortable column result from two sources.
- [buildBlock(_:_:_:)](<tablecolumnbuilder/buildblock(______).md>) — Creates an unsortable column result from three sources.
- [buildBlock(_:_:_:_:)](<tablecolumnbuilder/buildblock(________).md>) — Creates an unsortable column result from four sources.
- [buildBlock(_:_:_:_:_:)](<tablecolumnbuilder/buildblock(__________).md>) — Creates an unsortable column result from five sources.
- [buildBlock(_:_:_:_:_:_:)](<tablecolumnbuilder/buildblock(____________).md>) — Creates an unsortable column result from six sources.
- [buildBlock(_:_:_:_:_:_:_:)](<tablecolumnbuilder/buildblock(______________).md>) — Creates an unsortable column result from seven sources.
- [buildBlock(_:_:_:_:_:_:_:_:)](<tablecolumnbuilder/buildblock(________________).md>) — Creates an unsortable column result from eight sources.
- [buildBlock(_:_:_:_:_:_:_:_:_:)](<tablecolumnbuilder/buildblock(__________________).md>) — Creates an unsortable column result from nine sources.
- [buildBlock(_:_:_:_:_:_:_:_:_:_:)](<tablecolumnbuilder/buildblock(____________________).md>) — Creates an unsortable column result from ten sources.
- [buildExpression(_:)](<tablecolumnbuilder/buildexpression(__).md>) — Creates a generic, unsortable single column expression.

### Supporting types

- [TupleTableColumnContent](tupletablecolumncontent.md) — A type of table column content that creates table columns created from a Swift tuple of table columns.

### Type Methods

- [buildEither(first:)](<tablecolumnbuilder/buildeither(first_).md>) — Creates a column result for the first of two column content alternatives.
- [buildEither(second:)](<tablecolumnbuilder/buildeither(second_).md>) — Creates a row result for the second of two row content alternatives.
- [buildIf(_:)](<tablecolumnbuilder/buildif(__).md>)
- [buildLimitedAvailability(_:)](<tablecolumnbuilder/buildlimitedavailability(__).md>)

## See Also

### Creating columns

- [TableColumn](tablecolumn.md) — A column that displays a view for each row in a table.
- [TableColumnContent](tablecolumncontent.md) — A type used to represent columns within a table.
- [TableColumnAlignment](tablecolumnalignment.md) — Describes the alignment of the content of a table column.
- [TableColumnForEach](tablecolumnforeach.md) — A structure that computes columns on demand from an underlying collection of identified data.

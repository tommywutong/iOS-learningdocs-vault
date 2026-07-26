---
title: TableColumnContent
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tablecolumncontent
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumncontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumncontent.json'
content_hash: 'sha256:c57535efae78bc3d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TableColumnContent

<sub>Protocol</sub>

A type used to represent columns within a table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency protocol TableColumnContent<TableRowValue, TableColumnSortComparator>
```

## Overview

This type provides the body content of the column, as well as the types of the column’s row values and the comparator used to sort rows.

You can factor column content out into separate types or properties, or by creating a custom type conforming to `TableColumnContent`.

```swift
var body: some View {
    Table(people, selection: $selectedPeople, sortOrder: $sortOrder) {
        nameColumns

        TableColumn("Location", value: \.location) {
            LocationView($0.location)
        }
    }
}

@TableColumnBuilder<Person, KeyPathComparator<Person>>
private var nameColumns: some TableColumnContent<
    Person, KeyPathComparator<Person>
> {
    TableColumn("First Name", value: \.firstName) {
        PrimaryColumnView(person: $0)
    }
    TableColumn("Last Name", value: \.lastName)
    TableColumn("Nickname", value: \.nickname)
}
```

The above example factors three table columns into a separate computed property that has an opaque type. The property’s primary associated type `TableRowValue` is a `Person` and its associated type `TableColumnSortComparator` is a key comparator for the `Person` type.

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Relationships

- **Conforming Types**: [Group](group.md), [TableColumn](tablecolumn.md), [TableColumnForEach](tablecolumnforeach.md), [TupleTableColumnContent](tupletablecolumncontent.md)

## Topics

### Getting the column body

- [tableColumnBody](tablecolumncontent/tablecolumnbody-swift.property.md) — The composition of content that comprise the table column content.
- [TableColumnBody](tablecolumncontent/tablecolumnbody-swift.associatedtype.md) — The type of content representing the body of this table column content.

### Defining the row value

- [TableRowValue](tablecolumncontent/tablerowvalue.md) — The type of value of rows presented by this column content.

### Defining the comparator

- [TableColumnSortComparator](tablecolumncontent/tablecolumnsortcomparator.md) — The type of sort comparator associated with this table column content.

### Configuring the content

- [alignment(_:)](<tablecolumncontent/alignment(__).md>) — Sets the alignment of the column, applying to both its column header label and the row view content for that column.
- [customizationID(_:)](<tablecolumncontent/customizationid(__).md>) — Sets the identifier to be associated with a column when persisting its state with `TableColumnCustomization`.
- [defaultVisibility(_:)](<tablecolumncontent/defaultvisibility(__).md>) — Sets the default visibility of a table column.
- [disabledCustomizationBehavior(_:)](<tablecolumncontent/disabledcustomizationbehavior(__).md>) — Sets the disabled customization behavior for a table column.

## See Also

### Creating columns

- [TableColumn](tablecolumn.md) — A column that displays a view for each row in a table.
- [TableColumnAlignment](tablecolumnalignment.md) — Describes the alignment of the content of a table column.
- [TableColumnBuilder](tablecolumnbuilder.md) — A result builder that creates table column content from closures.
- [TableColumnForEach](tablecolumnforeach.md) — A structure that computes columns on demand from an underlying collection of identified data.

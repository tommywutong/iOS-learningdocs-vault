---
title: 'init(_:value:comparator:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.6+, iPadOS 16.6+, Mac Catalyst 16.6+, macOS 13.5+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablecolumn/init(_:value:comparator:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumn/init(_:value:comparator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumn/init%28_%3Avalue%3Acomparator%3A%29.json'
content_hash: 'sha256:0482d76e0032d958'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableColumn](../tablecolumn.md)

# init(_:value:comparator:)

<sub>Initializer</sub>

Creates a sortable column that displays a string property, and generates its label from a localized string resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, String>, comparator: String.StandardComparator = .localizedStandard) where Content == Text
```

## Parameters

- `titleResource` — Text resource for the column’s localized title.

- `value` — The path to the property associated with the column, to display verbatim as text in each row of a table, and the key path used to create a sort comparator when sorting the column.

- `comparator` — The `SortComparator` used to order the string values.

## Discussion

This initializer creates a [Text](../text.md) view for you. For more information about localizing strings, see [Text](../text.md).

## See Also

### Creating a sortable column

- [init(_:value:content:)](<init(__value_content_).md>) — Creates a sortable column for Boolean values that generates its label from a localized string resource.
- [init(_:value:comparator:content:)](<init(__value_comparator_content_).md>) — Creates a sortable column that generates its label from a localized string resource.
- [init(_:sortUsing:content:)](<init(__sortusing_content_).md>) — Creates a sortable column that generates its label from a localized string resource.

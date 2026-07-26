---
title: 'init(_:sortUsing:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.6+, iPadOS 16.6+, Mac Catalyst 16.6+, macOS 13.5+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablecolumn/init(_:sortusing:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumn/init(_:sortusing:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumn/init%28_%3Asortusing%3Acontent%3A%29.json'
content_hash: 'sha256:5e2962bea1691b0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableColumn](../tablecolumn.md)

# init(_:sortUsing:content:)

<sub>Initializer</sub>

Creates a sortable column that generates its label from a localized string resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, sortUsing comparator: Sort, @ContentBuilder content: @escaping (RowValue) -> Content)
```

## Parameters

- `titleResource` — Text resource for the column’s localized title.

- `comparator` — The prototype sort comparator to use when representing this column. When a person taps or clicks the column header, the containing table’s `sortOrder` incorporates this value, potentially with a flipped order.

- `content` — The view content to display for each row in a table.

## Discussion

This initializer creates a [Text](../text.md) view on your behalf. For more information about localizing strings, see[Text](../text.md).

## See Also

### Creating a sortable column

- [init(_:value:content:)](<init(__value_content_).md>) — Creates a sortable column for Boolean values that generates its label from a localized string resource.
- [init(_:value:comparator:)](<init(__value_comparator_).md>) — Creates a sortable column that displays a string property, and generates its label from a localized string resource.
- [init(_:value:comparator:content:)](<init(__value_comparator_content_).md>) — Creates a sortable column that generates its label from a localized string resource.

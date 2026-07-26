---
title: 'init(_:value:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.6+, iPadOS 16.6+, Mac Catalyst 16.6+, macOS 13.5+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablecolumn/init(_:value:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumn/init(_:value:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumn/init%28_%3Avalue%3Acontent%3A%29.json'
content_hash: 'sha256:b79c595982bd003e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableColumn](../tablecolumn.md)

# init(_:value:content:)

<sub>Initializer</sub>

Creates a sortable column for Boolean values that generates its label from a localized string resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, Bool>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

## Parameters

- `titleResource` — The resource for the column’s localized title.

- `value` — The path to the property associated with the column, which will be used to update and reflect the sorting state in a table.

- `content` — The view content to display for each row in a table.

## Discussion

This initializer creates a [Text](../text.md) view on your behalf. See [Text](../text.md) for more information about localizing strings.

## See Also

### Creating a sortable column

- [init(_:value:comparator:)](<init(__value_comparator_).md>) — Creates a sortable column that displays a string property, and generates its label from a localized string resource.
- [init(_:value:comparator:content:)](<init(__value_comparator_content_).md>) — Creates a sortable column that generates its label from a localized string resource.
- [init(_:sortUsing:content:)](<init(__sortusing_content_).md>) — Creates a sortable column that generates its label from a localized string resource.

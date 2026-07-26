---
title: 'init(_:value:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.6+, iPadOS 16.6+, Mac Catalyst 16.6+, macOS 13.5+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablecolumn/init(_:value:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumn/init(_:value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumn/init%28_%3Avalue%3A%29.json'
content_hash: 'sha256:096fcd7fc9193deb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableColumn](../tablecolumn.md)

# init(_:value:)

<sub>Initializer</sub>

Creates an unsortable column that displays a string property that generates its label from a localized string resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, String>) where Content == Text
```

## Parameters

- `titleResource` — Text resource for the column’s localized title.

- `value` — The path to the property associated with the column. The table uses this to display the property as verbatim text in each row of the table.

## Discussion

This initializer creates a [Text](../text.md) view for you. For more information about localizing strings, see [Text](../text.md).

## See Also

### Creating an unsortable column

- [init(_:content:)](<init(__content_).md>) — Creates an unsortable column that generates its label from a localized string resource.

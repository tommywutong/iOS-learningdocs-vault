---
title: 'init(_:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.6+, iPadOS 16.6+, Mac Catalyst 16.6+, macOS 13.5+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablecolumn/init(_:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumn/init(_:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumn/init%28_%3Acontent%3A%29.json'
content_hash: 'sha256:ab6fa51a97a8da7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableColumn](../tablecolumn.md)

# init(_:content:)

<sub>Initializer</sub>

Creates an unsortable column that generates its label from a localized string resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, @ContentBuilder content: @escaping (RowValue) -> Content)
```

## Parameters

- `titleResource` — Text resource for the column’s localized title.

- `content` — The view content to display for each row in a table.

## Discussion

This initializer creates a [Text](../text.md) view for you. For more information about localizing strings, see [Text](../text.md).

## See Also

### Creating an unsortable column

- [init(_:value:)](<init(__value_).md>) — Creates an unsortable column that displays a string property that generates its label from a localized string resource.

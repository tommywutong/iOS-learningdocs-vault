---
title: 'makeBody(configuration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablestyle/makebody(configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablestyle/makebody(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablestyle/makebody%28configuration%3A%29.json'
content_hash: 'sha256:5f18d171d06eafe0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableStyle](../tablestyle.md)

# makeBody(configuration:)

<sub>Instance Method</sub>

Creates a view that represents the body of a table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@ContentBuilder @MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

## Parameters

- `configuration` — The properties of the table.

## Discussion

The system calls this method for each [Table](../table.md) instance in a view hierarchy where this style is the current table style.

## See Also

### Creating custom table styles

- [Configuration](configuration.md) — The properties of a table.
- [Body](body.md) — A view that represents the body of a table.

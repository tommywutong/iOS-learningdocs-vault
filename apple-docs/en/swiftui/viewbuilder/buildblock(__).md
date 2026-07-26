---
title: 'buildBlock(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/viewbuilder/buildblock(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/viewbuilder/buildblock(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/viewbuilder/buildblock%28_%3A%29.json'
content_hash: 'sha256:8918835a981b54fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ViewBuilder](../viewbuilder.md)

# buildBlock(_:)

<sub>Type Method</sub>

Passes a single piece of content written as a child view through unmodified.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func buildBlock<Content>(_ content: Content) -> Content
```

## Discussion

An example of a single item written as child content is `{ Text("Hello") }`.

## See Also

### Building content

- [buildBlock()](<buildblock().md>) — Builds an empty content from a block containing no statements.

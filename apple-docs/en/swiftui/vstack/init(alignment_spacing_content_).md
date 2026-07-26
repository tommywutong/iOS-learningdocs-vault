---
title: 'init(alignment:spacing:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/vstack/init(alignment:spacing:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/vstack/init(alignment:spacing:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/vstack/init%28alignment%3Aspacing%3Acontent%3A%29.json'
content_hash: 'sha256:d0006762468bc6cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VStack](../vstack.md)

# init(alignment:spacing:content:)

<sub>Initializer</sub>

Creates an instance with the given spacing and horizontal alignment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(alignment: HorizontalAlignment = .center, spacing: CGFloat? = nil, @ContentBuilder content: () -> Content)
```

## Parameters

- `alignment` — The guide for aligning the subviews in this stack. This guide has the same vertical screen coordinate for every subview.

- `spacing` — The distance between adjacent subviews, or `nil` if you want the stack to choose a default distance for each pair of subviews.

- `content` — A content builder that creates the content of this stack.

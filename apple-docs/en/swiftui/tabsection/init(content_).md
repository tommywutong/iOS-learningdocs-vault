---
title: 'init(content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tabsection/init(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabsection/init(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabsection/init%28content%3A%29.json'
content_hash: 'sha256:9b034653ffbae658'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabSection](../tabsection.md)

# init(content:)

<sub>Initializer</sub>

Creates a section with the provided section content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(@TabContentBuilder<SelectionValue> content: () -> Content) where Header == EmptyView, Footer == EmptyView
```

## Parameters

- `content` — The section’s content.

## See Also

### Creating a tab section

- [init(_:content:)](<init(__content_).md>) — Creates a section with the provided content.
- [init(content:header:)](<init(content_header_).md>) — Creates a section with a header and the provided section content.

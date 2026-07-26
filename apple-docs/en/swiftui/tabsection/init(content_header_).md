---
title: 'init(content:header:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tabsection/init(content:header:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabsection/init(content:header:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabsection/init%28content%3Aheader%3A%29.json'
content_hash: 'sha256:d24f73d832790777'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabSection](../tabsection.md)

# init(content:header:)

<sub>Initializer</sub>

Creates a section with a header and the provided section content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(@TabContentBuilder<SelectionValue> content: () -> Content, @ContentBuilder header: () -> Header) where Header : View, Footer == EmptyView
```

## Parameters

- `content` — The section’s content.

- `header` — A view to use as the section’s header.

## See Also

### Creating a tab section

- [init(content:)](<init(content_).md>) — Creates a section with the provided section content.
- [init(_:content:)](<init(__content_).md>) — Creates a section with the provided content.

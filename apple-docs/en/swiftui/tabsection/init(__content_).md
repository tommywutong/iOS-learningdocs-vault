---
title: 'init(_:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tabsection/init(_:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabsection/init(_:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabsection/init%28_%3Acontent%3A%29.json'
content_hash: 'sha256:b13a57684ac073c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabSection](../tabsection.md)

# init(_:content:)

<sub>Initializer</sub>

Creates a section with the provided content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) init(_ titleResource: LocalizedStringResource, @TabContentBuilder<SelectionValue> content: () -> Content) where Header == Text, Footer == EmptyView
```

## Parameters

- `titleResource` — The localized string resource label for the section’s header.

- `content` — The section’s content.

## See Also

### Creating a tab section

- [init(content:)](<init(content_).md>) — Creates a section with the provided section content.
- [init(content:header:)](<init(content_header_).md>) — Creates a section with a header and the provided section content.

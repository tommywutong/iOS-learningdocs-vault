---
title: 'init(content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/section/init(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/section/init(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/section/init%28content%3A%29.json'
content_hash: 'sha256:7082e7324f11833a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Section](../section.md)

# init(content:)

<sub>Initializer</sub>

Creates a section with the provided section content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) init(@ContentBuilder content: () -> Content)
```

## Parameters

- `content` — The section’s content.

## See Also

### Creating a section

- [init(_:content:)](<init(__content_).md>) — Creates a section with the provided section content.

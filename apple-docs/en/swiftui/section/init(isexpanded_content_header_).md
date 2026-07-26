---
title: 'init(isExpanded:content:header:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/section/init(isexpanded:content:header:)'
source_url: 'https://developer.apple.com/documentation/swiftui/section/init(isexpanded:content:header:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/section/init%28isexpanded%3Acontent%3Aheader%3A%29.json'
content_hash: 'sha256:6ec26a2f36e57d00'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Section](../section.md)

# init(isExpanded:content:header:)

<sub>Initializer</sub>

Creates a section with the provided section content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) init(isExpanded: Binding<Bool>, @ContentBuilder content: () -> Content, @ContentBuilder header: () -> Parent)
```

## Parameters

- `isExpanded` — A binding to a Boolean value that determines the section’s expansion state (expanded or collapsed).

- `content` — The section’s content.

## See Also

### Controlling collapsibility

- [init(_:isExpanded:content:)](<init(__isexpanded_content_).md>) — Creates a section with the provided section content.

---
title: 'init(_:isExpanded:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/section/init(_:isexpanded:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/section/init(_:isexpanded:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/section/init%28_%3Aisexpanded%3Acontent%3A%29.json'
content_hash: 'sha256:08d12a2f035a44e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Section](../section.md)

# init(_:isExpanded:content:)

<sub>Initializer</sub>

Creates a section with the provided section content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) init(_ titleKey: LocalizedStringKey, isExpanded: Binding<Bool>, @ContentBuilder content: () -> Content)
```

## Parameters

- `titleKey` — The key for the section’s localized title, which describes the contents of the section.

- `isExpanded` — A binding to a Boolean value that determines the section’s expansion state (expanded or collapsed).

- `content` — The section’s content.

## See Also

### Controlling collapsibility

- [init(isExpanded:content:header:)](<init(isexpanded_content_header_).md>) — Creates a section with the provided section content.

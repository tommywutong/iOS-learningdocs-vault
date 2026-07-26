---
title: 'init(content:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/labeledcontent/init(content:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/labeledcontent/init(content:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/labeledcontent/init%28content%3Alabel%3A%29.json'
content_hash: 'sha256:f2467fa1cab548b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LabeledContent](../labeledcontent.md)

# init(content:label:)

<sub>Initializer</sub>

Creates a standard labeled element, with a view that conveys the value of the element and a label.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(@ContentBuilder content: () -> Content, @ContentBuilder label: () -> Label)
```

## Parameters

- `content` — The view that conveys the value of the resulting labeled element.

- `label` — The label that describes the purpose of the result.

## See Also

### Creating labeled content

- [init(_:content:)](<init(__content_).md>) — Creates a labeled view that generates its label from a localized string key.
- [init(_:value:)](<init(__value_).md>) — Creates a labeled informational view.
- [init(_:value:format:)](<init(__value_format_).md>) — Creates a labeled informational view from a formatted value.
- [init(_:)](<init(__).md>) — Creates labeled content based on a labeled content style configuration.

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
doc_path: '/documentation/swiftui/list/init(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/list/init(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/list/init%28content%3A%29.json'
content_hash: 'sha256:5db4dbe4b29fe9aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [List](../list.md)

# init(content:)

<sub>Initializer</sub>

Creates a list with the given content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(@ContentBuilder content: () -> Content)
```

## Parameters

- `content` — The content of the list.

## See Also

### Creating a list from a set of views

- [init(selection:content:)](<init(selection_content_).md>) — Creates a list with the given content that supports selecting a single row that cannot be deselected.

---
title: 'init(selection:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/list/init(selection:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/list/init(selection:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/list/init%28selection%3Acontent%3A%29.json'
content_hash: 'sha256:3008f0c46f648b39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [List](../list.md)

# init(selection:content:)

<sub>Initializer</sub>

Creates a list with the given content that supports selecting a single row that cannot be deselected.

<sub>macOS</sub>

```swift
nonisolated init(selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content)
```

## Parameters

- `selection` — A binding to a selected row.

- `content` — The content of the list.

## See Also

### Creating a list from a set of views

- [init(content:)](<init(content_).md>) — Creates a list with the given content.

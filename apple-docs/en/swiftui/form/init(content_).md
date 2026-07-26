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
doc_path: '/documentation/swiftui/form/init(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/form/init(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/form/init%28content%3A%29.json'
content_hash: 'sha256:2558f091004c27d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Form](../form.md)

# init(content:)

<sub>Initializer</sub>

Creates a form with the provided content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(@ContentBuilder content: () -> Content)
```

## Parameters

- `content` — A [ContentBuilder](../contentbuilder.md) that provides the content for the form.

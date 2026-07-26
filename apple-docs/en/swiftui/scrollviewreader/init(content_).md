---
title: 'init(content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scrollviewreader/init(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scrollviewreader/init(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollviewreader/init%28content%3A%29.json'
content_hash: 'sha256:1c2d394869b21a72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollViewReader](../scrollviewreader.md)

# init(content:)

<sub>Initializer</sub>

Creates an instance that can perform programmatic scrolling of its child scroll views.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(@ContentBuilder content: @escaping (ScrollViewProxy) -> Content)
```

## Parameters

- `content` — The reader’s content, containing one or more scroll views. This content builder receives a [ScrollViewProxy](../scrollviewproxy.md) instance that you use to perform scrolling.

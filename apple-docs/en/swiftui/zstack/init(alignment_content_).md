---
title: 'init(alignment:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/zstack/init(alignment:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/zstack/init(alignment:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/zstack/init%28alignment%3Acontent%3A%29.json'
content_hash: 'sha256:1a2ee55369a6f2b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ZStack](../zstack.md)

# init(alignment:content:)

<sub>Initializer</sub>

Creates an instance with the given alignment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(alignment: Alignment = .center, @ContentBuilder content: () -> Content)
```

## Parameters

- `alignment` — The guide for aligning the subviews in this stack on both the x- and y-axes.

- `content` — A content builder that creates the content of this stack.

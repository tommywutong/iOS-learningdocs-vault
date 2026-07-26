---
title: 'init(alignment:spacing:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/zstack/init(alignment:spacing:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/zstack/init(alignment:spacing:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/zstack/init%28alignment%3Aspacing%3Acontent%3A%29.json'
content_hash: 'sha256:8a28ee28928dd9fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ZStack](../zstack.md)

# init(alignment:spacing:content:)

<sub>Initializer</sub>

Creates an instance with the given spacing and alignment.

<sub>visionOS</sub>

```swift
nonisolated init<V>(alignment: Alignment = .center, spacing: CGFloat?, @ContentBuilder content: () -> V) where Content == ZStackContent3D<V>, V : View
```

## Parameters

- `alignment` — The guide for aligning the subviews in this stack on both the x- and y-axes.

- `spacing` — The distance between adjacent subviews, or `nil` if you want the stack to choose a default distance for each pair of subviews.

- `content` — A content builder that creates the content of this stack.

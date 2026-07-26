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
doc_path: '/documentation/swiftui/group/init(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/group/init(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/group/init%28content%3A%29.json'
content_hash: 'sha256:74a23351d998b56e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Group](../group.md)

# init(content:)

<sub>Initializer</sub>

Creates a group of content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(@ContentBuilder content: () -> Content)
```

## Parameters

- `content` — A [ContentBuilder](../contentbuilder.md) that produces the content to group.

## See Also

### Creating a group

- [init(sections:transform:)](<init(sections_transform_).md>) — Constructs a group from the sections of the given view.
- [init(subviews:transform:)](<init(subviews_transform_).md>) — Constructs a group from the subviews of the given view.

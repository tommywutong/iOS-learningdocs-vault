---
title: 'init(content:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/groupbox/init(content:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/groupbox/init(content:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/groupbox/init%28content%3Alabel%3A%29.json'
content_hash: 'sha256:664f1848204ab52f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GroupBox](../groupbox.md)

# init(content:label:)

<sub>Initializer</sub>

Creates a group box with the provided label and view content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated init(@ContentBuilder content: () -> Content, @ContentBuilder label: () -> Label)
```

## Parameters

- `content` — A [ContentBuilder](../contentbuilder.md) that produces the content for the group box.

- `label` — A [ContentBuilder](../contentbuilder.md) that produces a label for the group box.

## See Also

### Creating a group box

- [init(content:)](<init(content_).md>) — Creates an unlabeled group box with the provided view content.
- [init(_:content:)](<init(__content_).md>) — Creates a group box with the provided view content and title.

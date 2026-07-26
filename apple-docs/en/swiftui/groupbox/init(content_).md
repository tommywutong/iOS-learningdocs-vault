---
title: 'init(content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/groupbox/init(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/groupbox/init(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/groupbox/init%28content%3A%29.json'
content_hash: 'sha256:04e6095791dfd880'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GroupBox](../groupbox.md)

# init(content:)

<sub>Initializer</sub>

Creates an unlabeled group box with the provided view content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init(@ContentBuilder content: () -> Content)
```

## Parameters

- `content` — A [ContentBuilder](../contentbuilder.md) that produces the content for the group box.

## See Also

### Creating a group box

- [init(content:label:)](<init(content_label_).md>) — Creates a group box with the provided label and view content.
- [init(_:content:)](<init(__content_).md>) — Creates a group box with the provided view content and title.

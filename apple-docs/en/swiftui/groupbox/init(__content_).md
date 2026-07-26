---
title: 'init(_:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/groupbox/init(_:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/groupbox/init(_:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/groupbox/init%28_%3Acontent%3A%29.json'
content_hash: 'sha256:4ae49433fd7996ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GroupBox](../groupbox.md)

# init(_:content:)

<sub>Initializer</sub>

Creates a group box with the provided view content and title.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, @ContentBuilder content: () -> Content)
```

## Parameters

- `titleResource` — Text resource for the group box’s title, which describes the content of the group box.

- `content` — A [ContentBuilder](../contentbuilder.md) that produces the content for the group box.

## See Also

### Creating a group box

- [init(content:)](<init(content_).md>) — Creates an unlabeled group box with the provided view content.
- [init(content:label:)](<init(content_label_).md>) — Creates a group box with the provided label and view content.

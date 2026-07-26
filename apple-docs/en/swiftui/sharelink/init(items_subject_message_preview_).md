---
title: 'init(items:subject:message:preview:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/sharelink/init(items:subject:message:preview:)'
source_url: 'https://developer.apple.com/documentation/swiftui/sharelink/init(items:subject:message:preview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sharelink/init%28items%3Asubject%3Amessage%3Apreview%3A%29.json'
content_hash: 'sha256:9d61d44c479a5c5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShareLink](../sharelink.md)

# init(items:subject:message:preview:)

<sub>Initializer</sub>

Creates an instance that presents the share interface.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated init(items: Data, subject: Text? = nil, message: Text? = nil, preview: @escaping (Data.Element) -> SharePreview<PreviewImage, PreviewIcon>)
```

## Parameters

- `items` — The items to share.

- `subject` — A title for the items to show when sharing to activities that support a subject field.

- `message` — A description of the items to show when sharing to activities that support a message field. Activities may support attributed text or HTML strings.

- `preview` — A closure that returns a representation of each item to render in a preview.

## Discussion

Use this initializer when you want the system-standard appearance for `ShareLink`.

## See Also

### Sharing items with a preview

- [init(_:items:subject:message:preview:)](<init(__items_subject_message_preview_).md>) — Creates an instance, with a custom label, that presents the share interface.
- [init(items:subject:message:preview:label:)](<init(items_subject_message_preview_label_).md>) — Creates an instance that presents the share interface.

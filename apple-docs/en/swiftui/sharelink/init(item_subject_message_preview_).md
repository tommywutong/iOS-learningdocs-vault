---
title: 'init(item:subject:message:preview:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/sharelink/init(item:subject:message:preview:)'
source_url: 'https://developer.apple.com/documentation/swiftui/sharelink/init(item:subject:message:preview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sharelink/init%28item%3Asubject%3Amessage%3Apreview%3A%29.json'
content_hash: 'sha256:e2d0b0fdb5deebf4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShareLink](../sharelink.md)

# init(item:subject:message:preview:)

<sub>Initializer</sub>

Creates an instance that presents the share interface.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated init<I>(item: I, subject: Text? = nil, message: Text? = nil, preview: SharePreview<PreviewImage, PreviewIcon>) where Data == CollectionOfOne<I>, I : Transferable
```

## Parameters

- `item` — The item to share.

- `subject` — A title for the item to show when sharing to activities that support a subject field.

- `message` — A description of the item to show when sharing to activities that support a message field. Activities may support attributed text or HTML strings.

- `preview` — A representation of the item to render in a preview.

## Discussion

Use this initializer when you want the system-standard appearance for `ShareLink`.

## See Also

### Sharing an item with a preview

- [init(_:item:subject:message:preview:)](<init(__item_subject_message_preview_).md>) — Creates an instance, with a custom label, that presents the share interface.
- [init(item:subject:message:preview:label:)](<init(item_subject_message_preview_label_).md>) — Creates an instance that presents the share interface.

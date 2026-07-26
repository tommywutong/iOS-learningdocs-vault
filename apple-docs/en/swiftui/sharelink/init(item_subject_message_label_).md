---
title: 'init(item:subject:message:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/sharelink/init(item:subject:message:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/sharelink/init(item:subject:message:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sharelink/init%28item%3Asubject%3Amessage%3Alabel%3A%29.json'
content_hash: 'sha256:cfd3ca11f2654df6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShareLink](../sharelink.md)

# init(item:subject:message:label:)

<sub>Initializer</sub>

Creates an instance that presents the share interface.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated init(item: String, subject: Text? = nil, message: Text? = nil, @ContentBuilder label: () -> Label) where Data == CollectionOfOne<String>
```

## Parameters

- `item` — The item to share.

- `subject` — A title for the item to show when sharing to activities that support a subject field.

- `message` — A description of the item to show when sharing to activities that support a message field. Activities may support attributed text or HTML strings.

- `label` — A content builder that produces a label that describes the share action.

## See Also

### Sharing an item

- [init(item:subject:message:)](<init(item_subject_message_).md>) — Creates an instance that presents the share interface.
- [init(_:item:subject:message:)](<init(__item_subject_message_).md>) — Creates an instance, with a custom label, that presents the share interface.

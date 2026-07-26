---
title: 'init(_:items:subject:message:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/sharelink/init(_:items:subject:message:)'
source_url: 'https://developer.apple.com/documentation/swiftui/sharelink/init(_:items:subject:message:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sharelink/init%28_%3Aitems%3Asubject%3Amessage%3A%29.json'
content_hash: 'sha256:f66d18b81c9abaeb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShareLink](../sharelink.md)

# init(_:items:subject:message:)

<sub>Initializer</sub>

Creates an instance, with a custom label, that presents the share interface.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, items: Data, subject: Text? = nil, message: Text? = nil)
```

## Parameters

- `titleResource` — A resource for the title of the share action.

- `items` — The items to share.

- `subject` — A title for the items to show when sharing to activities that support a subject field.

- `message` — A description of the items to show when sharing to activities that support a message field. Activities may support attributed text or HTML strings.

## See Also

### Sharing items

- [init(items:subject:message:)](<init(items_subject_message_).md>) — Creates an instance that presents the share interface.
- [init(items:subject:message:label:)](<init(items_subject_message_label_).md>) — Creates an instance that presents the share interface.

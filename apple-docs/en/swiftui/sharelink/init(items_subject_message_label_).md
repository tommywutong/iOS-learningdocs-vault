---
title: 'init(items:subject:message:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/sharelink/init(items:subject:message:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/sharelink/init(items:subject:message:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sharelink/init%28items%3Asubject%3Amessage%3Alabel%3A%29.json'
content_hash: 'sha256:ffa9ec71b74a3fae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShareLink](../sharelink.md)

# init(items:subject:message:label:)

<sub>Initializer</sub>

Creates an instance that presents the share interface.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated init(items: Data, subject: Text? = nil, message: Text? = nil, @ContentBuilder label: () -> Label)
```

## Parameters

- `items` — The items to share.

- `subject` — A title for the items to show when sharing to activities that support a subject field.

- `message` — A description of the items to show when sharing to activities that support a message field. Activities may support attributed text or HTML strings.

- `label` — A content builder that produces a label that describes the share action.

## See Also

### Sharing items

- [init(items:subject:message:)](<init(items_subject_message_).md>) — Creates an instance that presents the share interface.
- [init(_:items:subject:message:)](<init(__items_subject_message_).md>) — Creates an instance, with a custom label, that presents the share interface.

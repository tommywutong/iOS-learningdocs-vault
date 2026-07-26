---
title: 'post(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/notificationcenter/post(_:)-7ia4j'
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/post(_:)-7ia4j'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/post%28_%3A%29-7ia4j.json'
content_hash: 'sha256:d6479103b9707bcb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NotificationCenter](../notificationcenter.md)

# post(_:)

<sub>Instance Method</sub>

Posts a given asynchronous message to the notification center.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func post<Message>(_ message: Message) where Message : NotificationCenter.AsyncMessage
```

## Parameters

- `message` — The message to post.

## See Also

### Posting notification messages

- [post(_:subject:)](<post(__subject_)-87dbk.md>) — Posts a given main actor message to the notification center.
- [post(_:)](<post(__)-19s7b.md>) — Posts a given main actor message to the notification center.
- [post(_:subject:)](<post(__subject_)-5271w.md>) — Posts a given asynchronous message to the notification center.

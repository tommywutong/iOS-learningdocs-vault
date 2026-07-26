---
title: 'post(_:subject:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/notificationcenter/post(_:subject:)-5271w'
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/post(_:subject:)-5271w'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/post%28_%3Asubject%3A%29-5271w.json'
content_hash: 'sha256:ff707af1413c7d2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NotificationCenter](../notificationcenter.md)

# post(_:subject:)

<sub>Instance Method</sub>

Posts a given asynchronous message to the notification center.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func post<Message>(_ message: Message, subject: Message.Subject) where Message : NotificationCenter.AsyncMessage, Message.Subject : AnyObject
```

## Parameters

- `message` — The message to post.

- `subject` — The subject instance that corresponds to the message.

## See Also

### Posting notification messages

- [post(_:subject:)](<post(__subject_)-87dbk.md>) — Posts a given main actor message to the notification center.
- [post(_:)](<post(__)-19s7b.md>) — Posts a given main actor message to the notification center.
- [post(_:)](<post(__)-7ia4j.md>) — Posts a given asynchronous message to the notification center.

---
title: 'messages(of:for:bufferSize:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/notificationcenter/messages(of:for:buffersize:)-623kg'
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/messages(of:for:buffersize:)-623kg'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/messages%28of%3Afor%3Abuffersize%3A%29-623kg.json'
content_hash: 'sha256:1dcdc5e172fb120f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NotificationCenter](../notificationcenter.md)

# messages(of:for:bufferSize:)

<sub>Instance Method</sub>

Returns an asynchronous sequence of messages produced by this center for a given subject and message type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func messages<Message>(of subject: Message.Subject? = nil, for messageType: Message.Type, bufferSize limit: Int = 10) -> some Sendable & AsyncSequence<Message, Never> where Message : NotificationCenter.AsyncMessage, Message.Subject : AnyObject

```

## Parameters

- `subject` — The subject to observe. Specify a metatype to observe all values for a given type.

- `messageType` — The message type to be observed.

- `limit` — The maximum number of messages allowed to buffer.

## Return Value

An asynchronous sequence of messages produced by this center.

## See Also

### Receiving notifications as asynchronous sequences

- [messages(of:for:bufferSize:)](<messages(of_for_buffersize_)-4tof0.md>) — Returns an asynchronous sequence of messages produced by this center for a given subject and identifier.
- [messages(of:for:bufferSize:)](<messages(of_for_buffersize_)-1ub69.md>) — Returns an asynchronous sequence of messages produced by this center for a given subject type and identifier.

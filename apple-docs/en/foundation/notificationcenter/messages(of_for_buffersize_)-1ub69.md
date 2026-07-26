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
doc_path: '/documentation/foundation/notificationcenter/messages(of:for:buffersize:)-1ub69'
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/messages(of:for:buffersize:)-1ub69'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/messages%28of%3Afor%3Abuffersize%3A%29-1ub69.json'
content_hash: 'sha256:bd907b9edbcc0014'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NotificationCenter](../notificationcenter.md)

# messages(of:for:bufferSize:)

<sub>Instance Method</sub>

Returns an asynchronous sequence of messages produced by this center for a given subject type and identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func messages<Identifier, Message>(of subject: Message.Subject.Type, for identifier: Identifier, bufferSize limit: Int = 10) -> some Sendable & AsyncSequence<Message, Never> where Identifier : NotificationCenter.MessageIdentifier, Message : NotificationCenter.AsyncMessage, Message == Identifier.MessageType

```

## Parameters

- `subject` — The metatype to observe all values for a given type.

- `identifier` — An identifier representing a specific message type.

- `limit` — The maximum number of messages allowed to buffer.

## Return Value

An asynchronous sequence of messages produced by this center.

## See Also

### Receiving notifications as asynchronous sequences

- [messages(of:for:bufferSize:)](<messages(of_for_buffersize_)-4tof0.md>) — Returns an asynchronous sequence of messages produced by this center for a given subject and identifier.
- [messages(of:for:bufferSize:)](<messages(of_for_buffersize_)-623kg.md>) — Returns an asynchronous sequence of messages produced by this center for a given subject and message type.

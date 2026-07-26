---
title: 'URLSessionWebSocketTask.Message.string(_:)'
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessionwebsockettask/message/string(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/message/string(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionwebsockettask/message/string%28_%3A%29.json'
content_hash: 'sha256:c01abbfc9bb15551'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URLSessionWebSocketTask](../../urlsessionwebsockettask.md) · [Message](../message.md)

# URLSessionWebSocketTask.Message.string(_:)

<sub>Case</sub>

A WebSocket message that contains a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case string(String)
```

## Discussion

The [URLSessionWebSocketTask](../../urlsessionwebsockettask.md) uses UTF-8 encoding to send the message’s string.

## See Also

### Message types

- [URLSessionWebSocketTask.Message.data(_:)](<data(__).md>) — A WebSocket message that contains a block of data.

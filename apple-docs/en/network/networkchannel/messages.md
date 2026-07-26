---
title: messages
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networkchannel/messages
source_url: 'https://developer.apple.com/documentation/network/networkchannel/messages'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/messages.json'
content_hash: 'sha256:1708240f1429e4ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# messages

<sub>Instance Property</sub>

Receive data from a connection as an async stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var messages: AsyncThrowingStream<ApplicationProtocol.Message<ApplicationProtocol.ContentType>, any Error> { get }
```

## Discussion

This may be called before the connection is ready, in which case the receive requests will be enqueued until the connection is ready.

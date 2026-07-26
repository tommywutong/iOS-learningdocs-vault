---
title: 'send(_:type:lastMessage:metadata:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkchannel/send(_:type:lastmessage:metadata:)'
source_url: 'https://developer.apple.com/documentation/network/networkchannel/send(_:type:lastmessage:metadata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/send%28_%3Atype%3Alastmessage%3Ametadata%3A%29.json'
content_hash: 'sha256:3f4e70b5784f6999'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# send(_:type:lastMessage:metadata:)

<sub>Instance Method</sub>

Send data on a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func send<Content>(_ content: Content, type: Int, lastMessage: Bool = false, @ProtocolMetadataBuilder metadata builder: () -> [NWProtocolMetadata] = {[]}) async throws where Content : DataProtocol
```

## Parameters

- `content` — The data to send.

- `type` — The message type.

- `lastMessage` — The last message to send.

- `builder` — A builder for specifying metadata about the content to send.

## Discussion

This may be called before the connection is ready, in which case the send will be enqueued until the connection is ready to send.

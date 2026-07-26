---
title: 'sendIdempotent(_:type:lastMessage:metadata:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkchannel/sendidempotent(_:type:lastmessage:metadata:)'
source_url: 'https://developer.apple.com/documentation/network/networkchannel/sendidempotent(_:type:lastmessage:metadata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/sendidempotent%28_%3Atype%3Alastmessage%3Ametadata%3A%29.json'
content_hash: 'sha256:2040307d9c20bb1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# sendIdempotent(_:type:lastMessage:metadata:)

<sub>Instance Method</sub>

Send idempotent data on a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sendIdempotent<Content>(_ content: Content, type: Int, lastMessage: Bool = false, @ProtocolMetadataBuilder metadata builder: () -> [NWProtocolMetadata] = {[]}) where Content : DataProtocol
```

## Parameters

- `content` — The data to send.

- `type` — The message type.

- `lastMessage` — The last message to send.

- `builder` — A builder for specifying metadata about the content to send.

## Discussion

Idempotent content is allowed to be sent before the connection is ready, and may be replayed across parallel connection attempts. This content can be sent as part of fast-open protocols, which allows the data to be sent out sooner than if it were required to wait for connection establishment.

> [!warning] Warning
> Idempotent content will be replayed multiple times on the network. It may be subject to weaker security protections than non-idempotent content.

Content that needs to be sensitive to sending backpressure should not be considered idempotent.

This may be called before the connection is ready, in which case the send will be enqueued until the connection is ready to send.

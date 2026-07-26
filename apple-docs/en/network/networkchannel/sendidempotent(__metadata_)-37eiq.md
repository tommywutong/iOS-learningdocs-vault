---
title: 'sendIdempotent(_:metadata:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkchannel/sendidempotent(_:metadata:)-37eiq'
source_url: 'https://developer.apple.com/documentation/network/networkchannel/sendidempotent(_:metadata:)-37eiq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/sendidempotent%28_%3Ametadata%3A%29-37eiq.json'
content_hash: 'sha256:c7996508bd563cc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# sendIdempotent(_:metadata:)

<sub>Instance Method</sub>

Send an idempotent text frame on a WebSocket connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sendIdempotent(_ content: String, @ProtocolMetadataBuilder metadata builder: () -> [NWProtocolMetadata] = {[]})
```

## Parameters

- `content` — A string to send.

- `builder` — A builder for specifying metadata about the content to send.

## Discussion

Idempotent content is allowed to be sent before the connection is ready, and may be replayed across parallel connection attempts. This content can be sent as part of fast-open protocols, which allows the data to be sent out sooner than if it were required to wait for connection establishment.

> [!warning] Warning
> Idempotent content will be replayed multiple times on the network. It may be subject to weaker security protections than non-idempotent content.

Content that needs to be sensitive to sending backpressure should not be considered idempotent.

This may be called before the connection is ready, in which case the send will be enqueued until the connection is ready to send.

---
title: 'send(_:lastMessage:metadata:other:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkchannel/send(_:lastmessage:metadata:other:)'
source_url: 'https://developer.apple.com/documentation/network/networkchannel/send(_:lastmessage:metadata:other:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/send%28_%3Alastmessage%3Ametadata%3Aother%3A%29.json'
content_hash: 'sha256:a2406a97c6888d61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# send(_:lastMessage:metadata:other:)

<sub>Instance Method</sub>

Send data on a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func send<T>(_ content: Data, lastMessage: Bool = false, metadata: NWProtocolFramer.Message? = nil, @ProtocolMetadataBuilder other builder: () -> [NWProtocolMetadata] = {[]}) async throws where ApplicationProtocol == Framer<T>, T : FramerProtocol
```

## Parameters

- `content` — The data to send.

- `lastMessage` — The last message to send.

- `metadata` — The metadata about the data being sent.

- `builder` — A builder for specifying metadata about the content to send.

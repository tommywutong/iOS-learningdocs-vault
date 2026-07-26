---
title: 'send(_:metadata:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkchannel/send(_:metadata:)-42nkz'
source_url: 'https://developer.apple.com/documentation/network/networkchannel/send(_:metadata:)-42nkz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/send%28_%3Ametadata%3A%29-42nkz.json'
content_hash: 'sha256:7221cbe5d12da25f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# send(_:metadata:)

<sub>Instance Method</sub>

Send data on a UDP connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func send<Content>(_ content: Content, @ProtocolMetadataBuilder metadata builder: () -> [NWProtocolMetadata] = {[]}) async throws where Content : DataProtocol
```

## Parameters

- `content` — The bytes to send on the connection.

- `builder` — A builder for specifying metadata about the content to send.

## Discussion

This may be called before the connection is ready, in which case the send will be enqueued until the connection is ready to send.

---
title: 'send(_:endOfStream:metadata:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkchannel/send(_:endofstream:metadata:)-79bb6'
source_url: 'https://developer.apple.com/documentation/network/networkchannel/send(_:endofstream:metadata:)-79bb6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/send%28_%3Aendofstream%3Ametadata%3A%29-79bb6.json'
content_hash: 'sha256:4630143df06a6ee1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# send(_:endOfStream:metadata:)

<sub>Instance Method</sub>

Send data on a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func send<Content>(_ content: Content, endOfStream: Bool = false, @ProtocolMetadataBuilder metadata builder: () -> [NWProtocolMetadata] = {[]}) async throws where Content : DataProtocol
```

## Parameters

- `content` — The bytes to send on the connection.

- `endOfStream` — Write-close this stream.

## Discussion

This may be called before the connection is ready, in which case the send will be enqueued until the connection is ready to send.

---
title: 'sendIdempotent(_:endOfStream:metadata:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkchannel/sendidempotent(_:endofstream:metadata:)-4bo5u'
source_url: 'https://developer.apple.com/documentation/network/networkchannel/sendidempotent(_:endofstream:metadata:)-4bo5u'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/sendidempotent%28_%3Aendofstream%3Ametadata%3A%29-4bo5u.json'
content_hash: 'sha256:532925173b5a66cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# sendIdempotent(_:endOfStream:metadata:)

<sub>Instance Method</sub>

Send data idempotently on a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sendIdempotent<Content>(_ content: Content, endOfStream: Bool = false, @ProtocolMetadataBuilder metadata builder: () -> [NWProtocolMetadata] = {[]}) where Content : DataProtocol
```

## Parameters

- `content` — The bytes to send on the connection.

- `endOfStream` — Write-close this stream.

- `builder` — A builder for specifying metadata about the content to send.

## Discussion

This may be called before the connection is ready, in which case the send will be enqueued until the connection is ready to send.

Idempotent content may be sent multiple times when opening up a 0-RTT connection, so there is no completion block

---
title: 'pong(_:metadata:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkchannel/pong(_:metadata:)'
source_url: 'https://developer.apple.com/documentation/network/networkchannel/pong(_:metadata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/pong%28_%3Ametadata%3A%29.json'
content_hash: 'sha256:bc6ecef693704fab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# pong(_:metadata:)

<sub>Instance Method</sub>

Send a pong frame on a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func pong<Content>(_ content: Content? = nil, @ProtocolMetadataBuilder metadata builder: () -> [NWProtocolMetadata] = {[]}) async throws where Content : DataProtocol
```

## Parameters

- `content` — Optional pong data.

- `builder` — A builder for specifying metadata about the content to send.

## Discussion

This may be called before the connection is ready, in which case the send will be enqueued until the connection is ready to send.

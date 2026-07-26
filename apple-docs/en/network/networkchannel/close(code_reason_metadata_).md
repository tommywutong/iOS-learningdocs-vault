---
title: 'close(code:reason:metadata:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkchannel/close(code:reason:metadata:)'
source_url: 'https://developer.apple.com/documentation/network/networkchannel/close(code:reason:metadata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/close%28code%3Areason%3Ametadata%3A%29.json'
content_hash: 'sha256:d04f69cfba85a4df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# close(code:reason:metadata:)

<sub>Instance Method</sub>

Send a WebSocket close frame on a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func close(code: NWProtocolWebSocket.CloseCode = .protocolCode(.normalClosure), reason: String? = nil, @ProtocolMetadataBuilder metadata builder: () -> [NWProtocolMetadata] = {[]}) async throws
```

## Parameters

- `code` — Optional close code. Defaults to normal closure.

- `reason` — Optional reason string containing details about the closure.

- `builder` — A builder for specifying metadata about the content to send.

## Discussion

This may be called before the connection is ready, in which case the send will be enqueued until the connection is ready to send.

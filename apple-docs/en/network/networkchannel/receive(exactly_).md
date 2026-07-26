---
title: 'receive(exactly:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkchannel/receive(exactly:)'
source_url: 'https://developer.apple.com/documentation/network/networkchannel/receive(exactly:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/receive%28exactly%3A%29.json'
content_hash: 'sha256:5fb583ff4fd77b9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# receive(exactly:)

<sub>Instance Method</sub>

Receive data from a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func receive(exactly: Int) async throws -> ApplicationProtocol.Message<Data>
```

## Parameters

- `exactly` — Receive exactly this number of bytes from the connection.

## Discussion

This may be called before the connection is ready, in which case the receive request will be enqueued until the connection is ready.

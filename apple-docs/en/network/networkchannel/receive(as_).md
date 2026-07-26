---
title: 'receive(as:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkchannel/receive(as:)'
source_url: 'https://developer.apple.com/documentation/network/networkchannel/receive(as:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/receive%28as%3A%29.json'
content_hash: 'sha256:bf2c8d558864b404'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# receive(as:)

<sub>Instance Method</sub>

Receive data from a connection as a fixed width integer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func receive<Value>(as type: Value.Type) async throws -> ApplicationProtocol.Message<Value> where Value : NetworkFixedWidthInteger
```

## Parameters

- `type` — The type to use when interpreting the bytes.

## Discussion

This may be called before the connection is ready, in which case the receive request will be enqueued until the connection is ready.

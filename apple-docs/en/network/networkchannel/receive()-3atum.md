---
title: receive()
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networkchannel/receive()-3atum
source_url: 'https://developer.apple.com/documentation/network/networkchannel/receive()-3atum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/receive%28%29-3atum.json'
content_hash: 'sha256:f37d55ff7bc55d35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# receive()

<sub>Instance Method</sub>

Receive data from a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func receive() async throws -> ApplicationProtocol.Message<Data>
```

## Discussion

This may be called before the connection is ready, in which case the receive request will be enqueued until the connection is ready.

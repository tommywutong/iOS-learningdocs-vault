---
title: 'openStream(directionality:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkconnection/openstream(directionality:)'
source_url: 'https://developer.apple.com/documentation/network/networkconnection/openstream(directionality:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkconnection/openstream%28directionality%3A%29.json'
content_hash: 'sha256:772e0c3e3ae06366'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkConnection](../networkconnection.md)

# openStream(directionality:)

<sub>Instance Method</sub>

Initiate a new data stream over QUIC. When invoked with no parameters, the default stream type will be bidirectional. Unidirectional streams can be initiated by setting the optional `bidirectional` parameter to false.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func openStream(directionality: QUICStream.Directionality = .bidirectional) async throws -> QUIC.Stream<QUICStream>
```

## Discussion

This call will start the underlying QUIC connection if it has not been started already and will block until the QUIC connection is ready.

While streams can be cancelled independently of the underlying connection, if the parent NetworkChannel is cancelled or fails, the streams will as well.

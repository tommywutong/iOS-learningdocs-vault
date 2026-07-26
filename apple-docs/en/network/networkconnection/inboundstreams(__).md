---
title: 'inboundStreams(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkconnection/inboundstreams(_:)'
source_url: 'https://developer.apple.com/documentation/network/networkconnection/inboundstreams(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkconnection/inboundstreams%28_%3A%29.json'
content_hash: 'sha256:1d6804e14d5e0aad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkConnection](../networkconnection.md)

# inboundStreams(_:)

<sub>Instance Method</sub>

Handle inbound streams and provide a closure on which callback handlers will be executed. When the `NetworkConnection<QUIC>` state moves to `ready`, the internal listener is registered with the system and can receive incoming streams on the multiplexing instance. `inboundStreams` should only be called once on a `NetworkConnection<QUIC>`, and multiple calls to run will throw an exception.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func inboundStreams(_ handler: @escaping @isolated(any) @Sendable (QUIC.Stream<QUICStream>) async throws -> Void) async throws
```

## Discussion

If the `NetworkConnection<QUIC>` is not started at the time that `inboundStreams` is invoked, it will be started.

The closure inherits the isolation domain of the caller.

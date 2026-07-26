---
title: datagrams
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networkconnection/datagrams
source_url: 'https://developer.apple.com/documentation/network/networkconnection/datagrams'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkconnection/datagrams.json'
content_hash: 'sha256:427d30f13fad0d91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkConnection](../networkconnection.md)

# datagrams

<sub>Instance Property</sub>

Access connection-wide unreliable datagrams over QUIC. Subsequent accesses to this object will return the same reference. All incoming datagrams for the entire QUIC connection will be received on this `SubConnection` once invoked.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var datagrams: QUIC.Datagrams<QUICDatagram> { get async throws }
```

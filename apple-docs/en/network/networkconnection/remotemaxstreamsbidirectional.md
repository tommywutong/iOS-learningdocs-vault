---
title: remoteMaxStreamsBidirectional
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networkconnection/remotemaxstreamsbidirectional
source_url: 'https://developer.apple.com/documentation/network/networkconnection/remotemaxstreamsbidirectional'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkconnection/remotemaxstreamsbidirectional.json'
content_hash: 'sha256:1a387c8c081481c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkConnection](../networkconnection.md)

# remoteMaxStreamsBidirectional

<sub>Instance Property</sub>

Get the maximum number of bidirectional streams advertised by peer that an application is allowed to create.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var remoteMaxStreamsBidirectional: Int { get }
```

## Discussion

Note that while attempts to create streams above this limit will be blocked until the server increases the limit, these blocked attempts will cause a STREAMS_BLOCKED frame to be sent to the server. This informs the server that the client has more streams it would like to create. As a result, the caller should attempt to create streams over this limit if it desires more streams.

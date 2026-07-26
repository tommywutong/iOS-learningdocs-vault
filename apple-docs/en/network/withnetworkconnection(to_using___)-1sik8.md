---
title: 'withNetworkConnection(to:using:_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/withnetworkconnection(to:using:_:)-1sik8'
source_url: 'https://developer.apple.com/documentation/network/withnetworkconnection(to:using:_:)-1sik8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/withnetworkconnection%28to%3Ausing%3A_%3A%29-1sik8.json'
content_hash: 'sha256:d0245e5191efc61e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# withNetworkConnection(to:using:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated(nonsending) func withNetworkConnection<ApplicationProtocol>(to endpoint: NWEndpoint, @ProtocolStackBuilder<ApplicationProtocol> using builder: () -> ApplicationProtocol, _ handler: (NetworkConnection<ApplicationProtocol>) async throws -> Void) async throws where ApplicationProtocol : OneToOneProtocol
```

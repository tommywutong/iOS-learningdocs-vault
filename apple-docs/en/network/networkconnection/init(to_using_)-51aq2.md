---
title: 'init(to:using:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkconnection/init(to:using:)-51aq2'
source_url: 'https://developer.apple.com/documentation/network/networkconnection/init(to:using:)-51aq2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkconnection/init%28to%3Ausing%3A%29-51aq2.json'
content_hash: 'sha256:74fe6ada83fca675'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkConnection](../networkconnection.md)

# init(to:using:)

<sub>Initializer</sub>

Create a new connection to an endpoint, with protocol stack.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(to provider: any Connectable, @ProtocolStackBuilder<ApplicationProtocol> using builder: () -> ApplicationProtocol)
```

---
title: NetworkListener.ServiceRegistrationUpdateHandler
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networklistener/serviceregistrationupdatehandler
source_url: 'https://developer.apple.com/documentation/network/networklistener/serviceregistrationupdatehandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networklistener/serviceregistrationupdatehandler.json'
content_hash: 'sha256:4a34d8d4d108784d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkListener](../networklistener.md)

# NetworkListener.ServiceRegistrationUpdateHandler

<sub>Type Alias</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias ServiceRegistrationUpdateHandler = @isolated(any) @Sendable (NetworkListener<ApplicationProtocol>, NetworkListener<ApplicationProtocol>.ServiceRegistrationChange) -> Void
```

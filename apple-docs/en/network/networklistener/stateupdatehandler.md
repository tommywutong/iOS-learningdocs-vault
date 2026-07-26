---
title: NetworkListener.StateUpdateHandler
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networklistener/stateupdatehandler
source_url: 'https://developer.apple.com/documentation/network/networklistener/stateupdatehandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networklistener/stateupdatehandler.json'
content_hash: 'sha256:eccc3941c24ca5c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkListener](../networklistener.md)

# NetworkListener.StateUpdateHandler

<sub>Type Alias</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias StateUpdateHandler = @isolated(any) @Sendable (NetworkListener<ApplicationProtocol>, NetworkListener<ApplicationProtocol>.State) -> Void
```

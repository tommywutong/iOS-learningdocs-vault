---
title: NetworkBrowser.StateUpdateHandler
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networkbrowser/stateupdatehandler
source_url: 'https://developer.apple.com/documentation/network/networkbrowser/stateupdatehandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkbrowser/stateupdatehandler.json'
content_hash: 'sha256:146d9d5fd86fda64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkBrowser](../networkbrowser.md)

# NetworkBrowser.StateUpdateHandler

<sub>Type Alias</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias StateUpdateHandler = @isolated(any) @Sendable (NetworkBrowser<Provider>, NetworkBrowser<Provider>.State) -> Void
```

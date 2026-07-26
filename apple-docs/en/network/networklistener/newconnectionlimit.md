---
title: newConnectionLimit
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networklistener/newconnectionlimit
source_url: 'https://developer.apple.com/documentation/network/networklistener/newconnectionlimit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networklistener/newconnectionlimit.json'
content_hash: 'sha256:1731e80bcba878ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkListener](../networklistener.md)

# newConnectionLimit

<sub>Instance Property</sub>

Configure the listener’s new connection limit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var newConnectionLimit: Int { get set }
```

## Discussion

Use the value NWListener.InfiniteConnectionLimit to disable connection limits.

If the value is not NWListener.InfiniteConnectionLimit, the value will be decremented by 1 every time a new connection is received. When the value reaches 0, the new connection handler will no longer be invoked until the the limit is increased.

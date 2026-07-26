---
title: 'newConnectionLimit(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networklistener/newconnectionlimit(_:)'
source_url: 'https://developer.apple.com/documentation/network/networklistener/newconnectionlimit(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networklistener/newconnectionlimit%28_%3A%29.json'
content_hash: 'sha256:5a7e23152e38b837'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkListener](../networklistener.md)

# newConnectionLimit(_:)

<sub>Instance Method</sub>

Configure the listener’s new connection limit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func newConnectionLimit(_ limit: Int) -> Self
```

## Parameters

- `limit` — The new connection limit.

## Discussion

Use the value NWListener.InfiniteConnectionLimit to disable connection limits.

If the value is not NWListener.InfiniteConnectionLimit, the value will be decremented by 1 every time a new connection is received. When the value reaches 0, the new connection handler will no longer be invoked until the the limit is increased.

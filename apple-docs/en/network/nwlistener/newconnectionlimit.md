---
title: newConnectionLimit
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwlistener/newconnectionlimit
source_url: 'https://developer.apple.com/documentation/network/nwlistener/newconnectionlimit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwlistener/newconnectionlimit.json'
content_hash: 'sha256:01f3fbd8b6a2ee55'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWListener](../nwlistener.md)

# newConnectionLimit

<sub>Instance Property</sub>

The remaining number of inbound connections to deliver before rejecting connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var newConnectionLimit: Int { get set }
```

## Discussion

When the new connection limit is set to a non-infinite value, it will decrement for every received connection. Once the value hits zero, new connections will be queued and eventually blocked, until you raise the limit. This allows you to limit the rate of inbound connections you handle.

By default, the limit is [InfiniteConnectionLimit](infiniteconnectionlimit.md). When the limit is infinite, it does not decrement but allows all inbound connections.

## See Also

### Receiving Connections

- [newConnectionHandler](newconnectionhandler.md) — A handler that receives inbound connections.
- [InfiniteConnectionLimit](infiniteconnectionlimit.md) — A static value to indicate that inbound connections should not be limited.

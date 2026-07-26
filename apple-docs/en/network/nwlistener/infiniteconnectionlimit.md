---
title: InfiniteConnectionLimit
framework: Network
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwlistener/infiniteconnectionlimit
source_url: 'https://developer.apple.com/documentation/network/nwlistener/infiniteconnectionlimit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwlistener/infiniteconnectionlimit.json'
content_hash: 'sha256:632daa25042dce54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWListener](../nwlistener.md)

# InfiniteConnectionLimit

<sub>Type Property</sub>

A static value to indicate that inbound connections should not be limited.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let InfiniteConnectionLimit: Int
```

## See Also

### Receiving Connections

- [newConnectionHandler](newconnectionhandler.md) — A handler that receives inbound connections.
- [newConnectionLimit](newconnectionlimit.md) — The remaining number of inbound connections to deliver before rejecting connections.

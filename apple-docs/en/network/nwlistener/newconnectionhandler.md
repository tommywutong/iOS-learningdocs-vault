---
title: newConnectionHandler
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwlistener/newconnectionhandler
source_url: 'https://developer.apple.com/documentation/network/nwlistener/newconnectionhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwlistener/newconnectionhandler.json'
content_hash: 'sha256:8b69f159d4b746c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWListener](../nwlistener.md)

# newConnectionHandler

<sub>Instance Property</sub>

A handler that receives inbound connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency final var newConnectionHandler: (@Sendable (NWConnection) -> Void)? { get set }
```

## Discussion

Upon receiving a new connection, you should set update handlers on the connection and start it in order to accept it. If you want to reject the connection, cancel the connection.

## See Also

### Receiving Connections

- [newConnectionLimit](newconnectionlimit.md) — The remaining number of inbound connections to deliver before rejecting connections.
- [InfiniteConnectionLimit](infiniteconnectionlimit.md) — A static value to indicate that inbound connections should not be limited.

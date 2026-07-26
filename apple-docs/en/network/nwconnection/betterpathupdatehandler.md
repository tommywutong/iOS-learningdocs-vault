---
title: betterPathUpdateHandler
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/betterpathupdatehandler
source_url: 'https://developer.apple.com/documentation/network/nwconnection/betterpathupdatehandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/betterpathupdatehandler.json'
content_hash: 'sha256:a295ef312725702d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# betterPathUpdateHandler

<sub>Instance Property</sub>

A handler that receives updates when an alternative network path is preferred over the current path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency final var betterPathUpdateHandler: (@Sendable (Bool) -> Void)? { get set }
```

## Discussion

Better path events are an indication that a more preferable network path is available. If you can migrate your work to a new connection, try establishing a new connection. Once that new connection is ready, cancel the original connection.

## See Also

### Handling Path Updates

- [currentPath](currentpath.md) — The network path the connection is using.
- [pathUpdateHandler](pathupdatehandler.md) — A handler that receives network path updates.
- [viabilityUpdateHandler](viabilityupdatehandler.md) — A handler that receives updates when data can be sent and received.

---
title: pathUpdateHandler
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/pathupdatehandler
source_url: 'https://developer.apple.com/documentation/network/nwconnection/pathupdatehandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/pathupdatehandler.json'
content_hash: 'sha256:c2a375392e0943eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# pathUpdateHandler

<sub>Instance Property</sub>

A handler that receives network path updates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency final var pathUpdateHandler: (@Sendable (NWPath) -> Void)? { get set }
```

## See Also

### Handling Path Updates

- [currentPath](currentpath.md) — The network path the connection is using.
- [viabilityUpdateHandler](viabilityupdatehandler.md) — A handler that receives updates when data can be sent and received.
- [betterPathUpdateHandler](betterpathupdatehandler.md) — A handler that receives updates when an alternative network path is preferred over the current path.

---
title: viabilityUpdateHandler
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/viabilityupdatehandler
source_url: 'https://developer.apple.com/documentation/network/nwconnection/viabilityupdatehandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/viabilityupdatehandler.json'
content_hash: 'sha256:7f1bedba540016cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# viabilityUpdateHandler

<sub>Instance Property</sub>

A handler that receives updates when data can be sent and received.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency final var viabilityUpdateHandler: (@Sendable (Bool) -> Void)? { get set }
```

## See Also

### Handling Path Updates

- [currentPath](currentpath.md) — The network path the connection is using.
- [pathUpdateHandler](pathupdatehandler.md) — A handler that receives network path updates.
- [betterPathUpdateHandler](betterpathupdatehandler.md) — A handler that receives updates when an alternative network path is preferred over the current path.

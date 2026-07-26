---
title: currentPath
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/currentpath
source_url: 'https://developer.apple.com/documentation/network/nwconnection/currentpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/currentpath.json'
content_hash: 'sha256:d81ce43100bbbb37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# currentPath

<sub>Instance Property</sub>

The network path the connection is using.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var currentPath: NWPath? { get }
```

## See Also

### Handling Path Updates

- [pathUpdateHandler](pathupdatehandler.md) — A handler that receives network path updates.
- [viabilityUpdateHandler](viabilityupdatehandler.md) — A handler that receives updates when data can be sent and received.
- [betterPathUpdateHandler](betterpathupdatehandler.md) — A handler that receives updates when an alternative network path is preferred over the current path.

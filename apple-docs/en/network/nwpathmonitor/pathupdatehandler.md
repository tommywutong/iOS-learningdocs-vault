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
doc_path: /documentation/network/nwpathmonitor/pathupdatehandler
source_url: 'https://developer.apple.com/documentation/network/nwpathmonitor/pathupdatehandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwpathmonitor/pathupdatehandler.json'
content_hash: 'sha256:2ae8a21abc389a3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWPathMonitor](../nwpathmonitor.md)

# pathUpdateHandler

<sub>Instance Property</sub>

A handler that receives network path updates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency final var pathUpdateHandler: (@Sendable (NWPath) -> Void)? { get set }
```

## See Also

### Handling Path Updates

- [currentPath](currentpath.md) — The currently available network path observed by the path monitor.

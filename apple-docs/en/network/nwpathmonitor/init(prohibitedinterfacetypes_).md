---
title: 'init(prohibitedInterfaceTypes:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwpathmonitor/init(prohibitedinterfacetypes:)'
source_url: 'https://developer.apple.com/documentation/network/nwpathmonitor/init(prohibitedinterfacetypes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwpathmonitor/init%28prohibitedinterfacetypes%3A%29.json'
content_hash: 'sha256:60f9da38ecb3404d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWPathMonitor](../nwpathmonitor.md)

# init(prohibitedInterfaceTypes:)

<sub>Initializer</sub>

Initializes a path monitor to observe interface types that are not explicitly prohibited.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(prohibitedInterfaceTypes: [NWInterface.InterfaceType])
```

## See Also

### Creating Path Monitors

- [init()](<init().md>) — Initializes a path monitor to observe all available interface types.
- [init(requiredInterfaceType:)](<init(requiredinterfacetype_).md>) — Initializes a path monitor to observe a specific interface type.
- [start(queue:)](<start(queue_).md>) — Starts monitoring path changes, and sets a queue on which to deliver path events.
- [queue](queue.md) — The queue on which path events are delivered.

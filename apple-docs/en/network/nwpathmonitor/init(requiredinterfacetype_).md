---
title: 'init(requiredInterfaceType:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwpathmonitor/init(requiredinterfacetype:)'
source_url: 'https://developer.apple.com/documentation/network/nwpathmonitor/init(requiredinterfacetype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwpathmonitor/init%28requiredinterfacetype%3A%29.json'
content_hash: 'sha256:c56f68751a6fa36b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWPathMonitor](../nwpathmonitor.md)

# init(requiredInterfaceType:)

<sub>Initializer</sub>

Initializes a path monitor to observe a specific interface type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(requiredInterfaceType: NWInterface.InterfaceType)
```

## See Also

### Creating Path Monitors

- [init()](<init().md>) — Initializes a path monitor to observe all available interface types.
- [init(prohibitedInterfaceTypes:)](<init(prohibitedinterfacetypes_).md>) — Initializes a path monitor to observe interface types that are not explicitly prohibited.
- [start(queue:)](<start(queue_).md>) — Starts monitoring path changes, and sets a queue on which to deliver path events.
- [queue](queue.md) — The queue on which path events are delivered.

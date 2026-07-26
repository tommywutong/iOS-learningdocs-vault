---
title: queue
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwpathmonitor/queue
source_url: 'https://developer.apple.com/documentation/network/nwpathmonitor/queue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwpathmonitor/queue.json'
content_hash: 'sha256:c2862910538fb693'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWPathMonitor](../nwpathmonitor.md)

# queue

<sub>Instance Property</sub>

The queue on which path events are delivered.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var queue: DispatchQueue? { get }
```

## See Also

### Creating Path Monitors

- [init()](<init().md>) — Initializes a path monitor to observe all available interface types.
- [init(requiredInterfaceType:)](<init(requiredinterfacetype_).md>) — Initializes a path monitor to observe a specific interface type.
- [init(prohibitedInterfaceTypes:)](<init(prohibitedinterfacetypes_).md>) — Initializes a path monitor to observe interface types that are not explicitly prohibited.
- [start(queue:)](<start(queue_).md>) — Starts monitoring path changes, and sets a queue on which to deliver path events.

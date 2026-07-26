---
title: 'start(queue:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwpathmonitor/start(queue:)'
source_url: 'https://developer.apple.com/documentation/network/nwpathmonitor/start(queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwpathmonitor/start%28queue%3A%29.json'
content_hash: 'sha256:bdd60dd9660e7322'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWPathMonitor](../nwpathmonitor.md)

# start(queue:)

<sub>Instance Method</sub>

Starts monitoring path changes, and sets a queue on which to deliver path events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func start(queue: DispatchQueue)
```

## See Also

### Creating Path Monitors

- [init()](<init().md>) — Initializes a path monitor to observe all available interface types.
- [init(requiredInterfaceType:)](<init(requiredinterfacetype_).md>) — Initializes a path monitor to observe a specific interface type.
- [init(prohibitedInterfaceTypes:)](<init(prohibitedinterfacetypes_).md>) — Initializes a path monitor to observe interface types that are not explicitly prohibited.
- [queue](queue.md) — The queue on which path events are delivered.

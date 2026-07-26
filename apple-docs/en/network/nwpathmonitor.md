---
title: NWPathMonitor
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwpathmonitor
source_url: 'https://developer.apple.com/documentation/network/nwpathmonitor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwpathmonitor.json'
content_hash: 'sha256:3781ef034e0954ff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NWPathMonitor

<sub>Class</sub>

An observer that you use to monitor and react to network changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class NWPathMonitor
```

## Relationships

- **Conforms To**: [AsyncSequence](../swift/asyncsequence.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating Path Monitors

- [init()](<nwpathmonitor/init().md>) — Initializes a path monitor to observe all available interface types.
- [init(requiredInterfaceType:)](<nwpathmonitor/init(requiredinterfacetype_).md>) — Initializes a path monitor to observe a specific interface type.
- [init(prohibitedInterfaceTypes:)](<nwpathmonitor/init(prohibitedinterfacetypes_).md>) — Initializes a path monitor to observe interface types that are not explicitly prohibited.
- [start(queue:)](<nwpathmonitor/start(queue_).md>) — Starts monitoring path changes, and sets a queue on which to deliver path events.
- [queue](nwpathmonitor/queue.md) — The queue on which path events are delivered.

### Handling Path Updates

- [currentPath](nwpathmonitor/currentpath.md) — The currently available network path observed by the path monitor.
- [pathUpdateHandler](nwpathmonitor/pathupdatehandler.md) — A handler that receives network path updates.

### Canceling Path Monitors

- [cancel()](<nwpathmonitor/cancel().md>) — Stops receiving network path updates.

### Structures

- [Iterator](nwpathmonitor/iterator.md)

### Type Properties

- [ethernetChannel](nwpathmonitor/ethernetchannel.md)

## See Also

### Paths and Interfaces

- [NWPath](nwpath.md) — An object that contains information about the properties of the network that a connection uses, or that are available to your app.
- [NWInterface](nwinterface.md) — An interface that a network connection uses to send and receive data.

---
title: stateUpdateHandler
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwlistener/stateupdatehandler
source_url: 'https://developer.apple.com/documentation/network/nwlistener/stateupdatehandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwlistener/stateupdatehandler.json'
content_hash: 'sha256:a9701695bc16b497'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWListener](../nwlistener.md)

# stateUpdateHandler

<sub>Instance Property</sub>

A handler that receives listener state updates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency final var stateUpdateHandler: (@Sendable (NWListener.State) -> Void)? { get set }
```

## See Also

### Creating Listeners

- [init(using:on:)](<init(using_on_).md>) — Initializes a network listener, with an optional local port.
- [start(queue:)](<start(queue_).md>) — Registers for listening, and sets the queue on which all listener events are delivered.
- [State](state-swift.enum.md) — States indicating whether a listener is able to accept incoming connections.
- [port](port.md) — The port on which the listener can accept connections.
- [cancel()](<cancel().md>) — Stops listening for inbound connections.

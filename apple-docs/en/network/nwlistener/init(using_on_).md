---
title: 'init(using:on:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwlistener/init(using:on:)'
source_url: 'https://developer.apple.com/documentation/network/nwlistener/init(using:on:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwlistener/init%28using%3Aon%3A%29.json'
content_hash: 'sha256:0f860de1a08c299d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWListener](../nwlistener.md)

# init(using:on:)

<sub>Initializer</sub>

Initializes a network listener, with an optional local port.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(using: NWParameters, on: NWEndpoint.Port = .any) throws
```

## See Also

### Creating Listeners

- [start(queue:)](<start(queue_).md>) — Registers for listening, and sets the queue on which all listener events are delivered.
- [stateUpdateHandler](stateupdatehandler.md) — A handler that receives listener state updates.
- [State](state-swift.enum.md) — States indicating whether a listener is able to accept incoming connections.
- [port](port.md) — The port on which the listener can accept connections.
- [cancel()](<cancel().md>) — Stops listening for inbound connections.

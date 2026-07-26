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
doc_path: '/documentation/network/nwlistener/start(queue:)'
source_url: 'https://developer.apple.com/documentation/network/nwlistener/start(queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwlistener/start%28queue%3A%29.json'
content_hash: 'sha256:ddc9f95618a90388'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWListener](../nwlistener.md)

# start(queue:)

<sub>Instance Method</sub>

Registers for listening, and sets the queue on which all listener events are delivered.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func start(queue: DispatchQueue)
```

## See Also

### Creating Listeners

- [init(using:on:)](<init(using_on_).md>) — Initializes a network listener, with an optional local port.
- [stateUpdateHandler](stateupdatehandler.md) — A handler that receives listener state updates.
- [State](state-swift.enum.md) — States indicating whether a listener is able to accept incoming connections.
- [port](port.md) — The port on which the listener can accept connections.
- [cancel()](<cancel().md>) — Stops listening for inbound connections.

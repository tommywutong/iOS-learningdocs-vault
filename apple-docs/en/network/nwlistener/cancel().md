---
title: cancel()
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwlistener/cancel()
source_url: 'https://developer.apple.com/documentation/network/nwlistener/cancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwlistener/cancel%28%29.json'
content_hash: 'sha256:ca02c336d0e76398'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWListener](../nwlistener.md)

# cancel()

<sub>Instance Method</sub>

Stops listening for inbound connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func cancel()
```

## See Also

### Creating Listeners

- [init(using:on:)](<init(using_on_).md>) — Initializes a network listener, with an optional local port.
- [start(queue:)](<start(queue_).md>) — Registers for listening, and sets the queue on which all listener events are delivered.
- [stateUpdateHandler](stateupdatehandler.md) — A handler that receives listener state updates.
- [State](state-swift.enum.md) — States indicating whether a listener is able to accept incoming connections.
- [port](port.md) — The port on which the listener can accept connections.

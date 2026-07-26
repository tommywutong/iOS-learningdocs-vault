---
title: NWListener.State
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwlistener/state-swift.enum
source_url: 'https://developer.apple.com/documentation/network/nwlistener/state-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwlistener/state-swift.enum.json'
content_hash: 'sha256:56ae37c4c18cffbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWListener](../nwlistener.md)

# NWListener.State

<sub>Enumeration</sub>

States indicating whether a listener is able to accept incoming connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum State
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### States

- [NWListener.State.setup](state-swift.enum/setup.md) — The listener has been initialized but not started.
- [NWListener.State.waiting(_:)](<state-swift.enum/waiting(__).md>) — The listener is waiting for a network to become available.
- [NWListener.State.ready](state-swift.enum/ready.md) — The listener is running and able to receive incoming connections.
- [NWListener.State.failed(_:)](<state-swift.enum/failed(__).md>) — The listener has encountered a fatal error.
- [NWListener.State.cancelled](state-swift.enum/cancelled.md) — The listener has been canceled.

## See Also

### Creating Listeners

- [init(using:on:)](<init(using_on_).md>) — Initializes a network listener, with an optional local port.
- [start(queue:)](<start(queue_).md>) — Registers for listening, and sets the queue on which all listener events are delivered.
- [stateUpdateHandler](stateupdatehandler.md) — A handler that receives listener state updates.
- [port](port.md) — The port on which the listener can accept connections.
- [cancel()](<cancel().md>) — Stops listening for inbound connections.

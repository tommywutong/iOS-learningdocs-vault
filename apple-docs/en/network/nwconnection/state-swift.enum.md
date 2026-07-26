---
title: NWConnection.State
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/state-swift.enum
source_url: 'https://developer.apple.com/documentation/network/nwconnection/state-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/state-swift.enum.json'
content_hash: 'sha256:879c85d9b33fd650'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# NWConnection.State

<sub>Enumeration</sub>

States indicating whether a connection can be used to send and receive data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum State
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### States

- [NWConnection.State.setup](state-swift.enum/setup.md) — The connection has been initialized but not started.
- [NWConnection.State.waiting(_:)](<state-swift.enum/waiting(__).md>) — The connection is waiting for a network path change.
- [NWConnection.State.preparing](state-swift.enum/preparing.md) — The connection in the process of being established.
- [NWConnection.State.ready](state-swift.enum/ready.md) — The connection is established, and ready to send and receive data.
- [NWConnection.State.failed(_:)](<state-swift.enum/failed(__).md>) — The connection has disconnected or encountered an error.
- [NWConnection.State.cancelled](state-swift.enum/cancelled.md) — The connection has been canceled.

## See Also

### Handling State Updates

- [state](state-swift.property.md) — The current state of the connection.
- [stateUpdateHandler](stateupdatehandler.md) — A handler that receives connection state updates.

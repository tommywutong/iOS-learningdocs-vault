---
title: NWEthernetChannel.State
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwethernetchannel/state-swift.enum
source_url: 'https://developer.apple.com/documentation/network/nwethernetchannel/state-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwethernetchannel/state-swift.enum.json'
content_hash: 'sha256:3b4b242cc9ad6aff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWEthernetChannel](../nwethernetchannel.md)

# NWEthernetChannel.State

<sub>Enumeration</sub>

States indicating whether an Ethernet channel is able to send and receive frames.

<sub>macOS</sub>

```swift
enum State
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### States

- [NWEthernetChannel.State.setup](state-swift.enum/setup.md) — The channel has been initialized but not started.
- [NWEthernetChannel.State.waiting(_:)](<state-swift.enum/waiting(__).md>) — The channel is waiting for its interface to become available.
- [NWEthernetChannel.State.preparing](state-swift.enum/preparing.md) — The channel is registering with the interface.
- [NWEthernetChannel.State.ready](state-swift.enum/ready.md) — The channel is able to send and receive Ethernet frames.
- [NWEthernetChannel.State.failed(_:)](<state-swift.enum/failed(__).md>) — The channel has encountered a fatal error.
- [NWEthernetChannel.State.cancelled](state-swift.enum/cancelled.md) — The channel has been canceled.

## See Also

### Handling State Updates

- [state](state-swift.property.md) — The current state of the channel.
- [stateUpdateHandler](stateupdatehandler.md) — A handler that delivers channel state updates.

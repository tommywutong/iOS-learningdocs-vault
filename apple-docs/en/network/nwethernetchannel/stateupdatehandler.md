---
title: stateUpdateHandler
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwethernetchannel/stateupdatehandler
source_url: 'https://developer.apple.com/documentation/network/nwethernetchannel/stateupdatehandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwethernetchannel/stateupdatehandler.json'
content_hash: 'sha256:842b793069c2285c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWEthernetChannel](../nwethernetchannel.md)

# stateUpdateHandler

<sub>Instance Property</sub>

A handler that delivers channel state updates.

<sub>macOS</sub>

```swift
@preconcurrency final var stateUpdateHandler: (@Sendable (NWEthernetChannel.State) -> Void)? { get set }
```

## See Also

### Handling State Updates

- [state](state-swift.property.md) — The current state of the channel.
- [State](state-swift.enum.md) — States indicating whether an Ethernet channel is able to send and receive frames.

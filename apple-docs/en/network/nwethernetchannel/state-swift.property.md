---
title: state
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwethernetchannel/state-swift.property
source_url: 'https://developer.apple.com/documentation/network/nwethernetchannel/state-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwethernetchannel/state-swift.property.json'
content_hash: 'sha256:5a1c2babbc6de04c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWEthernetChannel](../nwethernetchannel.md)

# state

<sub>Instance Property</sub>

The current state of the channel.

<sub>macOS</sub>

```swift
final var state: NWEthernetChannel.State { get }
```

## See Also

### Handling State Updates

- [State](state-swift.enum.md) — States indicating whether an Ethernet channel is able to send and receive frames.
- [stateUpdateHandler](stateupdatehandler.md) — A handler that delivers channel state updates.

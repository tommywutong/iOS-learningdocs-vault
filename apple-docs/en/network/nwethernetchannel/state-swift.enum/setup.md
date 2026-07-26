---
title: NWEthernetChannel.State.setup
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwethernetchannel/state-swift.enum/setup
source_url: 'https://developer.apple.com/documentation/network/nwethernetchannel/state-swift.enum/setup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwethernetchannel/state-swift.enum/setup.json'
content_hash: 'sha256:35900c0bfb70833f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWEthernetChannel](../../nwethernetchannel.md) · [State](../state-swift.enum.md)

# NWEthernetChannel.State.setup

<sub>Case</sub>

The channel has been initialized but not started.

<sub>macOS</sub>

```swift
case setup
```

## See Also

### States

- [NWEthernetChannel.State.waiting(_:)](<waiting(__).md>) — The channel is waiting for its interface to become available.
- [NWEthernetChannel.State.preparing](preparing.md) — The channel is registering with the interface.
- [NWEthernetChannel.State.ready](ready.md) — The channel is able to send and receive Ethernet frames.
- [NWEthernetChannel.State.failed(_:)](<failed(__).md>) — The channel has encountered a fatal error.
- [NWEthernetChannel.State.cancelled](cancelled.md) — The channel has been canceled.

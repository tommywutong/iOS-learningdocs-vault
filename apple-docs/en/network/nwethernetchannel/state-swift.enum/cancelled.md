---
title: NWEthernetChannel.State.cancelled
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwethernetchannel/state-swift.enum/cancelled
source_url: 'https://developer.apple.com/documentation/network/nwethernetchannel/state-swift.enum/cancelled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwethernetchannel/state-swift.enum/cancelled.json'
content_hash: 'sha256:3cc5b2d4cc3733ea'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWEthernetChannel](../../nwethernetchannel.md) · [State](../state-swift.enum.md)

# NWEthernetChannel.State.cancelled

<sub>Case</sub>

The channel has been canceled.

<sub>macOS</sub>

```swift
case cancelled
```

## See Also

### States

- [NWEthernetChannel.State.setup](setup.md) — The channel has been initialized but not started.
- [NWEthernetChannel.State.waiting(_:)](<waiting(__).md>) — The channel is waiting for its interface to become available.
- [NWEthernetChannel.State.preparing](preparing.md) — The channel is registering with the interface.
- [NWEthernetChannel.State.ready](ready.md) — The channel is able to send and receive Ethernet frames.
- [NWEthernetChannel.State.failed(_:)](<failed(__).md>) — The channel has encountered a fatal error.

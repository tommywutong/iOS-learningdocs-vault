---
title: NWEthernetChannel.State.ready
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwethernetchannel/state-swift.enum/ready
source_url: 'https://developer.apple.com/documentation/network/nwethernetchannel/state-swift.enum/ready'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwethernetchannel/state-swift.enum/ready.json'
content_hash: 'sha256:fe02345b0fa8a34b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWEthernetChannel](../../nwethernetchannel.md) · [State](../state-swift.enum.md)

# NWEthernetChannel.State.ready

<sub>Case</sub>

The channel is able to send and receive Ethernet frames.

<sub>macOS</sub>

```swift
case ready
```

## See Also

### States

- [NWEthernetChannel.State.setup](setup.md) — The channel has been initialized but not started.
- [NWEthernetChannel.State.waiting(_:)](<waiting(__).md>) — The channel is waiting for its interface to become available.
- [NWEthernetChannel.State.preparing](preparing.md) — The channel is registering with the interface.
- [NWEthernetChannel.State.failed(_:)](<failed(__).md>) — The channel has encountered a fatal error.
- [NWEthernetChannel.State.cancelled](cancelled.md) — The channel has been canceled.

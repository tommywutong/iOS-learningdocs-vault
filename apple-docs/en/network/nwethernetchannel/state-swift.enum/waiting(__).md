---
title: 'NWEthernetChannel.State.waiting(_:)'
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwethernetchannel/state-swift.enum/waiting(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwethernetchannel/state-swift.enum/waiting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwethernetchannel/state-swift.enum/waiting%28_%3A%29.json'
content_hash: 'sha256:878f76cf3c8792cf'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWEthernetChannel](../../nwethernetchannel.md) · [State](../state-swift.enum.md)

# NWEthernetChannel.State.waiting(_:)

<sub>Case</sub>

The channel is waiting for its interface to become available.

<sub>macOS</sub>

```swift
case waiting(NWError)
```

## See Also

### States

- [NWEthernetChannel.State.setup](setup.md) — The channel has been initialized but not started.
- [NWEthernetChannel.State.preparing](preparing.md) — The channel is registering with the interface.
- [NWEthernetChannel.State.ready](ready.md) — The channel is able to send and receive Ethernet frames.
- [NWEthernetChannel.State.failed(_:)](<failed(__).md>) — The channel has encountered a fatal error.
- [NWEthernetChannel.State.cancelled](cancelled.md) — The channel has been canceled.

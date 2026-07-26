---
title: 'NWEthernetChannel.State.failed(_:)'
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwethernetchannel/state-swift.enum/failed(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwethernetchannel/state-swift.enum/failed(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwethernetchannel/state-swift.enum/failed%28_%3A%29.json'
content_hash: 'sha256:13e617daae29ac52'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWEthernetChannel](../../nwethernetchannel.md) · [State](../state-swift.enum.md)

# NWEthernetChannel.State.failed(_:)

<sub>Case</sub>

The channel has encountered a fatal error.

<sub>macOS</sub>

```swift
case failed(NWError)
```

## See Also

### States

- [NWEthernetChannel.State.setup](setup.md) — The channel has been initialized but not started.
- [NWEthernetChannel.State.waiting(_:)](<waiting(__).md>) — The channel is waiting for its interface to become available.
- [NWEthernetChannel.State.preparing](preparing.md) — The channel is registering with the interface.
- [NWEthernetChannel.State.ready](ready.md) — The channel is able to send and receive Ethernet frames.
- [NWEthernetChannel.State.cancelled](cancelled.md) — The channel has been canceled.

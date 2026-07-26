---
title: 'init(on:etherType:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwethernetchannel/init(on:ethertype:)'
source_url: 'https://developer.apple.com/documentation/network/nwethernetchannel/init(on:ethertype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwethernetchannel/init%28on%3Aethertype%3A%29.json'
content_hash: 'sha256:16d20c1ed7d39d3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWEthernetChannel](../nwethernetchannel.md)

# init(on:etherType:)

<sub>Initializer</sub>

Initializes an Ethernet channel on a specific interface with a custom Ethernet type.

<sub>macOS</sub>

```swift
init(on interface: NWInterface, etherType: UInt16)
```

## Parameters

- `interface` — The interface on which to send and receive Ethernet frames.

- `etherType` — The custom Ethernet frame type to register for this channel, in host-byte order.

## See Also

### Managing Ethernet Channels

- [start(queue:)](<start(queue_).md>) — Starts the process of registering the channel, and sets the queue on which all channel events are delivered.
- [cancel()](<cancel().md>) — Unregisters the channel from the interface.

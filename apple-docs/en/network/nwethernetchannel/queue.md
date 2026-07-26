---
title: queue
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwethernetchannel/queue
source_url: 'https://developer.apple.com/documentation/network/nwethernetchannel/queue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwethernetchannel/queue.json'
content_hash: 'sha256:6d2e7369ab192a63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWEthernetChannel](../nwethernetchannel.md)

# queue

<sub>Instance Property</sub>

The queue on which channel events will be delivered.

<sub>macOS</sub>

```swift
final var queue: DispatchQueue? { get }
```

## See Also

### Inspecting Ethernet Channels

- [etherType](ethertype.md) — The custom Ethernet type with which the channel was initialized.
- [interface](interface.md) — The interface with which the channel was initialized.

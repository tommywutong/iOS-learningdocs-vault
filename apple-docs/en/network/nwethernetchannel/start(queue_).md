---
title: 'start(queue:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwethernetchannel/start(queue:)'
source_url: 'https://developer.apple.com/documentation/network/nwethernetchannel/start(queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwethernetchannel/start%28queue%3A%29.json'
content_hash: 'sha256:18aa452455b6fd0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWEthernetChannel](../nwethernetchannel.md)

# start(queue:)

<sub>Instance Method</sub>

Starts the process of registering the channel, and sets the queue on which all channel events are delivered.

<sub>macOS</sub>

```swift
final func start(queue: DispatchQueue)
```

## See Also

### Managing Ethernet Channels

- [init(on:etherType:)](<init(on_ethertype_).md>) — Initializes an Ethernet channel on a specific interface with a custom Ethernet type.
- [cancel()](<cancel().md>) — Unregisters the channel from the interface.

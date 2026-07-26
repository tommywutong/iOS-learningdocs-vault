---
title: 'send(content:to:vlanTag:completion:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwethernetchannel/send(content:to:vlantag:completion:)'
source_url: 'https://developer.apple.com/documentation/network/nwethernetchannel/send(content:to:vlantag:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwethernetchannel/send%28content%3Ato%3Avlantag%3Acompletion%3A%29.json'
content_hash: 'sha256:2f3c0c0d8b3b2894'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWEthernetChannel](../nwethernetchannel.md)

# send(content:to:vlanTag:completion:)

<sub>Instance Method</sub>

Sends a single Ethernet frame over a channel to a specific Ethernet address.

<sub>macOS</sub>

```swift
@preconcurrency final func send(content: Data, to remoteAddress: NWEthernetChannel.EthernetAddress, vlanTag: UInt16, completion: @escaping @Sendable (NWError?) -> Void)
```

## See Also

### Sending and Receiving Ethernet Frames

- [receiveHandler](receivehandler.md) — A handler that delivers inbound Ethernet frames.
- [EthernetAddress](ethernetaddress.md) — A 48-bit Ethernet address.

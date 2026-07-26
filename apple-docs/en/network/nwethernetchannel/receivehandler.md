---
title: receiveHandler
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwethernetchannel/receivehandler
source_url: 'https://developer.apple.com/documentation/network/nwethernetchannel/receivehandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwethernetchannel/receivehandler.json'
content_hash: 'sha256:40e6e4ed03474d91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWEthernetChannel](../nwethernetchannel.md)

# receiveHandler

<sub>Instance Property</sub>

A handler that delivers inbound Ethernet frames.

<sub>macOS</sub>

```swift
@preconcurrency final var receiveHandler: (@Sendable (Data, UInt16, NWEthernetChannel.EthernetAddress, NWEthernetChannel.EthernetAddress) -> Void)? { get set }
```

## Discussion

The receive handler only needs to be set once, and will be invoked for each received Ethernet frame.

## See Also

### Sending and Receiving Ethernet Frames

- [send(content:to:vlanTag:completion:)](<send(content_to_vlantag_completion_).md>) — Sends a single Ethernet frame over a channel to a specific Ethernet address.
- [EthernetAddress](ethernetaddress.md) — A 48-bit Ethernet address.

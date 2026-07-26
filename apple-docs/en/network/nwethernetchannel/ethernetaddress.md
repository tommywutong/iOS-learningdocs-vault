---
title: NWEthernetChannel.EthernetAddress
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwethernetchannel/ethernetaddress
source_url: 'https://developer.apple.com/documentation/network/nwethernetchannel/ethernetaddress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwethernetchannel/ethernetaddress.json'
content_hash: 'sha256:88c2a71bdbbabf57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWEthernetChannel](../nwethernetchannel.md)

# NWEthernetChannel.EthernetAddress

<sub>Structure</sub>

A 48-bit Ethernet address.

<sub>macOS</sub>

```swift
struct EthernetAddress
```

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating Addresses

- [init(_:)](<ethernetaddress/init(__)-62x9i.md>) — Initializes an Ethernet address with data.
- [init(_:)](<ethernetaddress/init(__)-1brh7.md>) — Initializes an Ethernet address with a string.

### Inspecting Addresses

- [rawValue](ethernetaddress/rawvalue.md) — The raw data of the Ethernet address.

## See Also

### Sending and Receiving Ethernet Frames

- [send(content:to:vlanTag:completion:)](<send(content_to_vlantag_completion_).md>) — Sends a single Ethernet frame over a channel to a specific Ethernet address.
- [receiveHandler](receivehandler.md) — A handler that delivers inbound Ethernet frames.

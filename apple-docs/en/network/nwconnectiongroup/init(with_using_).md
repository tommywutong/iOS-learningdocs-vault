---
title: 'init(with:using:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwconnectiongroup/init(with:using:)'
source_url: 'https://developer.apple.com/documentation/network/nwconnectiongroup/init(with:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnectiongroup/init%28with%3Ausing%3A%29.json'
content_hash: 'sha256:e794e405d34e8c19'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnectionGroup](../nwconnectiongroup.md)

# init(with:using:)

<sub>Initializer</sub>

Initializes a new connection group with a group identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(with: any NWGroupDescriptor, using: NWParameters)
```

## See Also

### Establishing Group Connectivity

- [NWMulticastGroup](../nwmulticastgroup.md) — A descriptor for a group you use to join an IP multicast group on a local network.
- [NWGroupDescriptor](../nwgroupdescriptor.md) — A protocol that defines a group of endpoints with which you can communicate, such as a multicast group.
- [start(queue:)](<start(queue_).md>) — Joins the group, registers to receive messages, and sets the queue on you handle group events.

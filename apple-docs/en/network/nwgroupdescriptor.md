---
title: NWGroupDescriptor
framework: Network
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwgroupdescriptor
source_url: 'https://developer.apple.com/documentation/network/nwgroupdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwgroupdescriptor.json'
content_hash: 'sha256:50f9558c6ffb3a0d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NWGroupDescriptor

<sub>Protocol</sub>

A protocol that defines a group of endpoints with which you can communicate, such as a multicast group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NWGroupDescriptor : AnyObject, Sendable
```

## Relationships

- **Inherits From**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [NWMulticastGroup](nwmulticastgroup.md), [NWMultiplexGroup](nwmultiplexgroup.md)

## Topics

### Inspecting Groups

- [members](nwgroupdescriptor/members.md) — The set of endpoints that define the connection group.

## See Also

### Establishing Group Connectivity

- [init(with:using:)](<nwconnectiongroup/init(with_using_).md>) — Initializes a new connection group with a group identifier.
- [NWMulticastGroup](nwmulticastgroup.md) — A descriptor for a group you use to join an IP multicast group on a local network.
- [start(queue:)](<nwconnectiongroup/start(queue_).md>) — Joins the group, registers to receive messages, and sets the queue on you handle group events.

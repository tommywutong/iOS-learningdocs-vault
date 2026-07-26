---
title: 'start(queue:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwconnectiongroup/start(queue:)'
source_url: 'https://developer.apple.com/documentation/network/nwconnectiongroup/start(queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnectiongroup/start%28queue%3A%29.json'
content_hash: 'sha256:2e5e79410f51ae15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnectionGroup](../nwconnectiongroup.md)

# start(queue:)

<sub>Instance Method</sub>

Joins the group, registers to receive messages, and sets the queue on you handle group events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func start(queue: DispatchQueue)
```

## See Also

### Establishing Group Connectivity

- [init(with:using:)](<init(with_using_).md>) — Initializes a new connection group with a group identifier.
- [NWMulticastGroup](../nwmulticastgroup.md) — A descriptor for a group you use to join an IP multicast group on a local network.
- [NWGroupDescriptor](../nwgroupdescriptor.md) — A protocol that defines a group of endpoints with which you can communicate, such as a multicast group.

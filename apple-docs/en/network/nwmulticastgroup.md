---
title: NWMulticastGroup
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwmulticastgroup
source_url: 'https://developer.apple.com/documentation/network/nwmulticastgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwmulticastgroup.json'
content_hash: 'sha256:f91385bcd4d797b3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NWMulticastGroup

<sub>Class</sub>

A descriptor for a group you use to join an IP multicast group on a local network.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NWMulticastGroup
```

## Overview

> [!important] Important
> In order to use multicast on iOS, your app will need to have the `com.apple.developer.networking.multicast` entitlement.

## Relationships

- **Conforms To**: [NWGroupDescriptor](nwgroupdescriptor.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Essentials

- [com.apple.developer.networking.multicast](../bundleresources/entitlements/com.apple.developer.networking.multicast.md) — A Boolean value that indicates whether an app can send or receive IP multicast traffic.

### Defining Multicast Groups

- [init(for:from:disableUnicast:)](<nwmulticastgroup/init(for_from_disableunicast_).md>) — Initializes a multicast group with a set of multicast addresses.

### Inspecting Multicast Groups

- [members](nwmulticastgroup/members.md) — The set of IP multicast group addresses that the connection group joins.
- [sourceFilter](nwmulticastgroup/sourcefilter.md) — An optional address endpoint you provide to filter received multicast packets.
- [isUnicastDisabled](nwmulticastgroup/isunicastdisabled.md) — A Boolean that specifies whether the connection group rejects unicast traffic.

## See Also

### Establishing Group Connectivity

- [init(with:using:)](<nwconnectiongroup/init(with_using_).md>) — Initializes a new connection group with a group identifier.
- [NWGroupDescriptor](nwgroupdescriptor.md) — A protocol that defines a group of endpoints with which you can communicate, such as a multicast group.
- [start(queue:)](<nwconnectiongroup/start(queue_).md>) — Joins the group, registers to receive messages, and sets the queue on you handle group events.

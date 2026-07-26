---
title: IPv4Address
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/ipv4address
source_url: 'https://developer.apple.com/documentation/network/ipv4address'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/ipv4address.json'
content_hash: 'sha256:8641f5ed355ae04f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# IPv4Address

<sub>Structure</sub>

A structure containing an IPv4 address.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct IPv4Address
```

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [IPAddress](ipaddress.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating Addresses

- [init(_:)](<ipv4address/init(__).md>) — Initializes an IPv4 address with a string.
- [init(_:_:)](<ipv4address/init(____).md>) — Initializes an IPv4 address with data.

### Inspecting Address Properties

- [rawValue](ipv4address/rawvalue.md) — The raw data of an IPv4 address.
- [interface](ipv4address/interface.md) — The interface associated with this address.
- [isLinkLocal](ipv4address/islinklocal.md) — A Boolean indicating whether this address is in a link-local range.
- [isLoopback](ipv4address/isloopback.md) — A Boolean indicating whether this address is a loopback address for the local device.
- [isMulticast](ipv4address/ismulticast.md) — A Boolean indicating whether this address is a multicast address.

### Setting Well-Known Addresses

- [any](ipv4address/any.md) — The unspecified address (0.0.0.0).
- [broadcast](ipv4address/broadcast.md) — The local broadcast address (255.255.255.255).
- [loopback](ipv4address/loopback.md) — The device’s loopback address (127.0.0.1).
- [allHostsGroup](ipv4address/allhostsgroup.md) — The multicast group for all hosts on the network segment (224.0.0.1).
- [allRoutersGroup](ipv4address/allroutersgroup.md) — The multicast group for all routers on the network segment (224.0.0.2).
- [allReportsGroup](ipv4address/allreportsgroup.md) — The multicast group for all IGMPv3 reports (224.0.0.22).
- [mdnsGroup](ipv4address/mdnsgroup.md) — The multicast group for multicast DNS (224.0.0.251).

## See Also

### Internet Addresses

- [IPAddress](ipaddress.md) — An abstract protocol you use to interact with IP addresses.
- [IPv6Address](ipv6address.md) — A structure containing an IPv6 address.

---
title: IPAddress
framework: Network
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/ipaddress
source_url: 'https://developer.apple.com/documentation/network/ipaddress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/ipaddress.json'
content_hash: 'sha256:8529dcff2be0b750'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# IPAddress

<sub>Protocol</sub>

An abstract protocol you use to interact with IP addresses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol IPAddress : Sendable
```

## Relationships

- **Inherits From**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [IPv4Address](ipv4address.md), [IPv6Address](ipv6address.md)

## Topics

### Creating Addresses

- [init(_:)](<ipaddress/init(__).md>) — Initializes an IP address with a string.
- [init(_:_:)](<ipaddress/init(____).md>) — Initializes an IP address with data.

### Inspecting Address Properties

- [rawValue](ipaddress/rawvalue.md) — The raw data of an IP address.
- [interface](ipaddress/interface.md) — The interface associated with this address, such as the IPv6 scoped interface.
- [isLinkLocal](ipaddress/islinklocal.md) — A Boolean indicating whether this address is in a link-local range.
- [isLoopback](ipaddress/isloopback.md) — A Boolean indicating whether this address is a loopback address for the local device.
- [isMulticast](ipaddress/ismulticast.md) — A Boolean indicating whether this address is a multicast address.

## See Also

### Internet Addresses

- [IPv4Address](ipv4address.md) — A structure containing an IPv4 address.
- [IPv6Address](ipv6address.md) — A structure containing an IPv6 address.

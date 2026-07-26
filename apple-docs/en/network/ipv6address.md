---
title: IPv6Address
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/ipv6address
source_url: 'https://developer.apple.com/documentation/network/ipv6address'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/ipv6address.json'
content_hash: 'sha256:b0e1fe9c506c3b29'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# IPv6Address

<sub>Structure</sub>

A structure containing an IPv6 address.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct IPv6Address
```

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [IPAddress](ipaddress.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating Addresses

- [init(_:)](<ipv6address/init(__).md>) — Initializes an IPv6 address with a string.
- [init(_:_:)](<ipv6address/init(____).md>) — Initializes an IPv6 address with data.
- [asIPv4](ipv6address/asipv4.md) — Extracts the IPv4 address contained within the IPv6 address, if the IPv6 address is an IPv4-mapped or IPv4-compatible address.

### Inspecting Address Properties

- [rawValue](ipv6address/rawvalue.md) — The raw data of an IPv6 address.
- [interface](ipv6address/interface.md) — The IPv6 scoped interface associated with this address.
- [multicastScope](ipv6address/multicastscope.md) — The IPv6 multicast scope of the address.
- [Scope](ipv6address/scope.md) — An IPv6 multicast scope.
- [isAny](ipv6address/isany.md) — A Boolean indicating whether the address is the unspecified address (::).
- [is6to4](ipv6address/is6to4.md) — A Boolean indicating whether the address is a 6to4 address.
- [isIPv4Compatabile](ipv6address/isipv4compatabile.md) — A Boolean indicating whether the address is IPv4-compatible.
- [isIPv4Mapped](ipv6address/isipv4mapped.md) — A Boolean indicating whether the address is an IPv4-mapped address.
- [isLinkLocal](ipv6address/islinklocal.md) — A Boolean indicating whether this address is in a link-local range.
- [isLoopback](ipv6address/isloopback.md) — A Boolean indicating whether this address is a loopback address for the local device.
- [isMulticast](ipv6address/ismulticast.md) — A Boolean indicating whether this address is a multicast address.

### Setting Well-Known Addresses

- [any](ipv6address/any.md) — The unspecified address (::).
- [broadcast](ipv6address/broadcast.md) — The unspecified broadcast address (::).
- [loopback](ipv6address/loopback.md) — The device’s loopback address (::1).
- [nodeLocalNodes](ipv6address/nodelocalnodes.md) — The multicast address for all local nodes (ff01::1).
- [linkLocalNodes](ipv6address/linklocalnodes.md) — The multicast address for all link-local nodes (ff02::1).
- [linkLocalRouters](ipv6address/linklocalrouters.md) — The multicast address for all link-local routers (ff02::2).

### Instance Properties

- [isUniqueLocal](ipv6address/isuniquelocal.md)

## See Also

### Internet Addresses

- [IPAddress](ipaddress.md) — An abstract protocol you use to interact with IP addresses.
- [IPv4Address](ipv4address.md) — A structure containing an IPv4 address.

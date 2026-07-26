---
title: isIPv4Mapped
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/ipv6address/isipv4mapped
source_url: 'https://developer.apple.com/documentation/network/ipv6address/isipv4mapped'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/ipv6address/isipv4mapped.json'
content_hash: 'sha256:8461fed1fa24dd13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [IPv6Address](../ipv6address.md)

# isIPv4Mapped

<sub>Instance Property</sub>

A Boolean indicating whether the address is an IPv4-mapped address.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isIPv4Mapped: Bool { get }
```

## See Also

### Inspecting Address Properties

- [rawValue](rawvalue.md) — The raw data of an IPv6 address.
- [interface](interface.md) — The IPv6 scoped interface associated with this address.
- [multicastScope](multicastscope.md) — The IPv6 multicast scope of the address.
- [Scope](scope.md) — An IPv6 multicast scope.
- [isAny](isany.md) — A Boolean indicating whether the address is the unspecified address (::).
- [is6to4](is6to4.md) — A Boolean indicating whether the address is a 6to4 address.
- [isIPv4Compatabile](isipv4compatabile.md) — A Boolean indicating whether the address is IPv4-compatible.
- [isLinkLocal](islinklocal.md) — A Boolean indicating whether this address is in a link-local range.
- [isLoopback](isloopback.md) — A Boolean indicating whether this address is a loopback address for the local device.
- [isMulticast](ismulticast.md) — A Boolean indicating whether this address is a multicast address.

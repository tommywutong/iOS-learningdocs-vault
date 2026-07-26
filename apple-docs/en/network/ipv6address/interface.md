---
title: interface
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/ipv6address/interface
source_url: 'https://developer.apple.com/documentation/network/ipv6address/interface'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/ipv6address/interface.json'
content_hash: 'sha256:9672b8d05afcecc2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [IPv6Address](../ipv6address.md)

# interface

<sub>Instance Property</sub>

The IPv6 scoped interface associated with this address.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let interface: NWInterface?
```

## See Also

### Inspecting Address Properties

- [rawValue](rawvalue.md) — The raw data of an IPv6 address.
- [multicastScope](multicastscope.md) — The IPv6 multicast scope of the address.
- [Scope](scope.md) — An IPv6 multicast scope.
- [isAny](isany.md) — A Boolean indicating whether the address is the unspecified address (::).
- [is6to4](is6to4.md) — A Boolean indicating whether the address is a 6to4 address.
- [isIPv4Compatabile](isipv4compatabile.md) — A Boolean indicating whether the address is IPv4-compatible.
- [isIPv4Mapped](isipv4mapped.md) — A Boolean indicating whether the address is an IPv4-mapped address.
- [isLinkLocal](islinklocal.md) — A Boolean indicating whether this address is in a link-local range.
- [isLoopback](isloopback.md) — A Boolean indicating whether this address is a loopback address for the local device.
- [isMulticast](ismulticast.md) — A Boolean indicating whether this address is a multicast address.

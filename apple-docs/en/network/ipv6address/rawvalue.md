---
title: rawValue
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/ipv6address/rawvalue
source_url: 'https://developer.apple.com/documentation/network/ipv6address/rawvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/ipv6address/rawvalue.json'
content_hash: 'sha256:4968332ab5ae96cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [IPv6Address](../ipv6address.md)

# rawValue

<sub>Instance Property</sub>

The raw data of an IPv6 address.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var rawValue: Data { get }
```

## See Also

### Inspecting Address Properties

- [interface](interface.md) — The IPv6 scoped interface associated with this address.
- [multicastScope](multicastscope.md) — The IPv6 multicast scope of the address.
- [Scope](scope.md) — An IPv6 multicast scope.
- [isAny](isany.md) — A Boolean indicating whether the address is the unspecified address (::).
- [is6to4](is6to4.md) — A Boolean indicating whether the address is a 6to4 address.
- [isIPv4Compatabile](isipv4compatabile.md) — A Boolean indicating whether the address is IPv4-compatible.
- [isIPv4Mapped](isipv4mapped.md) — A Boolean indicating whether the address is an IPv4-mapped address.
- [isLinkLocal](islinklocal.md) — A Boolean indicating whether this address is in a link-local range.
- [isLoopback](isloopback.md) — A Boolean indicating whether this address is a loopback address for the local device.
- [isMulticast](ismulticast.md) — A Boolean indicating whether this address is a multicast address.

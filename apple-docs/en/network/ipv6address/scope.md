---
title: IPv6Address.Scope
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/ipv6address/scope
source_url: 'https://developer.apple.com/documentation/network/ipv6address/scope'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/ipv6address/scope.json'
content_hash: 'sha256:bed57b269e9f0b10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [IPv6Address](../ipv6address.md)

# IPv6Address.Scope

<sub>Enumeration</sub>

An IPv6 multicast scope.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Scope
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md)

## Topics

### Scope Values

- [IPv6Address.Scope.nodeLocal](scope/nodelocal.md) — The node-local multicast scope.
- [IPv6Address.Scope.linkLocal](scope/linklocal.md) — The link-local multicast scope.
- [IPv6Address.Scope.siteLocal](scope/sitelocal.md) — The site-local multicast scope.
- [IPv6Address.Scope.organizationLocal](scope/organizationlocal.md) — The organization-local multicast scope.
- [IPv6Address.Scope.global](scope/global.md) — The global multicast scope.

## See Also

### Inspecting Address Properties

- [rawValue](rawvalue.md) — The raw data of an IPv6 address.
- [interface](interface.md) — The IPv6 scoped interface associated with this address.
- [multicastScope](multicastscope.md) — The IPv6 multicast scope of the address.
- [isAny](isany.md) — A Boolean indicating whether the address is the unspecified address (::).
- [is6to4](is6to4.md) — A Boolean indicating whether the address is a 6to4 address.
- [isIPv4Compatabile](isipv4compatabile.md) — A Boolean indicating whether the address is IPv4-compatible.
- [isIPv4Mapped](isipv4mapped.md) — A Boolean indicating whether the address is an IPv4-mapped address.
- [isLinkLocal](islinklocal.md) — A Boolean indicating whether this address is in a link-local range.
- [isLoopback](isloopback.md) — A Boolean indicating whether this address is a loopback address for the local device.
- [isMulticast](ismulticast.md) — A Boolean indicating whether this address is a multicast address.

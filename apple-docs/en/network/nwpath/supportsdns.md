---
title: supportsDNS
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwpath/supportsdns
source_url: 'https://developer.apple.com/documentation/network/nwpath/supportsdns'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwpath/supportsdns.json'
content_hash: 'sha256:d45393845099fb92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWPath](../nwpath.md)

# supportsDNS

<sub>Instance Property</sub>

A Boolean indicating whether the path has a DNS server configured.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let supportsDNS: Bool
```

## See Also

### Checking Path Capabilities

- [supportsIPv4](supportsipv4.md) — A Boolean indicating whether the path can route IPv4 traffic.
- [supportsIPv6](supportsipv6.md) — A Boolean indicating whether the path can route IPv6 traffic.
- [isConstrained](isconstrained.md) — A Boolean indicating whether the path uses an interface in Low Data Mode.
- [isExpensive](isexpensive.md) — A Boolean indicating whether the path uses an interface that is considered expensive, such as Cellular or a Personal Hotspot.

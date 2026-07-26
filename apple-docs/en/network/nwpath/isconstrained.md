---
title: isConstrained
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwpath/isconstrained
source_url: 'https://developer.apple.com/documentation/network/nwpath/isconstrained'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwpath/isconstrained.json'
content_hash: 'sha256:b025b7872a1537bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWPath](../nwpath.md)

# isConstrained

<sub>Instance Property</sub>

A Boolean indicating whether the path uses an interface in Low Data Mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isConstrained: Bool { get }
```

## See Also

### Checking Path Capabilities

- [supportsIPv4](supportsipv4.md) — A Boolean indicating whether the path can route IPv4 traffic.
- [supportsIPv6](supportsipv6.md) — A Boolean indicating whether the path can route IPv6 traffic.
- [supportsDNS](supportsdns.md) — A Boolean indicating whether the path has a DNS server configured.
- [isExpensive](isexpensive.md) — A Boolean indicating whether the path uses an interface that is considered expensive, such as Cellular or a Personal Hotspot.

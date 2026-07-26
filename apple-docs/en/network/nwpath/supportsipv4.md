---
title: supportsIPv4
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwpath/supportsipv4
source_url: 'https://developer.apple.com/documentation/network/nwpath/supportsipv4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwpath/supportsipv4.json'
content_hash: 'sha256:5055546f529431c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWPath](../nwpath.md)

# supportsIPv4

<sub>Instance Property</sub>

A Boolean indicating whether the path can route IPv4 traffic.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let supportsIPv4: Bool
```

## See Also

### Checking Path Capabilities

- [supportsIPv6](supportsipv6.md) — A Boolean indicating whether the path can route IPv6 traffic.
- [supportsDNS](supportsdns.md) — A Boolean indicating whether the path has a DNS server configured.
- [isConstrained](isconstrained.md) — A Boolean indicating whether the path uses an interface in Low Data Mode.
- [isExpensive](isexpensive.md) — A Boolean indicating whether the path uses an interface that is considered expensive, such as Cellular or a Personal Hotspot.

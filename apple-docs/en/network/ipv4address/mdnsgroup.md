---
title: mdnsGroup
framework: Network
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/ipv4address/mdnsgroup
source_url: 'https://developer.apple.com/documentation/network/ipv4address/mdnsgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/ipv4address/mdnsgroup.json'
content_hash: 'sha256:5fc2ae61b80cf54e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [IPv4Address](../ipv4address.md)

# mdnsGroup

<sub>Type Property</sub>

The multicast group for multicast DNS (224.0.0.251).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let mdnsGroup: IPv4Address
```

## See Also

### Setting Well-Known Addresses

- [any](any.md) — The unspecified address (0.0.0.0).
- [broadcast](broadcast.md) — The local broadcast address (255.255.255.255).
- [loopback](loopback.md) — The device’s loopback address (127.0.0.1).
- [allHostsGroup](allhostsgroup.md) — The multicast group for all hosts on the network segment (224.0.0.1).
- [allRoutersGroup](allroutersgroup.md) — The multicast group for all routers on the network segment (224.0.0.2).
- [allReportsGroup](allreportsgroup.md) — The multicast group for all IGMPv3 reports (224.0.0.22).

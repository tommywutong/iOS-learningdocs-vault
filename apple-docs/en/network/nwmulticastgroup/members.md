---
title: members
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwmulticastgroup/members
source_url: 'https://developer.apple.com/documentation/network/nwmulticastgroup/members'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwmulticastgroup/members.json'
content_hash: 'sha256:5291a23e1dc1c04d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWMulticastGroup](../nwmulticastgroup.md)

# members

<sub>Instance Property</sub>

The set of IP multicast group addresses that the connection group joins.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var members: [NWEndpoint] { get }
```

## See Also

### Inspecting Multicast Groups

- [sourceFilter](sourcefilter.md) — An optional address endpoint you provide to filter received multicast packets.
- [isUnicastDisabled](isunicastdisabled.md) — A Boolean that specifies whether the connection group rejects unicast traffic.

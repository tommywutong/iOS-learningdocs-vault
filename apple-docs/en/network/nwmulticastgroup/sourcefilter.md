---
title: sourceFilter
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwmulticastgroup/sourcefilter
source_url: 'https://developer.apple.com/documentation/network/nwmulticastgroup/sourcefilter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwmulticastgroup/sourcefilter.json'
content_hash: 'sha256:7f856fe9a3f1576d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWMulticastGroup](../nwmulticastgroup.md)

# sourceFilter

<sub>Instance Property</sub>

An optional address endpoint you provide to filter received multicast packets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final let sourceFilter: NWEndpoint?
```

## See Also

### Inspecting Multicast Groups

- [members](members.md) — The set of IP multicast group addresses that the connection group joins.
- [isUnicastDisabled](isunicastdisabled.md) — A Boolean that specifies whether the connection group rejects unicast traffic.

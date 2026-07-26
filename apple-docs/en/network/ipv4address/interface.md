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
doc_path: /documentation/network/ipv4address/interface
source_url: 'https://developer.apple.com/documentation/network/ipv4address/interface'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/ipv4address/interface.json'
content_hash: 'sha256:68d2f6cba93d384d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [IPv4Address](../ipv4address.md)

# interface

<sub>Instance Property</sub>

The interface associated with this address.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let interface: NWInterface?
```

## See Also

### Inspecting Address Properties

- [rawValue](rawvalue.md) — The raw data of an IPv4 address.
- [isLinkLocal](islinklocal.md) — A Boolean indicating whether this address is in a link-local range.
- [isLoopback](isloopback.md) — A Boolean indicating whether this address is a loopback address for the local device.
- [isMulticast](ismulticast.md) — A Boolean indicating whether this address is a multicast address.

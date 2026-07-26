---
title: isLoopback
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/ipaddress/isloopback
source_url: 'https://developer.apple.com/documentation/network/ipaddress/isloopback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/ipaddress/isloopback.json'
content_hash: 'sha256:a3af1d6d8d62ac67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [IPAddress](../ipaddress.md)

# isLoopback

<sub>Instance Property</sub>

A Boolean indicating whether this address is a loopback address for the local device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isLoopback: Bool { get }
```

## See Also

### Inspecting Address Properties

- [rawValue](rawvalue.md) — The raw data of an IP address.
- [interface](interface.md) — The interface associated with this address, such as the IPv6 scoped interface.
- [isLinkLocal](islinklocal.md) — A Boolean indicating whether this address is in a link-local range.
- [isMulticast](ismulticast.md) — A Boolean indicating whether this address is a multicast address.

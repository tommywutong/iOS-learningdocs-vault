---
title: loopback
framework: Network
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/ipv6address/loopback
source_url: 'https://developer.apple.com/documentation/network/ipv6address/loopback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/ipv6address/loopback.json'
content_hash: 'sha256:b6ccfe137af47939'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [IPv6Address](../ipv6address.md)

# loopback

<sub>Type Property</sub>

The device’s loopback address (::1).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let loopback: IPv6Address
```

## See Also

### Setting Well-Known Addresses

- [any](any.md) — The unspecified address (::).
- [broadcast](broadcast.md) — The unspecified broadcast address (::).
- [nodeLocalNodes](nodelocalnodes.md) — The multicast address for all local nodes (ff01::1).
- [linkLocalNodes](linklocalnodes.md) — The multicast address for all link-local nodes (ff02::1).
- [linkLocalRouters](linklocalrouters.md) — The multicast address for all link-local routers (ff02::2).

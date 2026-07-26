---
title: 'init(_:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/ipv6address/init(_:)'
source_url: 'https://developer.apple.com/documentation/network/ipv6address/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/ipv6address/init%28_%3A%29.json'
content_hash: 'sha256:4839c6b5e5cf0f14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [IPv6Address](../ipv6address.md)

# init(_:)

<sub>Initializer</sub>

Initializes an IPv6 address with a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(_ string: String)
```

## Discussion

The provided string will be interpreted as an IPv6 address. If the string cannot be interpreted as an IPv6 address, the initialization will fail.

## See Also

### Creating Addresses

- [init(_:_:)](<init(____).md>) — Initializes an IPv6 address with data.
- [asIPv4](asipv4.md) — Extracts the IPv4 address contained within the IPv6 address, if the IPv6 address is an IPv4-mapped or IPv4-compatible address.

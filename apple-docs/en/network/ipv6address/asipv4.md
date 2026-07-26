---
title: asIPv4
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/ipv6address/asipv4
source_url: 'https://developer.apple.com/documentation/network/ipv6address/asipv4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/ipv6address/asipv4.json'
content_hash: 'sha256:3240c095d0f8e379'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [IPv6Address](../ipv6address.md)

# asIPv4

<sub>Instance Property</sub>

Extracts the IPv4 address contained within the IPv6 address, if the IPv6 address is an IPv4-mapped or IPv4-compatible address.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var asIPv4: IPv4Address? { get }
```

## See Also

### Creating Addresses

- [init(_:)](<init(__).md>) — Initializes an IPv6 address with a string.
- [init(_:_:)](<init(____).md>) — Initializes an IPv6 address with data.

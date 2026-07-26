---
title: 'init(_:_:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/ipv6address/init(_:_:)'
source_url: 'https://developer.apple.com/documentation/network/ipv6address/init(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/ipv6address/init%28_%3A_%3A%29.json'
content_hash: 'sha256:0d016da2e7c716d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [IPv6Address](../ipv6address.md)

# init(_:_:)

<sub>Initializer</sub>

Initializes an IPv6 address with data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(_ rawValue: Data, _ interface: NWInterface? = nil)
```

## Discussion

The provided data is expected to be an IPv6 address of 16 bytes.

## See Also

### Creating Addresses

- [init(_:)](<init(__).md>) — Initializes an IPv6 address with a string.
- [asIPv4](asipv4.md) — Extracts the IPv4 address contained within the IPv6 address, if the IPv6 address is an IPv4-mapped or IPv4-compatible address.

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
doc_path: '/documentation/network/ipaddress/init(_:_:)'
source_url: 'https://developer.apple.com/documentation/network/ipaddress/init(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/ipaddress/init%28_%3A_%3A%29.json'
content_hash: 'sha256:3940c9dd35d67c07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [IPAddress](../ipaddress.md)

# init(_:_:)

<sub>Initializer</sub>

Initializes an IP address with data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(_ rawValue: Data, _ interface: NWInterface?)
```

## Discussion

The provided data is expected to be either an IPv4 address of 4 bytes or an IPv6 address of 16 bytes.

## See Also

### Creating Addresses

- [init(_:)](<init(__).md>) — Initializes an IP address with a string.

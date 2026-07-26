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
doc_path: '/documentation/network/ipaddress/init(_:)'
source_url: 'https://developer.apple.com/documentation/network/ipaddress/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/ipaddress/init%28_%3A%29.json'
content_hash: 'sha256:69452ac06498db02'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [IPAddress](../ipaddress.md)

# init(_:)

<sub>Initializer</sub>

Initializes an IP address with a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(_ string: String)
```

## Discussion

The provided string will be interpreted as an IPv4 or IPv6 address. If the string cannot be interpreted as an address, the initialization will fail.

## See Also

### Creating Addresses

- [init(_:_:)](<init(____).md>) — Initializes an IP address with data.

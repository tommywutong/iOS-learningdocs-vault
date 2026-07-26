---
title: 'hopLimit(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/ip/hoplimit(_:)'
source_url: 'https://developer.apple.com/documentation/network/ip/hoplimit(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/ip/hoplimit%28_%3A%29.json'
content_hash: 'sha256:e1f1d11878248121'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [IP](../ip.md)

# hopLimit(_:)

<sub>Instance Method</sub>

Configure the IP hop limit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hopLimit(_ limit: UInt8) -> IP
```

## Parameters

- `limit` — The hop limit.

## Discussion

Equivalent to `IP_TTL` for IPv4 and `IPV6_HOPLIMIT` for IPv6.

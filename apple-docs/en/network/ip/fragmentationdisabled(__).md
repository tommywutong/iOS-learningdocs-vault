---
title: 'fragmentationDisabled(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/ip/fragmentationdisabled(_:)'
source_url: 'https://developer.apple.com/documentation/network/ip/fragmentationdisabled(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/ip/fragmentationdisabled%28_%3A%29.json'
content_hash: 'sha256:934aa344291d4891'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [IP](../ip.md)

# fragmentationDisabled(_:)

<sub>Instance Method</sub>

Configure IP to disable fragmentation on outgoing packets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func fragmentationDisabled(_ dontFragment: Bool) -> IP
```

## Parameters

- `dontFragment` — True to disable fragmentation, false otherwise.

## Discussion

Equivalent to `IP_DONTFRAG` for IPv4 and `IPV6_DONTFRAG` for IPv6.

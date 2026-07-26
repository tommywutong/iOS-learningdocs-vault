---
title: 'minimumMTU(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/ip/minimummtu(_:)'
source_url: 'https://developer.apple.com/documentation/network/ip/minimummtu(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/ip/minimummtu%28_%3A%29.json'
content_hash: 'sha256:b047f62a9763b199'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [IP](../ip.md)

# minimumMTU(_:)

<sub>Instance Method</sub>

Configure IP to use the minimum MTU value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func minimumMTU(_ useMinimumMTU: Bool) -> IP
```

## Parameters

- `useMinimumMTU` — True to use the minimum MTU value, false otherwise.

## Discussion

The minimum MTU value is 1280 bytes for IPv6 (`IPV6_USE_MIN_MTU`). This value has no effect for IPv4.

---
title: 'noChecksumPreferred(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/udp/nochecksumpreferred(_:)'
source_url: 'https://developer.apple.com/documentation/network/udp/nochecksumpreferred(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/udp/nochecksumpreferred%28_%3A%29.json'
content_hash: 'sha256:6d445f0ee85992db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [UDP](../udp.md)

# noChecksumPreferred(_:)

<sub>Instance Method</sub>

Skip computing checksums when sending UDP packets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func noChecksumPreferred(_ noChecksum: Bool) -> UDP
```

## Discussion

This will only take effect when running over IPv4 (`UDP_NOCKSUM`).

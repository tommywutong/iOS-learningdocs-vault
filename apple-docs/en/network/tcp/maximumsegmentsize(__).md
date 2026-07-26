---
title: 'maximumSegmentSize(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/tcp/maximumsegmentsize(_:)'
source_url: 'https://developer.apple.com/documentation/network/tcp/maximumsegmentsize(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tcp/maximumsegmentsize%28_%3A%29.json'
content_hash: 'sha256:654bbd711687f24d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [TCP](../tcp.md)

# maximumSegmentSize(_:)

<sub>Instance Method</sub>

Set maximum segment size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func maximumSegmentSize(_ bytes: UInt32) -> TCP
```

## Parameters

- `bytes` — The maximum segment size in bytes.

## Discussion

The maximum segment size in bytes (`TCP_MAXSEG`).

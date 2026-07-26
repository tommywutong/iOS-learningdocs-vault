---
title: 'retransmitFinDrop(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/tcp/retransmitfindrop(_:)'
source_url: 'https://developer.apple.com/documentation/network/tcp/retransmitfindrop(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tcp/retransmitfindrop%28_%3A%29.json'
content_hash: 'sha256:7c9113ac61ce1016'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [TCP](../tcp.md)

# retransmitFinDrop(_:)

<sub>Instance Method</sub>

Configure TCP to drop the connection after a FIN does not receive an ACK.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func retransmitFinDrop(_ drop: Bool) -> TCP
```

## Parameters

- `drop` — True to drop, false otherwise.

## Discussion

A boolean to cause TCP to drop its connection after not receiving an ACK after a FIN (`TCP_RXT_FINDROP`).

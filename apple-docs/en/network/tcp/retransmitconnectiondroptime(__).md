---
title: 'retransmitConnectionDropTime(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/tcp/retransmitconnectiondroptime(_:)'
source_url: 'https://developer.apple.com/documentation/network/tcp/retransmitconnectiondroptime(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tcp/retransmitconnectiondroptime%28_%3A%29.json'
content_hash: 'sha256:0ae7e5d660f2dd68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [TCP](../tcp.md)

# retransmitConnectionDropTime(_:)

<sub>Instance Method</sub>

Set the TCP retransmission attempt timeout.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func retransmitConnectionDropTime(_ timeout: UInt32) -> TCP
```

## Parameters

- `timeout` — The retransmission attempt timeout, in seconds.

## Discussion

A timeout for TCP retransmission attempts, in seconds (`TCP_RXT_CONNDROPTIME`).

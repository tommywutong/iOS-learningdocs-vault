---
title: 'ackStretchingDisabled(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/tcp/ackstretchingdisabled(_:)'
source_url: 'https://developer.apple.com/documentation/network/tcp/ackstretchingdisabled(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tcp/ackstretchingdisabled%28_%3A%29.json'
content_hash: 'sha256:ae3b5834948378e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [TCP](../tcp.md)

# ackStretchingDisabled(_:)

<sub>Instance Method</sub>

Disable ACK stretching.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func ackStretchingDisabled(_ disableAckStretching: Bool) -> TCP
```

## Parameters

- `disableAckStretching` — True to disable ACK stretching, false otherwise.

## Discussion

A boolean to cause TCP to disable ACK stretching (`TCP_SENDMOREACKS`).

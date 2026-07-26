---
title: 'receiveTimeCalculated(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/ip/receivetimecalculated(_:)'
source_url: 'https://developer.apple.com/documentation/network/ip/receivetimecalculated(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/ip/receivetimecalculated%28_%3A%29.json'
content_hash: 'sha256:0eafbd5cc9b2d6e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [IP](../ip.md)

# receiveTimeCalculated(_:)

<sub>Instance Method</sub>

Configure IP to calculate receive time for inbound packets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func receiveTimeCalculated(_ calculateReceiveTime: Bool) -> IP
```

## Parameters

- `calculateReceiveTime` — True to calculate receive time, false otherwise.

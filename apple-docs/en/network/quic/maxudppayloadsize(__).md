---
title: 'maxUDPPayloadSize(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/quic/maxudppayloadsize(_:)'
source_url: 'https://developer.apple.com/documentation/network/quic/maxudppayloadsize(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/quic/maxudppayloadsize%28_%3A%29.json'
content_hash: 'sha256:8a9b51b41ab2adde'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [QUIC](../quic.md)

# maxUDPPayloadSize(_:)

<sub>Instance Method</sub>

Set the maximum length of a QUIC packet that you are willing to receive on a connection, in bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func maxUDPPayloadSize(_ size: Int) -> QUIC
```

## Parameters

- `size` — The maximum length, in bytes.

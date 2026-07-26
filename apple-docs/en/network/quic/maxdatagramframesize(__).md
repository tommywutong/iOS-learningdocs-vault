---
title: 'maxDatagramFrameSize(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/quic/maxdatagramframesize(_:)'
source_url: 'https://developer.apple.com/documentation/network/quic/maxdatagramframesize(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/quic/maxdatagramframesize%28_%3A%29.json'
content_hash: 'sha256:d25e0770ca1c5cc3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [QUIC](../quic.md)

# maxDatagramFrameSize(_:)

<sub>Instance Method</sub>

Set the max_datagram_frame_size transport parameter on a QUIC connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func maxDatagramFrameSize(_ size: Int) -> QUIC
```

## Parameters

- `size` — The value to use for the `max_datagram_frame_size` transport parameter on a QUIC connection.

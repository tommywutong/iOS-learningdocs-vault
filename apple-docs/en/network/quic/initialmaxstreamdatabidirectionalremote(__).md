---
title: 'initialMaxStreamDataBidirectionalRemote(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/quic/initialmaxstreamdatabidirectionalremote(_:)'
source_url: 'https://developer.apple.com/documentation/network/quic/initialmaxstreamdatabidirectionalremote(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/quic/initialmaxstreamdatabidirectionalremote%28_%3A%29.json'
content_hash: 'sha256:ad0fa78b60b72db1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [QUIC](../quic.md)

# initialMaxStreamDataBidirectionalRemote(_:)

<sub>Instance Method</sub>

Set the initial_max_stream_data_bidi_remote transport parameter on a QUIC connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func initialMaxStreamDataBidirectionalRemote(_ initialMaxStreamDataBidiRemote: Int) -> QUIC
```

## Parameters

- `initialMaxStreamDataBidiRemote` — The value to use for the `initial_max_stream_data_bidi_remote` transport parameter on a QUIC connection.

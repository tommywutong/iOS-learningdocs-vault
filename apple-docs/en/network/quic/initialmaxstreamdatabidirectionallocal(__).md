---
title: 'initialMaxStreamDataBidirectionalLocal(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/quic/initialmaxstreamdatabidirectionallocal(_:)'
source_url: 'https://developer.apple.com/documentation/network/quic/initialmaxstreamdatabidirectionallocal(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/quic/initialmaxstreamdatabidirectionallocal%28_%3A%29.json'
content_hash: 'sha256:c2e380e162c863e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [QUIC](../quic.md)

# initialMaxStreamDataBidirectionalLocal(_:)

<sub>Instance Method</sub>

Set the initial_max_stream_data_bidi_local transport parameter on a QUIC connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func initialMaxStreamDataBidirectionalLocal(_ initialMaxStreamDataBidiLocal: Int) -> QUIC
```

## Parameters

- `initialMaxStreamDataBidiLocal` — The value to use for the `initial_max_stream_data_bidi_local` transport parameter on a QUIC connection.

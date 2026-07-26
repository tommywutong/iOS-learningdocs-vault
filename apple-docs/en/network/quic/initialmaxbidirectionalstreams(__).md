---
title: 'initialMaxBidirectionalStreams(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/quic/initialmaxbidirectionalstreams(_:)'
source_url: 'https://developer.apple.com/documentation/network/quic/initialmaxbidirectionalstreams(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/quic/initialmaxbidirectionalstreams%28_%3A%29.json'
content_hash: 'sha256:710177a39995d36b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [QUIC](../quic.md)

# initialMaxBidirectionalStreams(_:)

<sub>Instance Method</sub>

Set the initial_max_streams_bidi transport parameter on a QUIC connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func initialMaxBidirectionalStreams(_ initialMaxStreamsBidi: Int) -> QUIC
```

## Parameters

- `initialMaxStreamsBidi` — The value to use for the `initial_max_streams_bidi` transport parameter on a QUIC connection.

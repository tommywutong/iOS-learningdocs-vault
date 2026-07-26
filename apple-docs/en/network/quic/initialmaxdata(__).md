---
title: 'initialMaxData(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/quic/initialmaxdata(_:)'
source_url: 'https://developer.apple.com/documentation/network/quic/initialmaxdata(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/quic/initialmaxdata%28_%3A%29.json'
content_hash: 'sha256:31e38c86b6431bc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [QUIC](../quic.md)

# initialMaxData(_:)

<sub>Instance Method</sub>

Set the initial_max_data transport parameter on a QUIC connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func initialMaxData(_ initialMaxData: Int) -> QUIC
```

## Parameters

- `initialMaxData` — The value to use for the `initial_max_data` transport parameter on a QUIC connection.

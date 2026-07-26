---
title: 'init(code:reason:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwprotocolquic/applicationerror/init(code:reason:)'
source_url: 'https://developer.apple.com/documentation/network/nwprotocolquic/applicationerror/init(code:reason:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolquic/applicationerror/init%28code%3Areason%3A%29.json'
content_hash: 'sha256:8d1add62910d6f7f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolQUIC](../../nwprotocolquic.md) · [ApplicationError](../applicationerror.md)

# init(code:reason:)

<sub>Initializer</sub>

Initializes a QUIC application error with an error code and an optional reason.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(code: UInt64, reason: String? = nil)
```

## Parameters

- `code` — The error code.

- `reason` — A string that describes the error.

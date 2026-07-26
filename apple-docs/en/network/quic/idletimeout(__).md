---
title: 'idleTimeout(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/quic/idletimeout(_:)'
source_url: 'https://developer.apple.com/documentation/network/quic/idletimeout(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/quic/idletimeout%28_%3A%29.json'
content_hash: 'sha256:e42065c2069ffca6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [QUIC](../quic.md)

# idleTimeout(_:)

<sub>Instance Method</sub>

Set the idle timeout for the QUIC connection, in milliseconds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func idleTimeout(_ timeout: Int) -> QUIC
```

## Parameters

- `timeout` — The idle timeout, in milliseconds.

## Discussion

If no packets are sent or received within this timeout, the QUIC connection will be closed.

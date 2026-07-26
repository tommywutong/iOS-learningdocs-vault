---
title: 'init(alpn:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/quic/init(alpn:)'
source_url: 'https://developer.apple.com/documentation/network/quic/init(alpn:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/quic/init%28alpn%3A%29.json'
content_hash: 'sha256:d7f28ed563915de1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [QUIC](../quic.md)

# init(alpn:)

<sub>Initializer</sub>

Create a QUIC protocol for use in a protocol stack.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(alpn: [String])
```

## Parameters

- `alpn` — An array of application layer protocol tokens to use for negotiation during the QUIC handshake.

## Discussion

The application layer protocol negotiation (ALPN) tokens describe the application protocol in use above QUIC.

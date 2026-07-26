---
title: 'init(_:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/tls/init(_:)'
source_url: 'https://developer.apple.com/documentation/network/tls/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tls/init%28_%3A%29.json'
content_hash: 'sha256:1609f87ecc7fdc0d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [TLS](../tls.md)

# init(_:)

<sub>Initializer</sub>

Create a TLS protocol to use in a protocol stack.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(@ProtocolStackBuilder<TCP> _ builder: () -> TCP)
```

## Parameters

- `builder` — The protocol stack below TLS.

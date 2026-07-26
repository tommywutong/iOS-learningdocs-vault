---
title: 'init(_:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/network/dtls/init(_:)'
source_url: 'https://developer.apple.com/documentation/network/dtls/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/dtls/init%28_%3A%29.json'
content_hash: 'sha256:3ecd9260bc1bd7db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [DTLS](../dtls.md)

# init(_:)

<sub>Initializer</sub>

Create a DTLS protocol to use in a protocol stack.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(@ProtocolStackBuilder<UDP> _ builder: () -> UDP)
```

## Parameters

- `builder` — The protocol stack below DTLS.

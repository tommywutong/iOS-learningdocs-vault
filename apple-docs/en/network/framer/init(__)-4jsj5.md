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
doc_path: '/documentation/network/framer/init(_:)-4jsj5'
source_url: 'https://developer.apple.com/documentation/network/framer/init(_:)-4jsj5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/framer/init%28_%3A%29-4jsj5.json'
content_hash: 'sha256:b4b86dd789581f09'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [Framer](../framer.md)

# init(_:)

<sub>Initializer</sub>

Create a Framer protocol for use in a protocol stack.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<BelowProtocol>(@ProtocolStackBuilder<BelowProtocol> _ builder: () -> BelowProtocol) where BelowProtocol : StreamProtocol
```

## Parameters

- `builder` — The protocol stack below Framer.

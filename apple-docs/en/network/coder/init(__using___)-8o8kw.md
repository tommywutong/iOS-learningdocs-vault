---
title: 'init(_:using:_:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/coder/init(_:using:_:)-8o8kw'
source_url: 'https://developer.apple.com/documentation/network/coder/init(_:using:_:)-8o8kw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/coder/init%28_%3Ausing%3A_%3A%29-8o8kw.json'
content_hash: 'sha256:1beb0e4e46f77a50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [Coder](../coder.md)

# init(_:using:_:)

<sub>Initializer</sub>

Create a Coder protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<BelowProtocol>(_ type: Sending.Type, using: CoderType, @ProtocolStackBuilder<BelowProtocol> _ builder: () -> BelowProtocol) where BelowProtocol : StreamProtocol
```

## Parameters

- `type` — The Codable type that will be sent and received.

- `builder` — The protocol stack below Coder.

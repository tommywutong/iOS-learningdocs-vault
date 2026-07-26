---
title: 'init(sending:receiving:using:_:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/coder/init(sending:receiving:using:_:)-7ox25'
source_url: 'https://developer.apple.com/documentation/network/coder/init(sending:receiving:using:_:)-7ox25'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/coder/init%28sending%3Areceiving%3Ausing%3A_%3A%29-7ox25.json'
content_hash: 'sha256:f7b382d3a4185a51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [Coder](../coder.md)

# init(sending:receiving:using:_:)

<sub>Initializer</sub>

Create a Coder protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<BelowProtocol>(sending: Sending.Type, receiving: Receiving.Type, using: CoderType, @ProtocolStackBuilder<BelowProtocol> _ builder: () -> BelowProtocol) where BelowProtocol : DatagramProtocol
```

## Parameters

- `sending` — The Codable type that will be sent.

- `receiving` — The Codable type that will be received.

- `using` — The NetworkCoder that will be used to encode and decode.

- `builder` — The protocol stack below Coder.

---
title: 'init(using:_:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/framer/init(using:_:)-94t7p'
source_url: 'https://developer.apple.com/documentation/network/framer/init(using:_:)-94t7p'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/framer/init%28using%3A_%3A%29-94t7p.json'
content_hash: 'sha256:7335afc50514affd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [Framer](../framer.md)

# init(using:_:)

<sub>Initializer</sub>

Create a Framer protocol for use in a protocol stack.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<BelowProtocol>(using framer: T.Type, @ProtocolStackBuilder<BelowProtocol> _ builder: () -> BelowProtocol) where BelowProtocol : MessageProtocol
```

## Parameters

- `builder` — The protocol stack below Framer.

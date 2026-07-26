---
title: FramerProtocol
framework: Network
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/framerprotocol
source_url: 'https://developer.apple.com/documentation/network/framerprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/framerprotocol.json'
content_hash: 'sha256:2ae510a831eb03b1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# FramerProtocol

<sub>Protocol</sub>

Framer protocols allow custom framing and serialization of messages on a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol FramerProtocol
```

## Overview

A Network Framer is an instance of a protocol in a connection’s protocol stack that parses and writes messages on top of a transport protocol, such as a TLS stream. A framer can add and parse headers or delimiters around application data to provide a message-oriented abstraction.

## Topics

### Type Properties

- [definition](framerprotocol/definition.md)

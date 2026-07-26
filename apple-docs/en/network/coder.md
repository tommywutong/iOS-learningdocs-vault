---
title: Coder
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/coder
source_url: 'https://developer.apple.com/documentation/network/coder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/coder.json'
content_hash: 'sha256:2a5a13134a581723'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# Coder

<sub>Structure</sub>

A protocol that frames and encodes/decodes Codable types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Coder<Sending, Receiving, CoderType> where Sending : Encodable, Receiving : Decodable, CoderType : NetworkCoder
```

## Overview

Supports sending and receiving Codable types using a specified format.

## Relationships

- **Conforms To**: [MessageProtocol](messageprotocol.md), [NetworkProtocolOptions](networkprotocoloptions.md), [OneToOneProtocol](onetooneprotocol.md)

## Topics

### Initializers

- [init(_:using:_:)](<coder/init(__using___)-61vdl.md>) — Create a Coder protocol.
- [init(_:using:_:)](<coder/init(__using___)-8o8kw.md>) — Create a Coder protocol.
- [init(receiving:sending:using:_:)](<coder/init(receiving_sending_using___)-4mm04.md>) — Create a Coder protocol.
- [init(receiving:sending:using:_:)](<coder/init(receiving_sending_using___)-7d2qd.md>) — Create a Coder protocol
- [init(sending:receiving:using:_:)](<coder/init(sending_receiving_using___)-1579q.md>) — Create a Coder protocol
- [init(sending:receiving:using:_:)](<coder/init(sending_receiving_using___)-7ox25.md>) — Create a Coder protocol.

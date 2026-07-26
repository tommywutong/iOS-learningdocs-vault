---
title: Framer
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/framer
source_url: 'https://developer.apple.com/documentation/network/framer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/framer.json'
content_hash: 'sha256:5562031575e31765'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# Framer

<sub>Structure</sub>

An instance of a Framer protocol to load into a protocol stack.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Framer<T> where T : FramerProtocol
```

## Relationships

- **Conforms To**: [MessageProtocol](messageprotocol.md), [NetworkProtocolOptions](networkprotocoloptions.md), [OneToOneProtocol](onetooneprotocol.md)

## Topics

### Initializers

- [init(_:)](<framer/init(__)-4jsj5.md>) — Create a Framer protocol for use in a protocol stack.
- [init(_:)](<framer/init(__)-7946z.md>) — Create a Framer protocol for use in a protocol stack.
- [init(using:_:)](<framer/init(using___)-16qam.md>) — Create a Framer protocol for use in a protocol stack.
- [init(using:_:)](<framer/init(using___)-94t7p.md>) — Create a Framer protocol for use in a protocol stack.

### Instance Properties

- [options](framer/options.md) — The framer options to use with this framer.

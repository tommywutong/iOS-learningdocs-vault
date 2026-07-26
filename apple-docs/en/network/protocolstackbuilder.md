---
title: ProtocolStackBuilder
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/protocolstackbuilder
source_url: 'https://developer.apple.com/documentation/network/protocolstackbuilder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/protocolstackbuilder.json'
content_hash: 'sha256:9a8ea93c76c5ca3c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# ProtocolStackBuilder

<sub>Structure</sub>

A resultBuilder for specifying and configuring protocol stacks in a declarative way

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@resultBuilder struct ProtocolStackBuilder<ApplicationProtocol, each P> where ApplicationProtocol : NetworkProtocolOptions, repeat each P : NetworkProtocolOptions
```

## Topics

### Type Methods

- [buildBlock(_:_:)](<protocolstackbuilder/buildblock(____).md>)

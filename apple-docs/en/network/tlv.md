---
title: TLV
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/tlv
source_url: 'https://developer.apple.com/documentation/network/tlv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tlv.json'
content_hash: 'sha256:f55dcbb3d3a2e8d1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# TLV

<sub>Structure</sub>

A Type-Length-Value (TLV) framing protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TLV
```

## Overview

This protocol will infer the length of the data based on the content passed to it in send.

Supports sending and receiving messages.

## Relationships

- **Conforms To**: [MessageProtocol](messageprotocol.md), [NetworkProtocolOptions](networkprotocoloptions.md), [OneToOneProtocol](onetooneprotocol.md)

## Topics

### Initializers

- [init(_:)](<tlv/init(__)-8ka4w.md>)
- [init(_:)](<tlv/init(__)-8qsbh.md>)
- [init(type:length:_:)](<tlv/init(type_length___)-7awe.md>) — Create TLV with the specified sizes for the type and length fields.
- [init(type:length:_:)](<tlv/init(type_length___)-h8s.md>) — Create TLV with the specified sizes for the type and length fields.

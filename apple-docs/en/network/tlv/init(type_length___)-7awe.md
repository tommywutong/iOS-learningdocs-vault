---
title: 'init(type:length:_:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/tlv/init(type:length:_:)-7awe'
source_url: 'https://developer.apple.com/documentation/network/tlv/init(type:length:_:)-7awe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tlv/init%28type%3Alength%3A_%3A%29-7awe.json'
content_hash: 'sha256:95d37011c8cc6bb7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [TLV](../tlv.md)

# init(type:length:_:)

<sub>Initializer</sub>

Create TLV with the specified sizes for the type and length fields.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<T, L, BelowProtocol>(type: T.Type, length: L.Type, @ProtocolStackBuilder<BelowProtocol> _ builder: () -> BelowProtocol) where T : Sendable, T : UnsignedInteger, L : Sendable, L : UnsignedInteger, BelowProtocol : MessageProtocol
```

## Parameters

- `type` — The object type to use for the `type` field.

- `length` — The object type to use for the `length` field.

- `builder` — The protocol stack below TLV.

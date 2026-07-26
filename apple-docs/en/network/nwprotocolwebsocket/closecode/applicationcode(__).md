---
title: 'NWProtocolWebSocket.CloseCode.applicationCode(_:)'
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwprotocolwebsocket/closecode/applicationcode(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwprotocolwebsocket/closecode/applicationcode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolwebsocket/closecode/applicationcode%28_%3A%29.json'
content_hash: 'sha256:ca78b5233feae448'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolWebSocket](../../nwprotocolwebsocket.md) · [CloseCode](../closecode.md)

# NWProtocolWebSocket.CloseCode.applicationCode(_:)

<sub>Case</sub>

A close code in the range reserved for applications and frameworks (3000-3999).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case applicationCode(UInt16)
```

## See Also

### Close Code Types

- [init(rawValue:)](<init(rawvalue_).md>) — Initializes a close code with a raw value.
- [NWProtocolWebSocket.CloseCode.protocolCode(_:)](<protocolcode(__).md>) — A well-known close code reserved by the protocol (values 1000-2999).
- [Defined](defined.md) — Well-known close code values.
- [NWProtocolWebSocket.CloseCode.privateCode(_:)](<privatecode(__).md>) — A close code in the private-use range (4000-4999).

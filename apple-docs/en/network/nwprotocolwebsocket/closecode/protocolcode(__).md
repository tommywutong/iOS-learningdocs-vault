---
title: 'NWProtocolWebSocket.CloseCode.protocolCode(_:)'
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwprotocolwebsocket/closecode/protocolcode(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwprotocolwebsocket/closecode/protocolcode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolwebsocket/closecode/protocolcode%28_%3A%29.json'
content_hash: 'sha256:368521598876acc1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolWebSocket](../../nwprotocolwebsocket.md) · [CloseCode](../closecode.md)

# NWProtocolWebSocket.CloseCode.protocolCode(_:)

<sub>Case</sub>

A well-known close code reserved by the protocol (values 1000-2999).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case protocolCode(NWProtocolWebSocket.CloseCode.Defined)
```

## See Also

### Close Code Types

- [init(rawValue:)](<init(rawvalue_).md>) — Initializes a close code with a raw value.
- [Defined](defined.md) — Well-known close code values.
- [NWProtocolWebSocket.CloseCode.applicationCode(_:)](<applicationcode(__).md>) — A close code in the range reserved for applications and frameworks (3000-3999).
- [NWProtocolWebSocket.CloseCode.privateCode(_:)](<privatecode(__).md>) — A close code in the private-use range (4000-4999).

---
title: 'init(rawValue:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwprotocolwebsocket/closecode/init(rawvalue:)'
source_url: 'https://developer.apple.com/documentation/network/nwprotocolwebsocket/closecode/init(rawvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolwebsocket/closecode/init%28rawvalue%3A%29.json'
content_hash: 'sha256:c58685e34bae0dde'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolWebSocket](../../nwprotocolwebsocket.md) · [CloseCode](../closecode.md)

# init(rawValue:)

<sub>Initializer</sub>

Initializes a close code with a raw value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(rawValue: UInt16) throws
```

## See Also

### Close Code Types

- [NWProtocolWebSocket.CloseCode.protocolCode(_:)](<protocolcode(__).md>) — A well-known close code reserved by the protocol (values 1000-2999).
- [Defined](defined.md) — Well-known close code values.
- [NWProtocolWebSocket.CloseCode.applicationCode(_:)](<applicationcode(__).md>) — A close code in the range reserved for applications and frameworks (3000-3999).
- [NWProtocolWebSocket.CloseCode.privateCode(_:)](<privatecode(__).md>) — A close code in the private-use range (4000-4999).

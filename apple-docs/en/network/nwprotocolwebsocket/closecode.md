---
title: NWProtocolWebSocket.CloseCode
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolwebsocket/closecode
source_url: 'https://developer.apple.com/documentation/network/nwprotocolwebsocket/closecode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolwebsocket/closecode.json'
content_hash: 'sha256:478776ed7deb2a89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWProtocolWebSocket](../nwprotocolwebsocket.md)

# NWProtocolWebSocket.CloseCode

<sub>Enumeration</sub>

Types of codes used upon closing a WebSocket connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CloseCode
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Close Code Types

- [init(rawValue:)](<closecode/init(rawvalue_).md>) — Initializes a close code with a raw value.
- [NWProtocolWebSocket.CloseCode.protocolCode(_:)](<closecode/protocolcode(__).md>) — A well-known close code reserved by the protocol (values 1000-2999).
- [Defined](closecode/defined.md) — Well-known close code values.
- [NWProtocolWebSocket.CloseCode.applicationCode(_:)](<closecode/applicationcode(__).md>) — A close code in the range reserved for applications and frameworks (3000-3999).
- [NWProtocolWebSocket.CloseCode.privateCode(_:)](<closecode/privatecode(__).md>) — A close code in the private-use range (4000-4999).

## See Also

### Sending Messages

- [init(opcode:)](<metadata/init(opcode_).md>) — Initializes a WebSocket message with a specific type code.
- [Opcode](opcode.md) — Types of messages that you send and receive on a WebSocket connection.
- [setPongHandler(_:handler:)](<metadata/setponghandler(__handler_).md>) — Sets a handler on a Ping message to be invoked when the corresponding Pong message is received.
- [closeCode](metadata/closecode.md) — The close code on a WebSocket message.

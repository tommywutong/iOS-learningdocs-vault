---
title: NWProtocolWebSocket.Opcode
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolwebsocket/opcode
source_url: 'https://developer.apple.com/documentation/network/nwprotocolwebsocket/opcode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolwebsocket/opcode.json'
content_hash: 'sha256:1f31541d1ef6d4a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWProtocolWebSocket](../nwprotocolwebsocket.md)

# NWProtocolWebSocket.Opcode

<sub>Enumeration</sub>

Types of messages that you send and receive on a WebSocket connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Opcode
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Data Types

- [NWProtocolWebSocket.Opcode.binary](opcode/binary.md) — A binary data message.
- [NWProtocolWebSocket.Opcode.text](opcode/text.md) — A text data message.
- [NWProtocolWebSocket.Opcode.cont](opcode/cont.md) — A continuation message.

### Control Types

- [NWProtocolWebSocket.Opcode.ping](opcode/ping.md) — A Ping message, which requests a Pong from the peer.
- [NWProtocolWebSocket.Opcode.pong](opcode/pong.md) — A Pong message in response to a Ping from the peer.
- [NWProtocolWebSocket.Opcode.close](opcode/close.md) — A message indicating a close of the connection.

## See Also

### Sending Messages

- [init(opcode:)](<metadata/init(opcode_).md>) — Initializes a WebSocket message with a specific type code.
- [setPongHandler(_:handler:)](<metadata/setponghandler(__handler_).md>) — Sets a handler on a Ping message to be invoked when the corresponding Pong message is received.
- [closeCode](metadata/closecode.md) — The close code on a WebSocket message.
- [CloseCode](closecode.md) — Types of codes used upon closing a WebSocket connection.

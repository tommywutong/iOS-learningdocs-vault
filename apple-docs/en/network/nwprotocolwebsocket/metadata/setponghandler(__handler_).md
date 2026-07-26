---
title: 'setPongHandler(_:handler:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwprotocolwebsocket/metadata/setponghandler(_:handler:)'
source_url: 'https://developer.apple.com/documentation/network/nwprotocolwebsocket/metadata/setponghandler(_:handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolwebsocket/metadata/setponghandler%28_%3Ahandler%3A%29.json'
content_hash: 'sha256:a0c0acfef8d395ed'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolWebSocket](../../nwprotocolwebsocket.md) · [Metadata](../metadata.md)

# setPongHandler(_:handler:)

<sub>Instance Method</sub>

Sets a handler on a Ping message to be invoked when the corresponding Pong message is received.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency func setPongHandler(_ queue: DispatchQueue, handler: @escaping @Sendable (NWError?) -> Void)
```

## See Also

### Sending Messages

- [init(opcode:)](<init(opcode_).md>) — Initializes a WebSocket message with a specific type code.
- [Opcode](../opcode.md) — Types of messages that you send and receive on a WebSocket connection.
- [closeCode](closecode.md) — The close code on a WebSocket message.
- [CloseCode](../closecode.md) — Types of codes used upon closing a WebSocket connection.

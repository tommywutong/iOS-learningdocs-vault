---
title: NWProtocolWebSocket.Response
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolwebsocket/response
source_url: 'https://developer.apple.com/documentation/network/nwprotocolwebsocket/response'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolwebsocket/response.json'
content_hash: 'sha256:664350c9c1ac367c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWProtocolWebSocket](../nwprotocolwebsocket.md)

# NWProtocolWebSocket.Response

<sub>Structure</sub>

A WebSocket handshake reponse sent from a server to a client.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Response
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Sending Handshake Responses

- [init(status:subprotocol:additionalHeaders:)](<response/init(status_subprotocol_additionalheaders_).md>) — Initializes a WebSocket server response with a status, selected subprotocol, and additional HTTP headers.
- [Status](response/status-swift.enum.md) — Status values that are sent with a WebSocket server response.
- [status](response/status-swift.property.md) — The status of a WebSocket server response.
- [subprotocol](response/subprotocol.md) — The selected subprotocol in a WebSocket server response.
- [additionalHeaders](response/additionalheaders.md) — Any additional HTTP headers in a WebSocket server response.

## See Also

### Handling Server Handshakes

- [setClientRequestHandler(_:handler:)](<options/setclientrequesthandler(__handler_).md>) — Sets a handler to react to as a server to inbound WebSocket client handshakes.

---
title: NWProtocolWebSocket.Response.Status
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolwebsocket/response/status-swift.enum
source_url: 'https://developer.apple.com/documentation/network/nwprotocolwebsocket/response/status-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolwebsocket/response/status-swift.enum.json'
content_hash: 'sha256:a417f6c99a2c5353'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolWebSocket](../../nwprotocolwebsocket.md) · [Response](../response.md)

# NWProtocolWebSocket.Response.Status

<sub>Enumeration</sub>

Status values that are sent with a WebSocket server response.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Status
```

## Relationships

- **Conforms To**: [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Handshake Status Values

- [NWProtocolWebSocket.Response.Status.accept](status-swift.enum/accept.md) — The client request is being accepted.
- [NWProtocolWebSocket.Response.Status.reject](status-swift.enum/reject.md) — The client request is being rejected.

## See Also

### Sending Handshake Responses

- [init(status:subprotocol:additionalHeaders:)](<init(status_subprotocol_additionalheaders_).md>) — Initializes a WebSocket server response with a status, selected subprotocol, and additional HTTP headers.
- [status](status-swift.property.md) — The status of a WebSocket server response.
- [subprotocol](subprotocol.md) — The selected subprotocol in a WebSocket server response.
- [additionalHeaders](additionalheaders.md) — Any additional HTTP headers in a WebSocket server response.

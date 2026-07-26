---
title: subprotocol
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolwebsocket/response/subprotocol
source_url: 'https://developer.apple.com/documentation/network/nwprotocolwebsocket/response/subprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolwebsocket/response/subprotocol.json'
content_hash: 'sha256:4a293176c9858f9b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolWebSocket](../../nwprotocolwebsocket.md) · [Response](../response.md)

# subprotocol

<sub>Instance Property</sub>

The selected subprotocol in a WebSocket server response.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let subprotocol: String?
```

## See Also

### Sending Handshake Responses

- [init(status:subprotocol:additionalHeaders:)](<init(status_subprotocol_additionalheaders_).md>) — Initializes a WebSocket server response with a status, selected subprotocol, and additional HTTP headers.
- [Status](status-swift.enum.md) — Status values that are sent with a WebSocket server response.
- [status](status-swift.property.md) — The status of a WebSocket server response.
- [additionalHeaders](additionalheaders.md) — Any additional HTTP headers in a WebSocket server response.

---
title: 'init(status:subprotocol:additionalHeaders:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwprotocolwebsocket/response/init(status:subprotocol:additionalheaders:)'
source_url: 'https://developer.apple.com/documentation/network/nwprotocolwebsocket/response/init(status:subprotocol:additionalheaders:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolwebsocket/response/init%28status%3Asubprotocol%3Aadditionalheaders%3A%29.json'
content_hash: 'sha256:b5f2da78b7afbb16'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolWebSocket](../../nwprotocolwebsocket.md) · [Response](../response.md)

# init(status:subprotocol:additionalHeaders:)

<sub>Initializer</sub>

Initializes a WebSocket server response with a status, selected subprotocol, and additional HTTP headers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(status: NWProtocolWebSocket.Response.Status, subprotocol: String?, additionalHeaders: [(name: String, value: String)]? = nil)
```

## See Also

### Sending Handshake Responses

- [Status](status-swift.enum.md) — Status values that are sent with a WebSocket server response.
- [status](status-swift.property.md) — The status of a WebSocket server response.
- [subprotocol](subprotocol.md) — The selected subprotocol in a WebSocket server response.
- [additionalHeaders](additionalheaders.md) — Any additional HTTP headers in a WebSocket server response.

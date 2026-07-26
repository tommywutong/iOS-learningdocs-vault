---
title: 'setClientRequestHandler(_:handler:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwprotocolwebsocket/options/setclientrequesthandler(_:handler:)'
source_url: 'https://developer.apple.com/documentation/network/nwprotocolwebsocket/options/setclientrequesthandler(_:handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolwebsocket/options/setclientrequesthandler%28_%3Ahandler%3A%29.json'
content_hash: 'sha256:e3cb2279e8aa91cb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolWebSocket](../../nwprotocolwebsocket.md) · [Options](../options.md)

# setClientRequestHandler(_:handler:)

<sub>Instance Method</sub>

Sets a handler to react to as a server to inbound WebSocket client handshakes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency func setClientRequestHandler(_ queue: DispatchQueue, handler: @escaping @Sendable ([String], [(name: String, value: String)]) -> NWProtocolWebSocket.Response)
```

## See Also

### Handling Server Handshakes

- [Response](../response.md) — A WebSocket handshake reponse sent from a server to a client.

---
title: additionalServerHeaders
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolwebsocket/metadata/additionalserverheaders
source_url: 'https://developer.apple.com/documentation/network/nwprotocolwebsocket/metadata/additionalserverheaders'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolwebsocket/metadata/additionalserverheaders.json'
content_hash: 'sha256:4623652cf52b203c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolWebSocket](../../nwprotocolwebsocket.md) · [Metadata](../metadata.md)

# additionalServerHeaders

<sub>Instance Property</sub>

Additional HTTP headers sent by the server during the WebSocket handshake.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var additionalServerHeaders: [(String, String)]? { get }
```

## See Also

### Inspecting Handshake Results

- [selectedSubprotocol](selectedsubprotocol.md) — The subprotocol selected by the server during the WebSocket handshake.

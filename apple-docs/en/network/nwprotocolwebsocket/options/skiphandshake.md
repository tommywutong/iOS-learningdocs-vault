---
title: skipHandshake
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolwebsocket/options/skiphandshake
source_url: 'https://developer.apple.com/documentation/network/nwprotocolwebsocket/options/skiphandshake'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolwebsocket/options/skiphandshake.json'
content_hash: 'sha256:a0dad3e9ca81181e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolWebSocket](../../nwprotocolwebsocket.md) · [Options](../options.md)

# skipHandshake

<sub>Instance Property</sub>

A Boolean indicating whether the WebSocket protocol skips its handshake and begins framing data once the underlying connection is established.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var skipHandshake: Bool { get set }
```

## Discussion

This option should not be set when communicating with a generic WebSocket server or client. This option allows a custom handshake (or no handshake) to be implemented below the WebSocket layer when both client and server are coordinated.

## See Also

### Configuring Client Handshakes

- [setAdditionalHeaders(_:)](<setadditionalheaders(__).md>) — Sets additional HTTP header fields to be sent by the client during the WebSocket handshake.
- [setSubprotocols(_:)](<setsubprotocols(__).md>) — Adds to the list of supported application protocols that will be presented to a WebSocket server during connection establishment.

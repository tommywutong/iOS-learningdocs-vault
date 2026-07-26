---
title: NWProtocolWebSocket.Options
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolwebsocket/options
source_url: 'https://developer.apple.com/documentation/network/nwprotocolwebsocket/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolwebsocket/options.json'
content_hash: 'sha256:dac4d1bd6d31ec19'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWProtocolWebSocket](../nwprotocolwebsocket.md)

# NWProtocolWebSocket.Options

<sub>Class</sub>

A container of options for configuring how WebSocket is used on a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Options
```

## Relationships

- **Inherits From**: [NWProtocolOptions](../nwprotocoloptions.md)

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Configuring WebSocket Options

- [init(_:)](<options/init(__).md>) — Initializes a default set of WebSocket connection options.
- [Version](version.md) — Supported versions of the WebSocket protocol.
- [autoReplyPing](options/autoreplyping.md) — A Boolean indicating whether the connection automatically replies to Ping messages instead of delivering them to you.
- [maximumMessageSize](options/maximummessagesize.md) — The maximum allowed message size, in bytes, to be received by the WebSocket connection.

### Configuring Client Handshakes

- [setAdditionalHeaders(_:)](<options/setadditionalheaders(__).md>) — Sets additional HTTP header fields to be sent by the client during the WebSocket handshake.
- [setSubprotocols(_:)](<options/setsubprotocols(__).md>) — Adds to the list of supported application protocols that will be presented to a WebSocket server during connection establishment.
- [skipHandshake](options/skiphandshake.md) — A Boolean indicating whether the WebSocket protocol skips its handshake and begins framing data once the underlying connection is established.

### Handling Server Handshakes

- [setClientRequestHandler(_:handler:)](<options/setclientrequesthandler(__handler_).md>) — Sets a handler to react to as a server to inbound WebSocket client handshakes.
- [Response](response.md) — A WebSocket handshake reponse sent from a server to a client.

## See Also

### Creating WebSocket Connections

- [definition](definition.md) — The system definition of the WebSocket protocol.

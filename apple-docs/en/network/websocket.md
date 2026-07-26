---
title: WebSocket
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/websocket
source_url: 'https://developer.apple.com/documentation/network/websocket'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/websocket.json'
content_hash: 'sha256:ec28a8c591b181ba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# WebSocket

<sub>Structure</sub>

The system definition of the WebSocket protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct WebSocket
```

## Overview

Can be used to add WebSocket to a protocol stack and configure its options.

## Relationships

- **Conforms To**: [MessageProtocol](messageprotocol.md), [NetworkProtocolOptions](networkprotocoloptions.md), [OneToOneProtocol](onetooneprotocol.md)

## Topics

### Initializers

- [init(_:)](<websocket/init(__)-5q53h.md>) — Create an instance of the WebSocket protocol.
- [init(_:)](<websocket/init(__)-7xsae.md>) — Create an instance of the WebSocket protocol.

### Instance Methods

- [additionalHeaders(_:)](<websocket/additionalheaders(__).md>) — Set additional HTTP header fields to be sent by the client during the WebSocket handshake.
- [autoReplyPing(_:)](<websocket/autoreplyping(__).md>) — Configure the WebSocket protocol to automatically reply to pings.
- [maximumMessageSize(_:)](<websocket/maximummessagesize(__).md>) — Set the maximum allowed message size to be received by the WebSocket connection.
- [skipHandshake(_:)](<websocket/skiphandshake(__).md>) — Configure the WebSocket protocol to skip the opening handshake and begin framing data as soon as the underlying connection is established.
- [subprotocols(_:)](<websocket/subprotocols(__).md>) — Set the list of supported application protocols that will be presented to a WebSocket server during connection establishment.

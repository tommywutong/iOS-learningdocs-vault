---
title: autoReplyPing
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolwebsocket/options/autoreplyping
source_url: 'https://developer.apple.com/documentation/network/nwprotocolwebsocket/options/autoreplyping'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolwebsocket/options/autoreplyping.json'
content_hash: 'sha256:2e9b4bf6409e0ff3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolWebSocket](../../nwprotocolwebsocket.md) · [Options](../options.md)

# autoReplyPing

<sub>Instance Property</sub>

A Boolean indicating whether the connection automatically replies to Ping messages instead of delivering them to you.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var autoReplyPing: Bool { get set }
```

## See Also

### Configuring WebSocket Options

- [init(_:)](<init(__).md>) — Initializes a default set of WebSocket connection options.
- [Version](../version.md) — Supported versions of the WebSocket protocol.
- [maximumMessageSize](maximummessagesize.md) — The maximum allowed message size, in bytes, to be received by the WebSocket connection.

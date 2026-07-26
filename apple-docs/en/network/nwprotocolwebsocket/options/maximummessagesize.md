---
title: maximumMessageSize
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolwebsocket/options/maximummessagesize
source_url: 'https://developer.apple.com/documentation/network/nwprotocolwebsocket/options/maximummessagesize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolwebsocket/options/maximummessagesize.json'
content_hash: 'sha256:e6111f92bf9414a7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolWebSocket](../../nwprotocolwebsocket.md) · [Options](../options.md)

# maximumMessageSize

<sub>Instance Property</sub>

The maximum allowed message size, in bytes, to be received by the WebSocket connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var maximumMessageSize: Int { get set }
```

## See Also

### Configuring WebSocket Options

- [init(_:)](<init(__).md>) — Initializes a default set of WebSocket connection options.
- [Version](../version.md) — Supported versions of the WebSocket protocol.
- [autoReplyPing](autoreplyping.md) — A Boolean indicating whether the connection automatically replies to Ping messages instead of delivering them to you.

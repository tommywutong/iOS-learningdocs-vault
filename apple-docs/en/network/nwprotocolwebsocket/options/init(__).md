---
title: 'init(_:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwprotocolwebsocket/options/init(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwprotocolwebsocket/options/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolwebsocket/options/init%28_%3A%29.json'
content_hash: 'sha256:93acd5d5dbb82f40'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolWebSocket](../../nwprotocolwebsocket.md) · [Options](../options.md)

# init(_:)

<sub>Initializer</sub>

Initializes a default set of WebSocket connection options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ version: NWProtocolWebSocket.Version = .version13)
```

## See Also

### Configuring WebSocket Options

- [Version](../version.md) — Supported versions of the WebSocket protocol.
- [autoReplyPing](autoreplyping.md) — A Boolean indicating whether the connection automatically replies to Ping messages instead of delivering them to you.
- [maximumMessageSize](maximummessagesize.md) — The maximum allowed message size, in bytes, to be received by the WebSocket connection.

---
title: NWProtocolWebSocket.Version
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolwebsocket/version
source_url: 'https://developer.apple.com/documentation/network/nwprotocolwebsocket/version'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolwebsocket/version.json'
content_hash: 'sha256:a4695c2574901a6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWProtocolWebSocket](../nwprotocolwebsocket.md)

# NWProtocolWebSocket.Version

<sub>Enumeration</sub>

Supported versions of the WebSocket protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Version
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Versions

- [NWProtocolWebSocket.Version.version13](version/version13.md) — Version 13 of the WebSocket protocol.

## See Also

### Configuring WebSocket Options

- [init(_:)](<options/init(__).md>) — Initializes a default set of WebSocket connection options.
- [autoReplyPing](options/autoreplyping.md) — A Boolean indicating whether the connection automatically replies to Ping messages instead of delivering them to you.
- [maximumMessageSize](options/maximummessagesize.md) — The maximum allowed message size, in bytes, to be received by the WebSocket connection.

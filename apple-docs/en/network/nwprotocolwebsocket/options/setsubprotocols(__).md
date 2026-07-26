---
title: 'setSubprotocols(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwprotocolwebsocket/options/setsubprotocols(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwprotocolwebsocket/options/setsubprotocols(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolwebsocket/options/setsubprotocols%28_%3A%29.json'
content_hash: 'sha256:67527fece19e3ee9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolWebSocket](../../nwprotocolwebsocket.md) · [Options](../options.md)

# setSubprotocols(_:)

<sub>Instance Method</sub>

Adds to the list of supported application protocols that will be presented to a WebSocket server during connection establishment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setSubprotocols(_ subprotocols: [String])
```

## See Also

### Configuring Client Handshakes

- [setAdditionalHeaders(_:)](<setadditionalheaders(__).md>) — Sets additional HTTP header fields to be sent by the client during the WebSocket handshake.
- [skipHandshake](skiphandshake.md) — A Boolean indicating whether the WebSocket protocol skips its handshake and begins framing data once the underlying connection is established.

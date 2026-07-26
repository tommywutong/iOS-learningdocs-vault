---
title: nw_ws_opcode_ping
framework: Network
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_ws_opcode_ping
source_url: 'https://developer.apple.com/documentation/network/nw_ws_opcode_ping'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_ws_opcode_ping.json'
content_hash: 'sha256:ef3cbfb6b13e1d95'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_ws_opcode_ping

<sub>Global Variable</sub>

A Ping message, which requests a Pong from the peer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nw_ws_opcode_ping: nw_ws_opcode_t { get }
```

## See Also

### Control Types

- [nw_ws_opcode_pong](nw_ws_opcode_pong.md) — A Pong message in response to a Ping from the peer.
- [nw_ws_opcode_close](nw_ws_opcode_close.md) — A message indicating a close of the connection.
- [nw_ws_opcode_invalid](nw_ws_opcode_invalid.md) — The message is not valid.

---
title: nw_connection_state_invalid
framework: Network
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_connection_state_invalid
source_url: 'https://developer.apple.com/documentation/network/nw_connection_state_invalid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_connection_state_invalid.json'
content_hash: 'sha256:743f7cfb59c91ef2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_connection_state_invalid

<sub>Global Variable</sub>

The connection is not valid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nw_connection_state_invalid: nw_connection_state_t { get }
```

## See Also

### Connection States

- [nw_connection_state_waiting](nw_connection_state_waiting.md) — The connection is waiting for a network path change.
- [nw_connection_state_preparing](nw_connection_state_preparing.md) — The connection in the process of being established.
- [nw_connection_state_ready](nw_connection_state_ready.md) — The connection is established, and ready to send and receive data.
- [nw_connection_state_failed](nw_connection_state_failed.md) — The connection has disconnected or encountered an error.
- [nw_connection_state_cancelled](nw_connection_state_cancelled.md) — The connection has been canceled.

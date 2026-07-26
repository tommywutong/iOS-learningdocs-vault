---
title: nw_connection_group_state_ready
framework: Network
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_connection_group_state_ready
source_url: 'https://developer.apple.com/documentation/network/nw_connection_group_state_ready'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_connection_group_state_ready.json'
content_hash: 'sha256:d28f2aefc1df7b30'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_connection_group_state_ready

<sub>Global Variable</sub>

The connection group is joined, and ready to send and receive data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nw_connection_group_state_ready: nw_connection_group_state_t { get }
```

## See Also

### States

- [nw_connection_group_state_invalid](nw_connection_group_state_invalid.md) — The connection group is not valid.
- [nw_connection_group_state_waiting](nw_connection_group_state_waiting.md) — The connection group is waiting for a network path change.
- [nw_connection_group_state_failed](nw_connection_group_state_failed.md) — The connection group encountered a fatal error.
- [nw_connection_group_state_cancelled](nw_connection_group_state_cancelled.md) — The connection group has been canceled.

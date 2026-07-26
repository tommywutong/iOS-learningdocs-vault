---
title: nw_connection_group_state_failed
framework: Network
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_connection_group_state_failed
source_url: 'https://developer.apple.com/documentation/network/nw_connection_group_state_failed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_connection_group_state_failed.json'
content_hash: 'sha256:958c07ccfc3539eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_connection_group_state_failed

<sub>Global Variable</sub>

The connection group encountered a fatal error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nw_connection_group_state_failed: nw_connection_group_state_t { get }
```

## See Also

### States

- [nw_connection_group_state_invalid](nw_connection_group_state_invalid.md) — The connection group is not valid.
- [nw_connection_group_state_waiting](nw_connection_group_state_waiting.md) — The connection group is waiting for a network path change.
- [nw_connection_group_state_ready](nw_connection_group_state_ready.md) — The connection group is joined, and ready to send and receive data.
- [nw_connection_group_state_cancelled](nw_connection_group_state_cancelled.md) — The connection group has been canceled.

---
title: nw_listener_state_cancelled
framework: Network
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_listener_state_cancelled
source_url: 'https://developer.apple.com/documentation/network/nw_listener_state_cancelled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_listener_state_cancelled.json'
content_hash: 'sha256:570e3a363aac8e4a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_listener_state_cancelled

<sub>Global Variable</sub>

The listener has been canceled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nw_listener_state_cancelled: nw_listener_state_t { get }
```

## See Also

### Listener States

- [nw_listener_state_invalid](nw_listener_state_invalid.md) — The listener is not valid.
- [nw_listener_state_waiting](nw_listener_state_waiting.md) — The listener is waiting for a network to become available.
- [nw_listener_state_ready](nw_listener_state_ready.md) — The listener is running and able to receive incoming connections.
- [nw_listener_state_failed](nw_listener_state_failed.md) — The listener has encountered a fatal error.

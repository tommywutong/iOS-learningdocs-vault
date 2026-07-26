---
title: nw_ethernet_channel_state_ready
framework: Network
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_ethernet_channel_state_ready
source_url: 'https://developer.apple.com/documentation/network/nw_ethernet_channel_state_ready'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_ethernet_channel_state_ready.json'
content_hash: 'sha256:2b9451bf26b0a55a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_ethernet_channel_state_ready

<sub>Global Variable</sub>

The channel is able to send and receive Ethernet frames.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nw_ethernet_channel_state_ready: nw_ethernet_channel_state_t { get }
```

## See Also

### States

- [nw_ethernet_channel_state_invalid](nw_ethernet_channel_state_invalid.md) — The channel is not valid.
- [nw_ethernet_channel_state_waiting](nw_ethernet_channel_state_waiting.md) — The channel is waiting for its interface to become available.
- [nw_ethernet_channel_state_preparing](nw_ethernet_channel_state_preparing.md) — The channel is registering with the interface.
- [nw_ethernet_channel_state_failed](nw_ethernet_channel_state_failed.md) — The channel has encountered a fatal error.
- [nw_ethernet_channel_state_cancelled](nw_ethernet_channel_state_cancelled.md) — The channel has been canceled.

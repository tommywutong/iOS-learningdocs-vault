---
title: nw_framer_start_result_ready
framework: Network
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_framer_start_result_ready
source_url: 'https://developer.apple.com/documentation/network/nw_framer_start_result_ready'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_framer_start_result_ready.json'
content_hash: 'sha256:65298e0d07ac851b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_framer_start_result_ready

<sub>Global Variable</sub>

The protocol is immediately ready to send and receive data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nw_framer_start_result_ready: nw_framer_start_result_t { get }
```

## See Also

### Start Results

- [nw_framer_start_result_will_mark_ready](nw_framer_start_result_will_mark_ready.md) — The protocol will perform a handshake, preventing the overall connection from becoming ready until [nw_framer_mark_ready](<nw_framer_mark_ready(__).md>) is called.

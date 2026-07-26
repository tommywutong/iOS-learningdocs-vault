---
title: NW_FRAMER_WAKEUP_TIME_FOREVER
framework: Network
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_framer_wakeup_time_forever
source_url: 'https://developer.apple.com/documentation/network/nw_framer_wakeup_time_forever'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_framer_wakeup_time_forever.json'
content_hash: 'sha256:287a79a069d06371'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NW_FRAMER_WAKEUP_TIME_FOREVER

<sub>Global Variable</sub>

A sentinel value that indicates that no wakeup should be delivered.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NW_FRAMER_WAKEUP_TIME_FOREVER: UInt64 { get }
```

## See Also

### Handling Asynchronous Events

- [nw_framer_schedule_wakeup](<nw_framer_schedule_wakeup(____).md>) — Requests that the [nw_framer_wakeup_handler_t](nw_framer_wakeup_handler_t.md) be called on your protocol at a specific time in the future.
- [nw_framer_set_wakeup_handler](<nw_framer_set_wakeup_handler(____).md>) — Sets a handler to receive scheduled wakeup events.
- [nw_framer_wakeup_handler_t](nw_framer_wakeup_handler_t.md) — A handler that delivers a scheduled wakeup event.
- [nw_framer_async](<nw_framer_async(____).md>) — Requests that a block be executed on the connection’s internal scheduling context.
- [nw_framer_block_t](nw_framer_block_t.md) — A block to be invoked asynchronously on your framer protocol’s scheduling context.

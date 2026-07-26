---
title: nw_framer_block_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_framer_block_t
source_url: 'https://developer.apple.com/documentation/network/nw_framer_block_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_framer_block_t.json'
content_hash: 'sha256:908f6ace8ae56ce1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_framer_block_t

<sub>Type Alias</sub>

A block to be invoked asynchronously on your framer protocol’s scheduling context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_framer_block_t = () -> Void
```

## See Also

### Handling Asynchronous Events

- [nw_framer_schedule_wakeup](<nw_framer_schedule_wakeup(____).md>) — Requests that the [nw_framer_wakeup_handler_t](nw_framer_wakeup_handler_t.md) be called on your protocol at a specific time in the future.
- [NW_FRAMER_WAKEUP_TIME_FOREVER](nw_framer_wakeup_time_forever.md) — A sentinel value that indicates that no wakeup should be delivered.
- [nw_framer_set_wakeup_handler](<nw_framer_set_wakeup_handler(____).md>) — Sets a handler to receive scheduled wakeup events.
- [nw_framer_wakeup_handler_t](nw_framer_wakeup_handler_t.md) — A handler that delivers a scheduled wakeup event.
- [nw_framer_async](<nw_framer_async(____).md>) — Requests that a block be executed on the connection’s internal scheduling context.

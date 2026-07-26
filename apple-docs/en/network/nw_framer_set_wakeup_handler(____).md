---
title: 'nw_framer_set_wakeup_handler(_:_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_framer_set_wakeup_handler(_:_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_framer_set_wakeup_handler(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_framer_set_wakeup_handler%28_%3A_%3A%29.json'
content_hash: 'sha256:2d78dcf6b40d0c31'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_framer_set_wakeup_handler(_:_:)

<sub>Function</sub>

Sets a handler to receive scheduled wakeup events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_framer_set_wakeup_handler(_ framer: nw_framer_t, _ wakeup_handler: @escaping nw_framer_wakeup_handler_t)
```

## See Also

### Handling Asynchronous Events

- [nw_framer_schedule_wakeup](<nw_framer_schedule_wakeup(____).md>) — Requests that the [nw_framer_wakeup_handler_t](nw_framer_wakeup_handler_t.md) be called on your protocol at a specific time in the future.
- [NW_FRAMER_WAKEUP_TIME_FOREVER](nw_framer_wakeup_time_forever.md) — A sentinel value that indicates that no wakeup should be delivered.
- [nw_framer_wakeup_handler_t](nw_framer_wakeup_handler_t.md) — A handler that delivers a scheduled wakeup event.
- [nw_framer_async](<nw_framer_async(____).md>) — Requests that a block be executed on the connection’s internal scheduling context.
- [nw_framer_block_t](nw_framer_block_t.md) — A block to be invoked asynchronously on your framer protocol’s scheduling context.

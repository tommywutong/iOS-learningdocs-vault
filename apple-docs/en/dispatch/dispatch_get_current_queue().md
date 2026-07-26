---
title: dispatch_get_current_queue()
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+（6.0 起废弃）, iPadOS 4.0+（6.0 起废弃）, tvOS, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/dispatch/dispatch_get_current_queue()
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_get_current_queue()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_get_current_queue%28%29.json'
content_hash: 'sha256:298c8b358bdc5c13'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_get_current_queue()

<sub>Function</sub>

Returns the queue on which the currently executing block is running.

<sub>tvOS, visionOS, watchOS</sub>

```swift
func dispatch_get_current_queue() -> dispatch_queue_t
```

## Return Value

Returns the current queue.

## Discussion

This function is defined to never return `NULL`.

When called from outside of the context of a submitted block, this function returns the main queue if the call is executed from the main thread. If the call is made from any other thread, this function returns the default concurrent queue.

## See Also

### Functions

- [dispatch_debugv](<dispatch_debugv(______).md>)

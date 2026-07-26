---
title: DISPATCH_QUEUE_CONCURRENT
framework: Dispatch
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_queue_concurrent
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_queue_concurrent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_queue_concurrent.json'
content_hash: 'sha256:cb02c584eab279b6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DISPATCH_QUEUE_CONCURRENT

<sub>Macro</sub>

A dispatch queue that executes blocks concurrently.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define DISPATCH_QUEUE_CONCURRENT
```

## Discussion

Although they execute blocks concurrently, you can use barrier blocks to create synchronization points within the queue.

## See Also

### Creating a Dispatch Queue

- [dispatch_get_main_queue](dispatch_get_main_queue.md) — Returns the serial dispatch queue associated with the application’s main thread.
- [dispatch_get_global_queue](dispatch_get_global_queue.md) — Returns a system-defined global concurrent queue with the specified quality-of-service class.
- [dispatch_queue_create](dispatch_queue_create.md) — Creates a new dispatch queue to which you can submit blocks.
- [dispatch_queue_create_with_target](dispatch_queue_create_with_target.md) — Creates a new dispatch queue to which you can submit blocks.
- [DISPATCH_QUEUE_SERIAL](dispatch_queue_serial.md) — A dispatch queue that executes blocks serially in FIFO order.
- [dispatch_queue_t](dispatch_queue_t.md) — A lightweight object to which your application submits blocks for subsequent execution.
- [dispatch_queue_main_t](dispatch_queue_main_t.md) — A dispatch queue that is bound to the app’s main thread and executes tasks serially on that thread.
- [dispatch_queue_global_t](dispatch_queue_global_t.md) — A dispatch queue that executes tasks concurrently using threads from the global thread pool.
- [dispatch_queue_serial_t](dispatch_queue_serial_t.md) — A dispatch queue that executes tasks serially in first-in, first-out (FIFO) order.
- [dispatch_queue_concurrent_t](dispatch_queue_concurrent_t.md) — A dispatch queue that executes tasks concurrently and in any order, respecting any barriers that may be in place.

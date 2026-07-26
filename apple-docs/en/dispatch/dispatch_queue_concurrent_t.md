---
title: dispatch_queue_concurrent_t
framework: Dispatch
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_queue_concurrent_t
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_queue_concurrent_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_queue_concurrent_t.json'
content_hash: 'sha256:aad25b761007c414'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_queue_concurrent_t

<sub>Type Alias</sub>

A dispatch queue that executes tasks concurrently and in any order, respecting any barriers that may be in place.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias dispatch_queue_concurrent_t = DispatchConcurrentQueue
```

## See Also

### Creating a Dispatch Queue

- [main](dispatchqueue/main.md) — The dispatch queue associated with the main thread of the current process.
- [global(qos:)](<dispatchqueue/global(qos_).md>) — Returns the global system queue with the specified quality-of-service class.
- [init(label:qos:attributes:autoreleaseFrequency:target:)](<dispatchqueue/init(label_qos_attributes_autoreleasefrequency_target_).md>) — Creates a new dispatch queue to which you can submit blocks.
- [QoSClass](dispatchqos/qosclass-swift.enum.md) — Quality-of-service classes that specify the priorities for executing tasks.
- [Attributes](dispatchqueue/attributes.md) — Attributes that define the behavior of a dispatch queue.
- [AutoreleaseFrequency](dispatchqueue/autoreleasefrequency.md) — Constants indicating the frequency with which a dispatch queue autoreleases objects.
- [OS_dispatch_queue_main](os_dispatch_queue_main-swift.class.md) — A system-provided dispatch queue that schedules tasks for serial execution on the app’s main thread.
- [OS_dispatch_queue_global](os_dispatch_queue_global-swift.class.md) — A system-provided dispatch queue that schedules tasks for concurrent execution.
- [DispatchSerialQueue](dispatchserialqueue.md) — A custom dispatch queue that schedules tasks for serial execution on an arbitrary thread.
- [DispatchConcurrentQueue](dispatchconcurrentqueue.md) — A custom dispatch queue that schedules tasks for concurrent execution.
- [dispatch_queue_main_t](dispatch_queue_main_t.md) — A dispatch queue that is bound to the app’s main thread and executes tasks serially on that thread.
- [dispatch_queue_global_t](dispatch_queue_global_t.md) — A dispatch queue that executes tasks concurrently using threads from the global thread pool.
- [dispatch_queue_serial_t](dispatch_queue_serial_t.md) — A dispatch queue that executes tasks serially in first-in, first-out (FIFO) order.

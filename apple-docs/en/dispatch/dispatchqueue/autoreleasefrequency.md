---
title: DispatchQueue.AutoreleaseFrequency
framework: Dispatch
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqueue/autoreleasefrequency
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/autoreleasefrequency'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/autoreleasefrequency.json'
content_hash: 'sha256:4c58a9eb9456eede'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQueue](../dispatchqueue.md)

# DispatchQueue.AutoreleaseFrequency

<sub>Enumeration</sub>

Constants indicating the frequency with which a dispatch queue autoreleases objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum AutoreleaseFrequency
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Autorelease Frequencies

- [DispatchQueue.AutoreleaseFrequency.inherit](autoreleasefrequency/inherit.md) — The queue inherits its autorelease frequency from its target queue.
- [DispatchQueue.AutoreleaseFrequency.workItem](autoreleasefrequency/workitem.md) — The queue configures an autorelease pool before the execution of a block, and releases the objects in that pool after the block finishes executing.
- [DispatchQueue.AutoreleaseFrequency.never](autoreleasefrequency/never.md) — The queue does not set up an autorelease pool around executed blocks.

## See Also

### Creating a Dispatch Queue

- [main](main.md) — The dispatch queue associated with the main thread of the current process.
- [global(qos:)](<global(qos_).md>) — Returns the global system queue with the specified quality-of-service class.
- [init(label:qos:attributes:autoreleaseFrequency:target:)](<init(label_qos_attributes_autoreleasefrequency_target_).md>) — Creates a new dispatch queue to which you can submit blocks.
- [QoSClass](../dispatchqos/qosclass-swift.enum.md) — Quality-of-service classes that specify the priorities for executing tasks.
- [Attributes](attributes.md) — Attributes that define the behavior of a dispatch queue.
- [OS_dispatch_queue_main](../os_dispatch_queue_main-swift.class.md) — A system-provided dispatch queue that schedules tasks for serial execution on the app’s main thread.
- [OS_dispatch_queue_global](../os_dispatch_queue_global-swift.class.md) — A system-provided dispatch queue that schedules tasks for concurrent execution.
- [DispatchSerialQueue](../dispatchserialqueue.md) — A custom dispatch queue that schedules tasks for serial execution on an arbitrary thread.
- [DispatchConcurrentQueue](../dispatchconcurrentqueue.md) — A custom dispatch queue that schedules tasks for concurrent execution.
- [dispatch_queue_main_t](../dispatch_queue_main_t.md) — A dispatch queue that is bound to the app’s main thread and executes tasks serially on that thread.
- [dispatch_queue_global_t](../dispatch_queue_global_t.md) — A dispatch queue that executes tasks concurrently using threads from the global thread pool.
- [dispatch_queue_serial_t](../dispatch_queue_serial_t.md) — A dispatch queue that executes tasks serially in first-in, first-out (FIFO) order.
- [dispatch_queue_concurrent_t](../dispatch_queue_concurrent_t.md) — A dispatch queue that executes tasks concurrently and in any order, respecting any barriers that may be in place.

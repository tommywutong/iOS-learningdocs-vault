---
title: 'global(qos:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchqueue/global(qos:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/global(qos:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/global%28qos%3A%29.json'
content_hash: 'sha256:9d5d885d9f0d6ef6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQueue](../dispatchqueue.md)

# global(qos:)

<sub>Type Method</sub>

Returns the global system queue with the specified quality-of-service class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func global(qos: DispatchQoS.QoSClass = .default) -> DispatchQueue
```

## Parameters

- `qos` — The quality-of-service level to associate with the queue. This value determines the priority at which the system schedules tasks for execution. For a list of possible values, see [QoSClass](../dispatchqos/qosclass-swift.enum.md).

## Discussion

This method returns a queue suitable for executing tasks with the specified quality-of-service level. Calls to the [dispatch_suspend](<../dispatchobject/suspend().md>), [dispatch_resume](<../dispatchobject/resume().md>), and [dispatch_set_context](../dispatch_set_context.md) functions have no effect on the returned queues.

Tasks submitted to the returned queue are scheduled concurrently with respect to one another.

## See Also

### Creating a Dispatch Queue

- [main](main.md) — The dispatch queue associated with the main thread of the current process.
- [init(label:qos:attributes:autoreleaseFrequency:target:)](<init(label_qos_attributes_autoreleasefrequency_target_).md>) — Creates a new dispatch queue to which you can submit blocks.
- [QoSClass](../dispatchqos/qosclass-swift.enum.md) — Quality-of-service classes that specify the priorities for executing tasks.
- [Attributes](attributes.md) — Attributes that define the behavior of a dispatch queue.
- [AutoreleaseFrequency](autoreleasefrequency.md) — Constants indicating the frequency with which a dispatch queue autoreleases objects.
- [OS_dispatch_queue_main](../os_dispatch_queue_main-swift.class.md) — A system-provided dispatch queue that schedules tasks for serial execution on the app’s main thread.
- [OS_dispatch_queue_global](../os_dispatch_queue_global-swift.class.md) — A system-provided dispatch queue that schedules tasks for concurrent execution.
- [DispatchSerialQueue](../dispatchserialqueue.md) — A custom dispatch queue that schedules tasks for serial execution on an arbitrary thread.
- [DispatchConcurrentQueue](../dispatchconcurrentqueue.md) — A custom dispatch queue that schedules tasks for concurrent execution.
- [dispatch_queue_main_t](../dispatch_queue_main_t.md) — A dispatch queue that is bound to the app’s main thread and executes tasks serially on that thread.
- [dispatch_queue_global_t](../dispatch_queue_global_t.md) — A dispatch queue that executes tasks concurrently using threads from the global thread pool.
- [dispatch_queue_serial_t](../dispatch_queue_serial_t.md) — A dispatch queue that executes tasks serially in first-in, first-out (FIFO) order.
- [dispatch_queue_concurrent_t](../dispatch_queue_concurrent_t.md) — A dispatch queue that executes tasks concurrently and in any order, respecting any barriers that may be in place.

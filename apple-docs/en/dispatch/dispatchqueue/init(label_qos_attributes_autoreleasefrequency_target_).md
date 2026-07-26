---
title: 'init(label:qos:attributes:autoreleaseFrequency:target:)'
framework: Dispatch
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchqueue/init(label:qos:attributes:autoreleasefrequency:target:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/init(label:qos:attributes:autoreleasefrequency:target:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/init%28label%3Aqos%3Aattributes%3Aautoreleasefrequency%3Atarget%3A%29.json'
content_hash: 'sha256:fb4bafc9abcdbce7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQueue](../dispatchqueue.md)

# init(label:qos:attributes:autoreleaseFrequency:target:)

<sub>Initializer</sub>

Creates a new dispatch queue to which you can submit blocks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(label: String, qos: DispatchQoS = .unspecified, attributes: DispatchQueue.Attributes = [], autoreleaseFrequency: DispatchQueue.AutoreleaseFrequency = .inherit, target: DispatchQueue? = nil)
```

## Parameters

- `label` — A string label to attach to the queue to uniquely identify it in debugging tools such as Instruments, sample, stackshots, and crash reports. Because applications, libraries, and frameworks can all create their own dispatch queues, a reverse-DNS naming style (`com.example.myqueue`) is recommended.

- `qos` — The quality-of-service level to associate with the queue. This value determines the priority at which the system schedules tasks for execution. For a list of possible values, see [QoSClass](../dispatchqos/qosclass-swift.enum.md).

- `attributes` — The attributes to associate with the queue. Include the concurrent attribute to create a dispatch queue that executes tasks concurrently. If you omit that attribute, the dispatch queue executes tasks serially.

- `autoreleaseFrequency` — The frequency with which to autorelease objects created by the blocks that the queue schedules. For a list of possible values, see [AutoreleaseFrequency](autoreleasefrequency.md).

- `target` — The target queue on which to execute blocks. Specify `DISPATCH_TARGET_QUEUE_DEFAULT` if you want the system to provide a queue that is appropriate for the current object.

## See Also

### Creating a Dispatch Queue

- [main](main.md) — The dispatch queue associated with the main thread of the current process.
- [global(qos:)](<global(qos_).md>) — Returns the global system queue with the specified quality-of-service class.
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

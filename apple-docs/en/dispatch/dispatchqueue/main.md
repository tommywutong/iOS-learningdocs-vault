---
title: main
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqueue/main
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/main'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/main.json'
content_hash: 'sha256:9d680535f6967bb1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQueue](../dispatchqueue.md)

# main

<sub>Type Property</sub>

The dispatch queue associated with the main thread of the current process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var main: DispatchQueue { get }
```

## Discussion

The system automatically creates the main queue and associates it with your application’s main thread. Your app uses one (and only one) of the following three approaches to execute blocks submitted to the main queue:

- Calling [dispatch_main](<../dispatchmain().md>)
- Starting your app with a call to [UIApplicationMain(_:_:_:_:)](<../../uikit/uiapplicationmain(________)-1yub7.md>) (iOS) or [NSApplicationMain(_:_:)](<../../appkit/nsapplicationmain(____).md>) (macOS)
- Using a [CFRunLoop](../../corefoundation/cfrunloop.md) on the main thread

As with the global concurrent queues, calls to [dispatch_suspend](<../dispatchobject/suspend().md>), [dispatch_resume](<../dispatchobject/resume().md>), [dispatch_set_context](../dispatch_set_context.md), and the like have no effect when used on the queue in this property.

> [!important] Important
> If the main thread is unresponsive for too long, it can lead to a `0x8badf00d` exception with the main thread at `mach_msg_trap`. On iOS, this exception may be raised if the watchdog mechanism detects that your app failed to respond to certain user interface events in time. The iOS watchdog exists in order to keep the user interface responsive.

If your app has a long running task, such as making network call, run it on a global system queue, or on another background dispatch queue. Alternatively, use asynchronous versions of the call, if available.

## See Also

### Creating a Dispatch Queue

- [global(qos:)](<global(qos_).md>) — Returns the global system queue with the specified quality-of-service class.
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

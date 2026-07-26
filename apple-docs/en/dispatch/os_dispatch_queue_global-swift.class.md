---
title: OS_dispatch_queue_global
framework: Dispatch
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/os_dispatch_queue_global-swift.class
source_url: 'https://developer.apple.com/documentation/dispatch/os_dispatch_queue_global-swift.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/os_dispatch_queue_global-swift.class.json'
content_hash: 'sha256:a90776d3f57e16cd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# OS_dispatch_queue_global

<sub>Class</sub>

A system-provided dispatch queue that schedules tasks for concurrent execution.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class OS_dispatch_queue_global
```

## Overview

You do not create objects of this type directly. You receive a queue of the appropriate type when you create a new [DispatchQueue](dispatchqueue.md) object.

## Relationships

- **Inherits From**: [DispatchQueue](dispatchqueue.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Equatable](../swift/equatable.md), [Executor](../swift/executor.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Scheduler](../combine/scheduler.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [TaskExecutor](../swift/taskexecutor.md)

## See Also

### Creating a Dispatch Queue

- [main](dispatchqueue/main.md) — The dispatch queue associated with the main thread of the current process.
- [global(qos:)](<dispatchqueue/global(qos_).md>) — Returns the global system queue with the specified quality-of-service class.
- [init(label:qos:attributes:autoreleaseFrequency:target:)](<dispatchqueue/init(label_qos_attributes_autoreleasefrequency_target_).md>) — Creates a new dispatch queue to which you can submit blocks.
- [QoSClass](dispatchqos/qosclass-swift.enum.md) — Quality-of-service classes that specify the priorities for executing tasks.
- [Attributes](dispatchqueue/attributes.md) — Attributes that define the behavior of a dispatch queue.
- [AutoreleaseFrequency](dispatchqueue/autoreleasefrequency.md) — Constants indicating the frequency with which a dispatch queue autoreleases objects.
- [OS_dispatch_queue_main](os_dispatch_queue_main-swift.class.md) — A system-provided dispatch queue that schedules tasks for serial execution on the app’s main thread.
- [DispatchSerialQueue](dispatchserialqueue.md) — A custom dispatch queue that schedules tasks for serial execution on an arbitrary thread.
- [DispatchConcurrentQueue](dispatchconcurrentqueue.md) — A custom dispatch queue that schedules tasks for concurrent execution.
- [dispatch_queue_main_t](dispatch_queue_main_t.md) — A dispatch queue that is bound to the app’s main thread and executes tasks serially on that thread.
- [dispatch_queue_global_t](dispatch_queue_global_t.md) — A dispatch queue that executes tasks concurrently using threads from the global thread pool.
- [dispatch_queue_serial_t](dispatch_queue_serial_t.md) — A dispatch queue that executes tasks serially in first-in, first-out (FIFO) order.
- [dispatch_queue_concurrent_t](dispatch_queue_concurrent_t.md) — A dispatch queue that executes tasks concurrently and in any order, respecting any barriers that may be in place.

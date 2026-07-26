---
title: DispatchQueue
framework: Dispatch
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqueue
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue.json'
content_hash: 'sha256:58d6fddd634e6aa7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchQueue

<sub>Class</sub>

An object that manages the execution of tasks serially or concurrently on your app’s main thread or on a background thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class DispatchQueue
```

## Overview

Dispatch queues are FIFO queues to which your application can submit tasks in the form of block objects. Dispatch queues execute tasks either serially or concurrently. Work submitted to dispatch queues executes on a pool of threads managed by the system. Except for the dispatch queue representing your app’s main thread, the system makes no guarantees about which thread it uses to execute a task.

You schedule work items synchronously or asynchronously. When you schedule a work item synchronously, your code waits until that item finishes execution. When you schedule a work item asynchronously, your code continues executing while the work item runs elsewhere.

> [!important] Important
> Attempting to synchronously execute a work item on the main queue results in deadlock.

### Avoiding Excessive Thread Creation

When designing tasks for concurrent execution, do not call methods that block the current thread of execution. When a task scheduled by a concurrent dispatch queue blocks a thread, the system creates additional threads to run other queued concurrent tasks. If too many tasks block, the system may run out of threads for your app.

Another way that apps consume too many threads is by creating too many private concurrent dispatch queues. Because each dispatch queue consumes thread resources, creating additional concurrent dispatch queues exacerbates the thread consumption problem. Instead of creating private concurrent queues, submit tasks to one of the global concurrent dispatch queues. For serial tasks, set the target of your serial queue to one of the global concurrent queues. That way, you can maintain the serialized behavior of the queue while minimizing the number of separate queues creating threads.

## Relationships

- **Inherits From**: [DispatchObject](dispatchobject.md)

- **Inherited By**: [DispatchConcurrentQueue](dispatchconcurrentqueue.md), [OS_dispatch_queue_global](os_dispatch_queue_global-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Executor](../swift/executor.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Scheduler](../combine/scheduler.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [TaskExecutor](../swift/taskexecutor.md)

## Topics

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
- [dispatch_queue_concurrent_t](dispatch_queue_concurrent_t.md) — A dispatch queue that executes tasks concurrently and in any order, respecting any barriers that may be in place.

### Executing Tasks Asynchronously

- [async(execute:)](<dispatchqueue/async(execute_).md>) — Schedules a work item for immediate execution, and returns immediately.
- [asyncAfter(deadline:execute:)](<dispatchqueue/asyncafter(deadline_execute_).md>) — Schedules a work item for execution at the specified time, and returns immediately.
- [asyncAfter(deadline:qos:flags:execute:)](<dispatchqueue/asyncafter(deadline_qos_flags_execute_).md>) — Schedules a block for execution using the specified attributes, and returns immediately.
- [asyncAfter(wallDeadline:execute:)](<dispatchqueue/asyncafter(walldeadline_execute_).md>) — Schedules a work item for execution after the specified time, and returns immediately.
- [asyncAfter(wallDeadline:qos:flags:execute:)](<dispatchqueue/asyncafter(walldeadline_qos_flags_execute_).md>) — Schedules a block for execution using the specified attributes, and returns immediately.

### Executing Tasks Synchronously

- [sync(execute:)](<dispatchqueue/sync(execute_)-2fzvo.md>) — Submits a work item for execution on the current queue and returns after that block finishes executing.
- [dispatch_sync](<dispatchqueue/sync(execute_)-3segw.md>) — Submits a block object for execution and returns after that block finishes executing.
- [sync(execute:)](<dispatchqueue/sync(execute_)-20xby.md>) — Submits a work item for execution and returns the results from that item after it finishes executing.
- [sync(flags:execute:)](<dispatchqueue/sync(flags_execute_).md>) — Submits a work item for execution using the specified attributes and returns the results from that item after it finishes executing.
- [dispatch_async_and_wait](<dispatchqueue/asyncandwait(execute_)-1udeu.md>) — Submits a work item for execution and returns only after it finishes executing.

### Executing a Task in Parallel

- [concurrentPerform(iterations:execute:)](<dispatchqueue/concurrentperform(iterations_execute_).md>) — Submits a single block to the dispatch queue and causes the block to be executed the specified number of times.

### Dispatching Work to Groups

- [async(group:execute:)](<dispatchqueue/async(group_execute_).md>) — Schedules a work item asynchronously for execution and associates it with the specified dispatch group.
- [async(group:qos:flags:execute:)](<dispatchqueue/async(group_qos_flags_execute_).md>) — Schedules a block asynchronously for execution and optionally associates it with a dispatch group.

### Managing Queue Attributes

- [label](dispatchqueue/label.md) — The label you assigned to the dispatch queue at creation time.
- [qos](dispatchqueue/qos.md) — The quality-of-service level assgined to the queue.
- [dispatch_set_target_queue](<dispatchobject/settarget(queue_).md>) — Specifies the dispatch queue on which to perform work associated with the current object.

### Getting and Setting Contextual Data

- [setSpecific(key:value:)](<dispatchqueue/setspecific(key_value_).md>) — Sets the key/value data for the specified dispatch queue.
- [getSpecific(key:)](<dispatchqueue/getspecific(key_)-swift.method.md>) — Returns the value for the key associated with this dispatch queue.
- [getSpecific(key:)](<dispatchqueue/getspecific(key_)-swift.type.method.md>) — Returns the value for the key associated with the current execution context.
- [DispatchSpecificKey](dispatchspecifickey.md) — A key associated with a specific contextual value on a dispatch queue.

### Managing the Main Dispatch Queue

- [dispatch_main](<dispatchmain().md>) — Executes blocks submitted to the main queue.

### Scheduling Combine Publishers

- [SchedulerTimeType](dispatchqueue/schedulertimetype.md) — The scheduler time type used by the dispatch queue.
- [SchedulerOptions](dispatchqueue/scheduleroptions.md) — A set of options that affect the operation of the dispatch queue scheduler.

### Deprecated

- [global(priority:)](<dispatchqueue/global(priority_).md>)
- [GlobalQueuePriority](dispatchqueue/globalqueuepriority.md) — Legacy constants for queue priorities.

### Instance Methods

- [asyncAfterUnsafe(deadline:qos:flags:execute:)](<dispatchqueue/asyncafterunsafe(deadline_qos_flags_execute_).md>)
- [asyncAfterUnsafe(wallDeadline:qos:flags:execute:)](<dispatchqueue/asyncafterunsafe(walldeadline_qos_flags_execute_).md>)
- [asyncAndWait(execute:)](<dispatchqueue/asyncandwait(execute_)-52p9n.md>)
- [asyncAndWait(execute:)](<dispatchqueue/asyncandwait(execute_)-pfxy.md>)
- [asyncAndWait(flags:execute:)](<dispatchqueue/asyncandwait(flags_execute_).md>)
- [asyncUnsafe(group:qos:flags:execute:)](<dispatchqueue/asyncunsafe(group_qos_flags_execute_).md>)

### Default Implementations

- [Scheduler Implementations](dispatchqueue/scheduler-implementations.md)

## See Also

### Queues and Tasks

- [DispatchWorkItem](dispatchworkitem.md) — The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.
- [DispatchGroup](dispatchgroup.md) — A group of tasks that you monitor as a single unit.
- [Dispatch Queue](dispatch-queue.md) — An object that manages the execution of tasks serially or concurrently on your app’s main thread or on a background thread.
- [Dispatch Work Item](dispatch-work-item.md) — The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.
- [Dispatch Group](dispatch-group.md) — A group of tasks that you monitor as a single unit.
- [Workloop](workloop.md) — A dispatch object that prioritizes the execution of tasks based on their quality-of-service (QoS) level.

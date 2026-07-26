---
title: OperationQueue
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/operationqueue
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue.json'
content_hash: 'sha256:76f4c5f79de8e702'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# OperationQueue

<sub>Class</sub>

A queue that regulates the execution of operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class OperationQueue
```

## Overview

An operation queue invokes its queued [Operation](operation.md) objects based on their priority and readiness. After you add an operation to a queue, it remains in the queue until the operation finishes its task. You can’t directly remove an operation from a queue after you add it.

> [!note] Note
> Operation queues retain operations until the operations finish, and queues themselves are retained until all operations are finished. Suspending an operation queue with operations that aren’t finished can result in a memory leak.

For more information about using operation queues, see the [Concurrency Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091).

### Determine the Execution Order

An operation queue organizes and invokes its operations according to their readiness, priority level, and interoperation dependencies. If all of the queued operations have the same [queuePriority](operation/queuepriority-swift.property.md) and the [ready](operation/isready.md) property returns [true](../swift/true.md), the queue invokes them in the order you added them. Otherwise, the operation queue always invokes the operation with the highest priority relative to the other ready operations.

However, don’t rely on queue semantics to ensure a specific execution order of operations  because changes in the readiness of an operation can change the resulting execution order. Interoperation dependencies provide an absolute execution order for operations, even if those operations are located in different operation queues. An operation object isn’t ready to run until all of its dependent operations have finished running.

For details on how to set priority levels and dependencies, see Managing Dependencies in [Operation](operation.md).

### Respond to Operation Cancelation

Finishing its task doesn’t necessarily mean that the operation performed that task to completion; an operation can also be canceled. Canceling an operation object leaves the object in the queue but notifies the object that it should stop its task as quickly as possible. For currently executing operations, this means that the operation object’s work code must check the cancellation state, stop what it is doing, and mark itself as finished. For operations that are queued but not yet executing, the queue must still call the operation object’s [- start](<operation/start().md>) method so that it can processes the cancellation event and mark itself as finished.

> [!note] Note
> Canceling an operation causes the operation to ignore any dependencies it may have. This behavior makes it possible for the queue to invoke the operation’s [- start](<operation/start().md>) method as soon as possible. The [- start](<operation/start().md>) method, in turn, moves the operation to the finished state so that it can be removed from the queue.

For more information about operation cancellation, see [Responding to the Cancel Command](operation.md#Responding-to-the-Cancel-Command) in [Operation](operation.md).

### Observe Operations Using Key-Value Observing

The [OperationQueue](operationqueue.md) class is key-value coding (KVC) and key-value observing (KVO) compliant. You can observe these properties to control other parts of your application. To observe the properties, use the following key paths:

- [operations](operationqueue/operations.md) — Read-only
- [operationCount](operationqueue/operationcount.md) — Read-only
- [maxConcurrentOperationCount](operationqueue/maxconcurrentoperationcount.md) — Readable and writable
- [suspended](operationqueue/issuspended.md) — Readable and writable
- [name](operationqueue/name.md) — Readable and writable

Although you can attach observers to these properties, don’t use Cocoa bindings to bind these properties to elements of your application’s user interface. Code associated with your user interface typically must run only in your app’s main thread. However, KVO notifications associated with an operation queue may occur in any thread.

For more information about KVO and how to attach observers to an object, see the [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

### Plan for Thread Safety

You can safely use a single [OperationQueue](operationqueue.md) object from multiple threads without creating additional locks to synchronize access to that object.

Operation queues use the [Dispatch](../dispatch.md) framework to initiate the execution of their operations. As a result, queues always invoke operations on a separate thread, regardless of whether the operation is synchronous or asynchronous.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [ProgressReporting](progressreporting.md), [Scheduler](../combine/scheduler.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing Specific Operation Queues

- [mainQueue](operationqueue/main.md) — Returns the operation queue associated with the main thread.
- [currentQueue](operationqueue/current.md) — Returns the operation queue that launched the current operation.

### Managing Operations in the Queue

- [- addOperation:](<operationqueue/addoperation(__)-64o8a.md>) — Adds the specified operation to the receiver.
- [- addOperations:waitUntilFinished:](<operationqueue/addoperations(__waituntilfinished_).md>) — Adds the specified operations to the queue.
- [- addOperationWithBlock:](<operationqueue/addoperation(__)-5s294.md>) — Wraps the specified block in an operation and adds it to the receiver.
- [- addBarrierBlock:](<operationqueue/addbarrierblock(__).md>) — Invokes a block when the queue finishes all enqueued operations, and prevents subsequent operations from starting until the block has completed.
- [- cancelAllOperations](<operationqueue/cancelalloperations().md>) — Cancels all queued and executing operations.
- [- waitUntilAllOperationsAreFinished](<operationqueue/waituntilalloperationsarefinished().md>) — Blocks the current thread until all the receiver’s queued and executing operations finish executing.
- [operations](operationqueue/operations.md) — The operations currently in the queue. _(deprecated)_
- [operationCount](operationqueue/operationcount.md) — The number of operations currently in the queue. _(deprecated)_

### Managing the Execution of Operations

- [qualityOfService](operationqueue/qualityofservice.md) — The default service level to apply to operations that the queue invokes.
- [maxConcurrentOperationCount](operationqueue/maxconcurrentoperationcount.md) — The maximum number of queued operations that can run at the same time.
- [NSOperationQueueDefaultMaxConcurrentOperationCount](operationqueue/defaultmaxconcurrentoperationcount.md) — The default maximum number of operations to invoke concurrently in a queue.

### Monitoring Progress of Operations

- [progress](operationqueue/progress.md) — An object that represents the total progress of the operations executing in the queue.

### Suspending Execution

- [suspended](operationqueue/issuspended.md) — A Boolean value indicating whether the queue is actively scheduling operations for execution.

### Configuring the Queue

- [name](operationqueue/name.md) — The name of the operation queue.
- [underlyingQueue](operationqueue/underlyingqueue.md) — The dispatch queue that the operation queue uses to invoke operations.

### Scheduling Operations

- [schedule(after:tolerance:options:_:)](<operationqueue/schedule(after_tolerance_options___).md>) — Performs the action at some time after the specified date, optionally taking into account tolerance if possible.
- [schedule(after:interval:tolerance:options:_:)](<operationqueue/schedule(after_interval_tolerance_options___).md>) — Performs the action at some time after the specified date, at the specified frequency, optionally taking into account tolerance if possible.
- [schedule(options:_:)](<operationqueue/schedule(options___).md>) — Performs the action at the next possible opportunity.
- [now](operationqueue/now.md) — The operation queue’s definition of the current moment in time.
- [minimumTolerance](operationqueue/minimumtolerance.md) — The minimum tolerance the dispatch queue scheduler allows.
- [SchedulerTimeType](operationqueue/schedulertimetype.md) — The scheduler time type the operation queue uses.
- [SchedulerOptions](operationqueue/scheduleroptions.md) — A type that defines options the operation queue accepts.

### Default Implementations

- [Scheduler Implementations](operationqueue/scheduler-implementations.md)

## See Also

### Operations

- [Operation](operation.md) — An abstract class that represents the code and data associated with a single task.
- [BlockOperation](blockoperation.md) — An operation that manages the concurrent execution of one or more blocks.

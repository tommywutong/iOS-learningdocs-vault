---
title: Task
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/task
source_url: 'https://developer.apple.com/documentation/swift/task'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/task.json'
content_hash: 'sha256:7ef6b27fe15d711f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Task

<sub>Structure</sub>

A unit of asynchronous work.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Task<Success, Failure> where Success : Sendable, Failure : Error
```

## Overview

When you create an instance of `Task`, you provide a closure that contains the work for that task to perform. Tasks can start running immediately after creation; you don’t explicitly start or schedule them. After creating a task, you use the instance to interact with it — for example, to wait for it to complete or to cancel it. It’s not a programming error to discard a reference to a task without waiting for that task to finish or canceling it. A task runs regardless of whether you keep a reference to it. However, if you discard the reference to a task, you give up the ability to wait for that task’s result or cancel the task.

To support operations on the current task, which can be either a detached task or child task, `Task` also exposes class methods like `yield()`. Because these methods are asynchronous, they’re always invoked as part of an existing task.

Only code that’s running as part of the task can interact with that task. To interact with the current task, you call one of the static methods on `Task`.

A task’s execution can be seen as a series of periods where the task ran. Each such period ends at a suspension point or the completion of the task. These periods of execution are represented by instances of `PartialAsyncTask`. Unless you’re implementing a custom executor, you don’t directly interact with partial tasks.

For information about the language-level concurrency model that `Task` is part of, see [Concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/).

## Task Cancellation

Tasks include a shared mechanism for indicating cancellation, but not a shared implementation for how to handle cancellation. Depending on the work you’re doing in the task, the correct way to stop that work varies. Likewise, it’s the responsibility of the code running as part of the task to check for cancellation whenever stopping is appropriate. In a long-task that includes multiple pieces, you might need to check for cancellation at several points, and handle cancellation differently at each point. If you only need to throw an error to stop the work, call the `Task.checkCancellation()` function to check for cancellation. Other responses to cancellation include returning the work completed so far, returning an empty result, or returning `nil`.

Cancellation is a purely Boolean state; there’s no way to include additional information like the reason for cancellation. This reflects the fact that a task can be canceled for many reasons, and additional reasons can accrue during the cancellation process.

### Task closure lifetime

Tasks are initialized by passing a closure containing the code that will be executed by a given task.

After this code has run to completion, the task has completed, resulting in either a failure or result value, this closure is eagerly released.

Retaining a task object doesn’t indefinitely retain the closure, because any references that a task holds are released after the task completes. Consequently, tasks rarely need to capture weak references to values.

For example, in the following snippet of code it is not necessary to capture the actor as `weak`, because as the task completes it’ll let go of the actor reference, breaking the reference cycle between the Task and the actor holding it.

```swift
struct Work: Sendable {}

actor Worker {
    var work: Task<Void, Never>?
    var result: Work?

    deinit {
        // even though the task is still retained,
        // once it completes it no longer causes a reference cycle with the actor

        print("deinit actor")
    }

    func start() {
        work = Task {
            print("start task work")
            try? await Task.sleep(for: .seconds(3))
            self.result = Work() // we captured self
            print("completed task work")
            // but as the task completes, this reference is released
        }
        // we keep a strong reference to the task
    }
}
```

And using it like this:

```swift
await Worker().start()
```

Note that the actor is only retained by the start() method’s use of `self`, and that the start method immediately returns, without waiting for the unstructured `Task` to finish. Once the task is completed and its closure is destroyed, the strong reference to the actor is also released allowing the actor to deinitialize as expected.

Therefore, the above call will consistently result in the following output:

```other
start task work
completed task work
deinit actor
```

## Relationships

- **Conforms To**: [Equatable](equatable.md), [Hashable](hashable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Creating a Task

- [init(name:priority:operation:)](<task/init(name_priority_operation_)-2dll5.md>) — Runs the given nonthrowing operation asynchronously as part of a new _unstructured_ top-level task.
- [init(name:priority:operation:)](<task/init(name_priority_operation_)-43wmk.md>) — Runs the given throwing operation asynchronously as part of a new _unstructured_ top-level task.
- [init(name:executorPreference:priority:operation:)](<task/init(name_executorpreference_priority_operation_)-59bfi.md>) — Runs the given throwing operation asynchronously as part of a new _unstructured_ top-level task.
- [init(name:executorPreference:priority:operation:)](<task/init(name_executorpreference_priority_operation_)-81pay.md>) — Runs the given nonthrowing operation asynchronously as part of a new _unstructured_ top-level task.
- [currentPriority](task/currentpriority.md) — The current task’s priority.
- [basePriority](task/basepriority.md) — The current task’s base priority.
- [withTaskPriorityEscalationHandler(operation:onPriorityEscalated:)](<withtaskpriorityescalationhandler(operation_onpriorityescalated_).md>) — Runs the passed `operation` while registering a task priority escalation handler. The handler will be triggered concurrently to the current task if the current is subject to priority escalation.

### Creating a Detached Task

- [detached(name:priority:operation:)](<task/detached(name_priority_operation_)-795w1.md>) — Runs the given throwing operation asynchronously as part of a new _unstructured_ _detached_ top-level task.
- [detached(name:priority:operation:)](<task/detached(name_priority_operation_)-9xki7.md>) — Runs the given nonthrowing operation asynchronously as part of a new _unstructured_ _detached_ top-level task.
- [detached(name:executorPreference:priority:operation:)](<task/detached(name_executorpreference_priority_operation_)-6r16s.md>) — Runs the given throwing operation asynchronously as part of a new _unstructured_ _detached_ top-level task.
- [detached(name:executorPreference:priority:operation:)](<task/detached(name_executorpreference_priority_operation_)-75ffe.md>) — Runs the given nonthrowing operation asynchronously as part of a new _unstructured_ _detached_ top-level task.

### Creating a Task that Starts Immediately

- [immediate(name:priority:executorPreference:operation:)](<task/immediate(name_priority_executorpreference_operation_)-88o80.md>) — Create and immediately start running a new task in the context of the calling thread/task.
- [immediate(name:priority:executorPreference:operation:)](<task/immediate(name_priority_executorpreference_operation_)-9bghc.md>) — Create and immediately start running a new task in the context of the calling thread/task.
- [immediateDetached(name:priority:executorPreference:operation:)](<task/immediatedetached(name_priority_executorpreference_operation_)-52ipd.md>) — Create and immediately start running a new detached task in the context of the calling thread/task.
- [immediateDetached(name:priority:executorPreference:operation:)](<task/immediatedetached(name_priority_executorpreference_operation_)-7h41b.md>) — Create and immediately start running a new detached task in the context of the calling thread/task.

### Accessing Results

- [value](task/value-60t02.md) — The result from a throwing task, after it completes.
- [value](task/value-40dtq.md) — The result from a nonthrowing task, after it completes.
- [result](task/result.md) — The result or error from a throwing task, after it completes.

### Accessing the Current Task’s Name

- [name](task/name-swift.type.property.md) — Returns the human-readable name of the current task, if it was set during the tasks’ creation.

### Canceling Tasks

- [CancellationError](cancellationerror.md) — An error that indicates a task was canceled.
- [cancel()](<task/cancel().md>) — Cancels this task.
- [isCancelled](task/iscancelled-swift.property.md) — A Boolean value that indicates whether the task should stop executing.
- [isCancelled](task/iscancelled-swift.type.property.md) — A Boolean value that indicates whether the task should stop executing.
- [checkCancellation()](<task/checkcancellation().md>) — Throws an error if the task was canceled.
- [withTaskCancellationHandler(operation:onCancel:)](<withtaskcancellationhandler(operation_oncancel_).md>) — Execute an operation with a cancellation handler that’s immediately invoked if the current task is canceled.
- [withTaskCancellationHandler(operation:onCancel:isolation:)](<withtaskcancellationhandler(operation_oncancel_isolation_).md>) — Execute an operation with a cancellation handler that’s immediately invoked if the current task is canceled.

### Shielding Tasks from Cancellation

- [withTaskCancellationShield(operation:)](<withtaskcancellationshield(operation_)-2lzl8.md>) — Enters a scope in which a task cancellation shield is active. _(beta)_
- [withTaskCancellationShield(operation:)](<withtaskcancellationshield(operation_)-8zlgh.md>) — Enters a scope in which a task cancellation shield is active. _(beta)_

### Suspending Execution

- [yield()](<task/yield().md>) — Suspends the current task and allows other tasks to execute.
- [sleep(nanoseconds:)](<task/sleep(nanoseconds_).md>) — Suspends the current task for at least the given duration in nanoseconds.
- [sleep(for:tolerance:clock:)](<task/sleep(for_tolerance_clock_).md>) — Suspends the current task for the given duration.
- [sleep(until:tolerance:clock:)](<task/sleep(until_tolerance_clock_).md>) — Suspends the current task until the given deadline within a tolerance.

### Escalating Tasks

- [escalatePriority(to:)](<task/escalatepriority(to_).md>) — Manually escalate the task `priority` of this task to the `newPriority`.

### Comparing Tasks

- [==(_:_:)](<task/==(____).md>) — Returns a Boolean value indicating whether two values are equal.
- [!=(_:_:)](<task/!=(____).md>) — Returns a Boolean value indicating whether two values are not equal.
- [hashValue](task/hashvalue.md) — The hash value.
- [hash(into:)](<task/hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.

### Deprecated

- [Group](task/group.md) _(deprecated)_
- [Handle](task/handle.md) _(deprecated)_
- [Priority](task/priority.md) _(deprecated)_
- [CancellationError()](<task/cancellationerror().md>) _(deprecated)_
- [getResult()](<task/getresult().md>) _(deprecated)_
- [get()](<task/get()-4i2gt.md>) _(deprecated)_
- [get()](<task/get()-4ohks.md>) _(deprecated)_
- [sleep(_:)](<task/sleep(__).md>) _(deprecated)_
- [suspend()](<task/suspend().md>) _(deprecated)_
- [runDetached(priority:operation:)](<task/rundetached(priority_operation_)-88zf5.md>) — Deprecated, available only for source compatibility reasons. _(deprecated)_
- [runDetached(priority:operation:)](<task/rundetached(priority_operation_)-8s8lh.md>) — Deprecated, available only for source compatibility reasons. _(deprecated)_
- [withCancellationHandler(handler:operation:)](<task/withcancellationhandler(handler_operation_).md>) _(deprecated)_
- [withGroup(resultType:returning:body:)](<task/withgroup(resulttype_returning_body_).md>) _(deprecated)_
- [withTaskCancellationHandler(handler:operation:)](<withtaskcancellationhandler(handler_operation_).md>) _(deprecated)_

### Instance Properties

- [name](task/name-swift.property.md) — Return the task’s name, if it was set during its creation. _(beta)_

### Type Properties

- [hasActiveCancellationShield](task/hasactivecancellationshield.md) — Checks if the current task is executing in a scope with a task cancellation shield activated by the `withTaskCancellationShield(operation:)` function. _(beta)_

### Default Implementations

- [Equatable Implementations](task/equatable-implementations.md)
- [Hashable Implementations](task/hashable-implementations.md)

## See Also

### Tasks

- [TaskGroup](taskgroup.md) — A group that contains dynamically created child tasks.
- [withTaskGroup(of:returning:isolation:body:)](<withtaskgroup(of_returning_isolation_body_).md>) — Starts a new scope that can contain a dynamic number of child tasks.
- [ThrowingTaskGroup](throwingtaskgroup.md) — A group that contains throwing, dynamically created child tasks.
- [withThrowingTaskGroup(of:returning:isolation:body:)](<withthrowingtaskgroup(of_returning_isolation_body_).md>) — Starts a new scope that can contain a dynamic number of throwing child tasks.
- [TaskPriority](taskpriority.md) — The priority of a task.
- [DiscardingTaskGroup](discardingtaskgroup.md) — A discarding group that contains dynamically created child tasks.
- [withDiscardingTaskGroup(returning:isolation:body:)](<withdiscardingtaskgroup(returning_isolation_body_).md>) — Starts a new scope that can contain a dynamic number of child tasks.
- [ThrowingDiscardingTaskGroup](throwingdiscardingtaskgroup.md) — A throwing discarding group that contains dynamically created child tasks.
- [withThrowingDiscardingTaskGroup(returning:isolation:body:)](<withthrowingdiscardingtaskgroup(returning_isolation_body_).md>) — Starts a new scope that can contain a dynamic number of child tasks.
- [UnsafeCurrentTask](unsafecurrenttask.md) — An unsafe reference to the current task.

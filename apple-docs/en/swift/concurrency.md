---
title: Concurrency
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/concurrency
source_url: 'https://developer.apple.com/documentation/swift/concurrency'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/concurrency.json'
content_hash: 'sha256:f7263bc70785d335'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md) · [Swift Standard Library](swift-standard-library.md)

# Concurrency

<sub>API Collection</sub>

Perform asynchronous and parallel operations.

## Topics

### Essentials

- [Code-along: Elevating an app with Swift concurrency](code-along-elevating-an-app-with-swift-concurrency.md) — Code along with the WWDC presenter to elevate a SwiftUI app with Swift concurrency.
- [Updating an app to use strict concurrency](updating-an-app-to-use-strict-concurrency.md) — Use this code to follow along with a guide to migrating your code to take advantage of the full concurrency protection that the Swift 6 language mode provides.
- [Updating an App to Use Swift Concurrency](updating_an_app_to_use_swift_concurrency.md) — Improve your app’s performance by refactoring your code to take advantage of asynchronous functions in Swift.

### Tasks

- [Task](task.md) — A unit of asynchronous work.
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

### Asynchronous Sequences

- [AsyncSequence](asyncsequence.md) — A type that provides asynchronous, sequential, iterated access to its elements.
- [AsyncStream](asyncstream.md) — An asynchronous sequence generated from a closure that calls a continuation to produce new elements.
- [AsyncThrowingStream](asyncthrowingstream.md) — An asynchronous sequence generated from an error-throwing closure that calls a continuation to produce new elements.

### Continuations

- [Continuation](continuation.md) — A mechanism to interface between synchronous and asynchronous code, which enforces that the continuation is resumed exactly once. _(beta)_
- [withContinuation(of:_:)](<withcontinuation(of___).md>) — Invokes the passed in closure with a non-copyable continuation for the current task. _(beta)_
- [withContinuation(of:throwing:_:)](<withcontinuation(of_throwing___).md>) — Invokes the passed in closure with a non-copyable continuation for the current task. _(beta)_
- [CheckedContinuation](checkedcontinuation.md) — A mechanism to interface between synchronous and asynchronous code, logging correctness violations.
- [withCheckedContinuation(function:_:)](<withcheckedcontinuation(function___).md>) — Invokes the passed in closure with a checked continuation for the current task.
- [withCheckedThrowingContinuation(function:_:)](<withcheckedthrowingcontinuation(function___)-13yf6.md>)
- [withCheckedThrowingContinuation(function:_:)](<withcheckedthrowingcontinuation(function___)-2k46m.md>) — Invokes the passed in closure with a checked continuation for the current task.
- [UnsafeContinuation](unsafecontinuation.md) — A mechanism to interface between synchronous and asynchronous code, without correctness checking.
- [withUnsafeContinuation(_:)](<withunsafecontinuation(__).md>) — Invokes the passed in closure with a unsafe continuation for the current task.

### Actors

- [Sendable](sendable.md) — A thread-safe type whose values can be shared across arbitrary concurrent contexts without introducing a risk of data races.
- [Actor](actor.md) — Common protocol to which all actors conform.
- [MainActor](mainactor.md) — A singleton actor whose executor is equivalent to the main dispatch queue.
- [GlobalActor](globalactor.md) — A type that represents a globally-unique actor that can be used to isolate various declarations anywhere in the program.
- [SendableMetatype](sendablemetatype.md) — A type whose metatype can be shared across arbitrary isolation domains without introducing a risk of data races.
- [isolation()](<isolation().md>) — Produce a reference to the actor to which the enclosing code is isolated, or `nil` if the code is nonisolated.

### Task-Local Storage

- [TaskLocal](tasklocal.md) — Wrapper type that defines a task-local value key.
- [TaskLocal()](<tasklocal().md>) — Macro that introduces a [TaskLocal](tasklocal.md) binding.

### Executors

- [Executor](executor.md) — A service that can execute jobs.
- [ExecutorJob](executorjob.md) — A unit of schedulable work.
- [SerialExecutor](serialexecutor.md) — A service that executes jobs.
- [TaskExecutor](taskexecutor.md) — An executor that may be used as preferred executor by a task.
- [UnownedJob](unownedjob.md) — A unit of schedulable work.
- [JobPriority](jobpriority.md) — The priority of this job.
- [UnownedSerialExecutor](unownedserialexecutor.md) — An unowned reference to a serial executor (a `SerialExecutor` value).
- [UnownedTaskExecutor](unownedtaskexecutor.md)
- [globalConcurrentExecutor](globalconcurrentexecutor.md) — The global concurrent executor that is used by default for Swift Concurrency tasks.
- [withTaskExecutorPreference(_:isolation:operation:)](<withtaskexecutorpreference(__isolation_operation_).md>) — Configure the current task hierarchy’s task executor preference to the passed [TaskExecutor](taskexecutor.md), and execute the passed in closure by immediately hopping to that executor.

### Deprecated

- [extractIsolation(_:)](<extractisolation(__).md>) _(deprecated)_
- [withCheckedContinuation(isolation:function:_:)](<withcheckedcontinuation(isolation_function___).md>) — Source-compatibility overload; replaced by [withCheckedContinuation(function:_:)](<withcheckedcontinuation(function___).md>). _(deprecated)_
- [withCheckedThrowingContinuation(isolation:function:_:)](<withcheckedthrowingcontinuation(isolation_function___).md>) — Source-compatibility overload; replaced by `withCheckedThrowingContinuation(function:_:)`. _(deprecated)_
- [withUnsafeContinuation(isolation:_:)](<withunsafecontinuation(isolation___).md>) — Source-compatibility overload; replaced by [withUnsafeContinuation(_:)](<withunsafecontinuation(__).md>). _(deprecated)_
- [AnyActor](anyactor.md) — Common marker protocol providing a shared “base” for both (local) `Actor` and (potentially remote) `DistributedActor` types. _(deprecated)_
- [ConcurrentValue](concurrentvalue.md) _(deprecated)_
- [Job](job.md) — Deprecated equivalent of [ExecutorJob](executorjob.md). _(deprecated)_
- [PartialAsyncTask](partialasynctask.md) _(deprecated)_
- [UnsafeConcurrentValue](unsafeconcurrentvalue.md) _(deprecated)_
- [UnsafeSendable](unsafesendable.md) — A type whose values can safely be passed across concurrency domains by copying, but which disables some safety checking at the conformance site. _(deprecated)_
- [UnsafeThrowingContinuation](unsafethrowingcontinuation.md) _(deprecated)_
- [withUnsafeThrowingContinuation(_:)](<withunsafethrowingcontinuation(__)-32nwt.md>) — Invokes the passed in closure with a unsafe continuation for the current task.
- [withUnsafeThrowingContinuation(_:)](<withunsafethrowingcontinuation(__)-7zhvy.md>)
- [withUnsafeThrowingContinuation(isolation:_:)](<withunsafethrowingcontinuation(isolation___).md>) — Source-compatibility overload; replaced by `withUnsafeThrowingContinuation(_:)`. _(deprecated)_

## See Also

### Programming Tasks

- [Input and Output](input-and-output.md) — Print values to the console, read from and write to text streams, and use command line arguments.
- [Debugging and Reflection](debugging-and-reflection.md) — Fortify your code with runtime checks, and examine your values’ runtime representation.
- [Macros](macros.md) — Generate boilerplate code and perform other compile-time operations.
- [Key-Path Expressions](key-path-expressions.md) — Use key-path expressions to access properties dynamically.
- [Manual Memory Management](manual-memory-management.md) — Allocate and manage memory manually.
- [Type Casting and Existential Types](type-casting-and-existential-types.md) — Perform casts between types or represent values of any type.
- [C Interoperability](c-interoperability.md) — Use imported C types or call C variadic functions.
- [Operator Declarations](operator-declarations.md) — Work with prefix, postfix, and infix operators.

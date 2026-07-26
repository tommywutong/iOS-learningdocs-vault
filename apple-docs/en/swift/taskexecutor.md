---
title: TaskExecutor
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/taskexecutor
source_url: 'https://developer.apple.com/documentation/swift/taskexecutor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/taskexecutor.json'
content_hash: 'sha256:45c037b820b55392'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# TaskExecutor

<sub>Protocol</sub>

An executor that may be used as preferred executor by a task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol TaskExecutor : Executor
```

### Impact of setting a task executor preference

By default, without setting a task executor preference, nonisolated asynchronous functions, as well as methods declared on default actors – that is actors which do not require a specific executor – execute on Swift’s default global concurrent executor. This is an executor shared by the entire runtime to execute any work which does not have strict executor requirements.

By setting a task executor preference, either with a `withTaskExecutorPreference(_:operation:)`, creating a task with a preference (`Task(executorPreference:)`, or `group.addTask(executorPreference:)`), the task and all of its child tasks (unless a new preference is set) will be preferring to execute on the provided task executor.

Unstructured tasks do not inherit the task executor.

## Relationships

- **Inherits From**: [Executor](executor.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Instance Methods

- [asUnownedTaskExecutor()](<taskexecutor/asunownedtaskexecutor().md>)
- [enqueue(_:)](<taskexecutor/enqueue(__)-30ge1.md>)
- [enqueue(_:)](<taskexecutor/enqueue(__)-6vkr9.md>) _(deprecated)_
- [enqueue(_:)](<taskexecutor/enqueue(__)-91eir.md>)

## See Also

### Executors

- [Executor](executor.md) — A service that can execute jobs.
- [ExecutorJob](executorjob.md) — A unit of schedulable work.
- [SerialExecutor](serialexecutor.md) — A service that executes jobs.
- [UnownedJob](unownedjob.md) — A unit of schedulable work.
- [JobPriority](jobpriority.md) — The priority of this job.
- [UnownedSerialExecutor](unownedserialexecutor.md) — An unowned reference to a serial executor (a `SerialExecutor` value).
- [UnownedTaskExecutor](unownedtaskexecutor.md)
- [globalConcurrentExecutor](globalconcurrentexecutor.md) — The global concurrent executor that is used by default for Swift Concurrency tasks.
- [withTaskExecutorPreference(_:isolation:operation:)](<withtaskexecutorpreference(__isolation_operation_).md>) — Configure the current task hierarchy’s task executor preference to the passed [TaskExecutor](taskexecutor.md), and execute the passed in closure by immediately hopping to that executor.

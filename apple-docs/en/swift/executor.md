---
title: Executor
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/executor
source_url: 'https://developer.apple.com/documentation/swift/executor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/executor.json'
content_hash: 'sha256:f1342d38b5d27ab2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Executor

<sub>Protocol</sub>

A service that can execute jobs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol Executor : AnyObject, Sendable
```

## Relationships

- **Inherits From**: [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

- **Inherited By**: [SerialExecutor](serialexecutor.md), [TaskExecutor](taskexecutor.md)

## Topics

### Instance Methods

- [enqueue(_:)](<executor/enqueue(__)-2sc5t.md>) _(deprecated)_
- [enqueue(_:)](<executor/enqueue(__)-55qpq.md>)
- [enqueue(_:)](<executor/enqueue(__)-b90u.md>)

## See Also

### Executors

- [ExecutorJob](executorjob.md) — A unit of schedulable work.
- [SerialExecutor](serialexecutor.md) — A service that executes jobs.
- [TaskExecutor](taskexecutor.md) — An executor that may be used as preferred executor by a task.
- [UnownedJob](unownedjob.md) — A unit of schedulable work.
- [JobPriority](jobpriority.md) — The priority of this job.
- [UnownedSerialExecutor](unownedserialexecutor.md) — An unowned reference to a serial executor (a `SerialExecutor` value).
- [UnownedTaskExecutor](unownedtaskexecutor.md)
- [globalConcurrentExecutor](globalconcurrentexecutor.md) — The global concurrent executor that is used by default for Swift Concurrency tasks.
- [withTaskExecutorPreference(_:isolation:operation:)](<withtaskexecutorpreference(__isolation_operation_).md>) — Configure the current task hierarchy’s task executor preference to the passed [TaskExecutor](taskexecutor.md), and execute the passed in closure by immediately hopping to that executor.

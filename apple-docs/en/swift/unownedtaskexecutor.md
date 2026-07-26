---
title: UnownedTaskExecutor
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unownedtaskexecutor
source_url: 'https://developer.apple.com/documentation/swift/unownedtaskexecutor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unownedtaskexecutor.json'
content_hash: 'sha256:3cb6886cfa8e7a42'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# UnownedTaskExecutor

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct UnownedTaskExecutor
```

## Relationships

- **Conforms To**: [BitwiseCopyable](bitwisecopyable.md), [Copyable](copyable.md), [Equatable](equatable.md), [Hashable](hashable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Initializers

- [init(_:)](<unownedtaskexecutor/init(__)-55b8h.md>)
- [init(_:)](<unownedtaskexecutor/init(__)-5pjm5.md>)
- [init(ordinary:)](<unownedtaskexecutor/init(ordinary_).md>)

### Instance Methods

- [asTaskExecutor()](<unownedtaskexecutor/astaskexecutor().md>)

### Default Implementations

- [Equatable Implementations](unownedtaskexecutor/equatable-implementations.md)
- [Hashable Implementations](unownedtaskexecutor/hashable-implementations.md)

## See Also

### Executors

- [Executor](executor.md) — A service that can execute jobs.
- [ExecutorJob](executorjob.md) — A unit of schedulable work.
- [SerialExecutor](serialexecutor.md) — A service that executes jobs.
- [TaskExecutor](taskexecutor.md) — An executor that may be used as preferred executor by a task.
- [UnownedJob](unownedjob.md) — A unit of schedulable work.
- [JobPriority](jobpriority.md) — The priority of this job.
- [UnownedSerialExecutor](unownedserialexecutor.md) — An unowned reference to a serial executor (a `SerialExecutor` value).
- [globalConcurrentExecutor](globalconcurrentexecutor.md) — The global concurrent executor that is used by default for Swift Concurrency tasks.
- [withTaskExecutorPreference(_:isolation:operation:)](<withtaskexecutorpreference(__isolation_operation_).md>) — Configure the current task hierarchy’s task executor preference to the passed [TaskExecutor](taskexecutor.md), and execute the passed in closure by immediately hopping to that executor.

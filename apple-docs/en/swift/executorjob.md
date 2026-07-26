---
title: ExecutorJob
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/executorjob
source_url: 'https://developer.apple.com/documentation/swift/executorjob'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/executorjob.json'
content_hash: 'sha256:daaf572573197d7b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# ExecutorJob

<sub>Structure</sub>

A unit of schedulable work.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct ExecutorJob
```

## Overview

Unless you’re implementing a scheduler, you don’t generally interact with jobs directly.

## Relationships

- **Conforms To**: [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Initializers

- [init(_:)](<executorjob/init(__)-2yixs.md>)
- [init(_:)](<executorjob/init(__)-36632.md>)

### Instance Properties

- [description](executorjob/description.md)
- [priority](executorjob/priority.md)

### Instance Methods

- [runSynchronously(isolatedTo:taskExecutor:)](<executorjob/runsynchronously(isolatedto_taskexecutor_).md>) — Run this job isolated to the passed in serial executor, while executing it on the specified task executor.
- [runSynchronously(on:)](<executorjob/runsynchronously(on_)-6e565.md>) — Run this job on the passed in task executor.
- [runSynchronously(on:)](<executorjob/runsynchronously(on_)-9dhs1.md>) — Run this job on the passed in executor.

## See Also

### Executors

- [Executor](executor.md) — A service that can execute jobs.
- [SerialExecutor](serialexecutor.md) — A service that executes jobs.
- [TaskExecutor](taskexecutor.md) — An executor that may be used as preferred executor by a task.
- [UnownedJob](unownedjob.md) — A unit of schedulable work.
- [JobPriority](jobpriority.md) — The priority of this job.
- [UnownedSerialExecutor](unownedserialexecutor.md) — An unowned reference to a serial executor (a `SerialExecutor` value).
- [UnownedTaskExecutor](unownedtaskexecutor.md)
- [globalConcurrentExecutor](globalconcurrentexecutor.md) — The global concurrent executor that is used by default for Swift Concurrency tasks.
- [withTaskExecutorPreference(_:isolation:operation:)](<withtaskexecutorpreference(__isolation_operation_).md>) — Configure the current task hierarchy’s task executor preference to the passed [TaskExecutor](taskexecutor.md), and execute the passed in closure by immediately hopping to that executor.

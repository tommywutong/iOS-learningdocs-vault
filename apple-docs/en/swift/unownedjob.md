---
title: UnownedJob
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unownedjob
source_url: 'https://developer.apple.com/documentation/swift/unownedjob'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unownedjob.json'
content_hash: 'sha256:881a6cb9d3504029'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# UnownedJob

<sub>Structure</sub>

A unit of schedulable work.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct UnownedJob
```

## Overview

Unless you’re implementing a scheduler, you don’t generally interact with jobs directly.

An `UnownedJob` must be eventually run _exactly once_ using `runSynchronously(on:)`. Not doing so is effectively going to leak and “hang” the work that the job represents (e.g. a [Task](task.md)).

## Relationships

- **Conforms To**: [BitwiseCopyable](bitwisecopyable.md), [Copyable](copyable.md), [CustomStringConvertible](customstringconvertible.md), [Escapable](escapable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Initializers

- [init(_:)](<unownedjob/init(__)-8ra8c.md>) — Create an `UnownedJob` whose lifetime must be managed carefully until it is run exactly once.
- [init(_:)](<unownedjob/init(__)-9f1zn.md>) — Create an `UnownedJob` whose lifetime must be managed carefully until it is run exactly once.

### Instance Properties

- [priority](unownedjob/priority.md) — The priority of this job.

### Instance Methods

- [runSynchronously(isolatedTo:taskExecutor:)](<unownedjob/runsynchronously(isolatedto_taskexecutor_).md>) — Run this job isolated to the passed in serial executor, while executing it on the specified task executor.
- [runSynchronously(on:)](<unownedjob/runsynchronously(on_)-4eaxu.md>) — Run this job isolated to the passed task executor.
- [runSynchronously(on:)](<unownedjob/runsynchronously(on_)-o1nb.md>) — Run this job on the passed in executor.

### Default Implementations

- [CustomStringConvertible Implementations](unownedjob/customstringconvertible-implementations.md)

## See Also

### Executors

- [Executor](executor.md) — A service that can execute jobs.
- [ExecutorJob](executorjob.md) — A unit of schedulable work.
- [SerialExecutor](serialexecutor.md) — A service that executes jobs.
- [TaskExecutor](taskexecutor.md) — An executor that may be used as preferred executor by a task.
- [JobPriority](jobpriority.md) — The priority of this job.
- [UnownedSerialExecutor](unownedserialexecutor.md) — An unowned reference to a serial executor (a `SerialExecutor` value).
- [UnownedTaskExecutor](unownedtaskexecutor.md)
- [globalConcurrentExecutor](globalconcurrentexecutor.md) — The global concurrent executor that is used by default for Swift Concurrency tasks.
- [withTaskExecutorPreference(_:isolation:operation:)](<withtaskexecutorpreference(__isolation_operation_).md>) — Configure the current task hierarchy’s task executor preference to the passed [TaskExecutor](taskexecutor.md), and execute the passed in closure by immediately hopping to that executor.

---
title: JobPriority
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/jobpriority
source_url: 'https://developer.apple.com/documentation/swift/jobpriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/jobpriority.json'
content_hash: 'sha256:e522830a6e4f6549'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# JobPriority

<sub>Structure</sub>

The priority of this job.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct JobPriority
```

## Overview

The executor determines how priority information affects the way tasks are scheduled. The behavior varies depending on the executor currently being used. Typically, executors attempt to run tasks with a higher priority before tasks with a lower priority. However, the semantics of how priority is treated are left up to each platform and `Executor` implementation.

A ExecutorJob’s priority is roughly equivalent to a `TaskPriority`, however, since not all jobs are tasks, represented as separate type.

Conversions between the two priorities are available as initializers on the respective types.

## Relationships

- **Conforms To**: [BitwiseCopyable](bitwisecopyable.md), [Comparable](comparable.md), [Copyable](copyable.md), [Equatable](equatable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Operators

- [!=(_:_:)](<jobpriority/!=(____).md>)

### Initializers

- [init(_:)](<jobpriority/init(__).md>) — Construct from a TaskPriority
- [init(rawValue:)](<jobpriority/init(rawvalue_).md>) — Construct from a raw value

### Instance Properties

- [rawValue](jobpriority/rawvalue-swift.property.md) — The raw priority value.

### Type Aliases

- [RawValue](jobpriority/rawvalue-swift.typealias.md)

### Default Implementations

- [Comparable Implementations](jobpriority/comparable-implementations.md)
- [Equatable Implementations](jobpriority/equatable-implementations.md)

## See Also

### Executors

- [Executor](executor.md) — A service that can execute jobs.
- [ExecutorJob](executorjob.md) — A unit of schedulable work.
- [SerialExecutor](serialexecutor.md) — A service that executes jobs.
- [TaskExecutor](taskexecutor.md) — An executor that may be used as preferred executor by a task.
- [UnownedJob](unownedjob.md) — A unit of schedulable work.
- [UnownedSerialExecutor](unownedserialexecutor.md) — An unowned reference to a serial executor (a `SerialExecutor` value).
- [UnownedTaskExecutor](unownedtaskexecutor.md)
- [globalConcurrentExecutor](globalconcurrentexecutor.md) — The global concurrent executor that is used by default for Swift Concurrency tasks.
- [withTaskExecutorPreference(_:isolation:operation:)](<withtaskexecutorpreference(__isolation_operation_).md>) — Configure the current task hierarchy’s task executor preference to the passed [TaskExecutor](taskexecutor.md), and execute the passed in closure by immediately hopping to that executor.

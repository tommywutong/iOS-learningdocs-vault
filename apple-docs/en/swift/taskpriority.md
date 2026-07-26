---
title: TaskPriority
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/taskpriority
source_url: 'https://developer.apple.com/documentation/swift/taskpriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/taskpriority.json'
content_hash: 'sha256:8292f936cd7ebbf3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# TaskPriority

<sub>Structure</sub>

The priority of a task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TaskPriority
```

## Overview

The executor determines how priority information affects the way tasks are scheduled. The behavior varies depending on the executor currently being used. Typically, executors attempt to run tasks with a higher priority before tasks with a lower priority. However, the semantics of how priority is treated are left up to each platform and `Executor` implementation.

Child tasks automatically inherit their parent task’s priority. Detached tasks created by `detach(priority:operation:)` don’t inherit task priority because they aren’t attached to the current task.

In some situations the priority of a task is elevated — that is, the task is treated as it if had a higher priority, without actually changing the priority of the task:

- If a task runs on behalf of an actor, and a new higher-priority task is enqueued to the actor, then the actor’s current task is temporarily elevated to the priority of the enqueued task. This priority elevation allows the new task to be processed at the priority it was enqueued with.
- If a higher-priority task accesses the `value` property, then the priority of this task increases until the task completes.

In both cases, priority elevation helps you prevent a low-priority task from blocking the execution of a high priority task, which is also known as _priority inversion_.

## Relationships

- **Conforms To**: [Comparable](comparable.md), [Copyable](copyable.md), [CustomStringConvertible](customstringconvertible.md), [Decodable](decodable.md), [Encodable](encodable.md), [Equatable](equatable.md), [Escapable](escapable.md), [RawRepresentable](rawrepresentable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Operators

- [!=(_:_:)](<taskpriority/!=(____).md>)

### Initializers

- [init(_:)](<taskpriority/init(__).md>) — Convert this `UnownedJob/Priority` to a [TaskPriority](taskpriority.md).
- [init(rawValue:)](<taskpriority/init(rawvalue_).md>) — Creates a new instance with the specified raw value.

### Instance Properties

- [rawValue](taskpriority/rawvalue-swift.property.md) — The corresponding value of the raw type.

### Type Aliases

- [RawValue](taskpriority/rawvalue-swift.typealias.md) — The raw type that can be used to represent all values of the conforming type.

### Type Properties

- [background](taskpriority/background.md)
- [default](taskpriority/default.md) _(deprecated)_
- [high](taskpriority/high.md)
- [low](taskpriority/low.md)
- [medium](taskpriority/medium.md)
- [unspecified](taskpriority/unspecified.md) _(deprecated)_
- [userInitiated](taskpriority/userinitiated.md)
- [userInteractive](taskpriority/userinteractive.md) _(deprecated)_
- [utility](taskpriority/utility.md)

### Default Implementations

- [Comparable Implementations](taskpriority/comparable-implementations.md)
- [CustomStringConvertible Implementations](taskpriority/customstringconvertible-implementations.md)
- [Equatable Implementations](taskpriority/equatable-implementations.md)
- [RawRepresentable Implementations](taskpriority/rawrepresentable-implementations.md)

## See Also

### Tasks

- [Task](task.md) — A unit of asynchronous work.
- [TaskGroup](taskgroup.md) — A group that contains dynamically created child tasks.
- [withTaskGroup(of:returning:isolation:body:)](<withtaskgroup(of_returning_isolation_body_).md>) — Starts a new scope that can contain a dynamic number of child tasks.
- [ThrowingTaskGroup](throwingtaskgroup.md) — A group that contains throwing, dynamically created child tasks.
- [withThrowingTaskGroup(of:returning:isolation:body:)](<withthrowingtaskgroup(of_returning_isolation_body_).md>) — Starts a new scope that can contain a dynamic number of throwing child tasks.
- [DiscardingTaskGroup](discardingtaskgroup.md) — A discarding group that contains dynamically created child tasks.
- [withDiscardingTaskGroup(returning:isolation:body:)](<withdiscardingtaskgroup(returning_isolation_body_).md>) — Starts a new scope that can contain a dynamic number of child tasks.
- [ThrowingDiscardingTaskGroup](throwingdiscardingtaskgroup.md) — A throwing discarding group that contains dynamically created child tasks.
- [withThrowingDiscardingTaskGroup(returning:isolation:body:)](<withthrowingdiscardingtaskgroup(returning_isolation_body_).md>) — Starts a new scope that can contain a dynamic number of child tasks.
- [UnsafeCurrentTask](unsafecurrenttask.md) — An unsafe reference to the current task.

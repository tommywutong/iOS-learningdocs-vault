---
title: ThrowingDiscardingTaskGroup
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/throwingdiscardingtaskgroup
source_url: 'https://developer.apple.com/documentation/swift/throwingdiscardingtaskgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/throwingdiscardingtaskgroup.json'
content_hash: 'sha256:123bccc326c55cf9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# ThrowingDiscardingTaskGroup

<sub>Structure</sub>

A throwing discarding group that contains dynamically created child tasks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct ThrowingDiscardingTaskGroup<Failure> where Failure : Error
```

## Overview

To create a discarding task group, call the `withDiscardingTaskGroup(returning:body:)` method.

Don’t use a task group from outside the task where you created it. In most cases, the Swift type system prevents a task group from escaping like that because adding a child task to a task group is a mutating operation, and mutation operations can’t be performed from a concurrent execution context like a child task.

Refer to [TaskGroup](taskgroup.md) documentation for detailed discussion of semantics shared between all task groups.

### Discarding behavior

A discarding task group eagerly discards and releases its child tasks as soon as they complete. This allows for the efficient releasing of memory used by those tasks, which are not retained for future `next()` calls, as would be the case with a [TaskGroup](taskgroup.md).

### Cancellation behavior

A throwing discarding task group becomes canceled in one of the following ways:

- when [cancelAll()](<throwingdiscardingtaskgroup/cancelall().md>) is invoked on it,
- when an error is thrown out of the `withThrowingDiscardingTaskGroup { ... }` closure,
- when the [Task](task.md) running this task group is canceled.

But also, and uniquely in _discarding_ task groups:

- when _any_ of its child tasks throws.

The group becoming canceled automatically, and cancelling all of its child tasks, whenever _any_ child task throws an error is a behavior unique to discarding task groups, because achieving such semantics is not possible otherwise, due to the missing `next()` method on discarding groups. Accumulating task groups can implement this by manually polling `next()` and deciding to `cancelAll()` when they decide an error should cause the group to become canceled, however a discarding group cannot poll child tasks for results and therefore assumes that child task throws are an indication of a group wide failure. In order to avoid such behavior, use a [DiscardingTaskGroup](discardingtaskgroup.md) instead of a throwing one, or catch specific errors in operations submitted using `addTask`.

Since a `ThrowingDiscardingTaskGroup` is a structured concurrency primitive, cancellation is automatically propagated through all of its child-tasks (and their child tasks).

A canceled task group can still keep adding tasks, however they will start being immediately canceled, and may act accordingly to this. To avoid adding new tasks to an already canceled task group, use `addTaskUnlessCancelled(priority:body:)` rather than the plain `addTask(priority:body:)` which adds tasks unconditionally.

For information about the language-level concurrency model that `DiscardingTaskGroup` is part of, see [Concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/).

> [!info] See Also
> [TaskGroup](taskgroup.md)

> [!info] See Also
> [ThrowingTaskGroup](throwingtaskgroup.md)

> [!info] See Also
> [DiscardingTaskGroup](discardingtaskgroup.md)

## Relationships

- **Conforms To**: [BitwiseCopyable](bitwisecopyable.md), [Copyable](copyable.md)

## Topics

### Instance Properties

- [isCancelled](throwingdiscardingtaskgroup/iscancelled.md) — A Boolean value that indicates whether the group was canceled.
- [isEmpty](throwingdiscardingtaskgroup/isempty.md) — A Boolean value that indicates whether the group has any remaining tasks.

### Instance Methods

- [addImmediateTask(name:priority:executorPreference:operation:)](<throwingdiscardingtaskgroup/addimmediatetask(name_priority_executorpreference_operation_).md>) — Add a child task to the group and immediately start running it in the context of the calling thread/task.
- [addImmediateTaskUnlessCancelled(name:priority:executorPreference:operation:)](<throwingdiscardingtaskgroup/addimmediatetaskunlesscancelled(name_priority_executorpreference_operation_).md>) — Add a child task to the group and immediately start running it in the context of the calling thread/task.
- [addTask(executorPreference:priority:operation:)](<throwingdiscardingtaskgroup/addtask(executorpreference_priority_operation_).md>) — Adds a child task to the group.
- [addTask(name:executorPreference:priority:operation:)](<throwingdiscardingtaskgroup/addtask(name_executorpreference_priority_operation_).md>) — Adds a child task to the group.
- [addTask(name:priority:operation:)](<throwingdiscardingtaskgroup/addtask(name_priority_operation_).md>) — Adds a child task to the group.
- [addTask(priority:operation:)](<throwingdiscardingtaskgroup/addtask(priority_operation_).md>) — Adds a child task to the group.
- [addTaskUnlessCancelled(executorPreference:priority:operation:)](<throwingdiscardingtaskgroup/addtaskunlesscancelled(executorpreference_priority_operation_).md>) — Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [addTaskUnlessCancelled(name:executorPreference:priority:operation:)](<throwingdiscardingtaskgroup/addtaskunlesscancelled(name_executorpreference_priority_operation_).md>) — Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [addTaskUnlessCancelled(name:priority:operation:)](<throwingdiscardingtaskgroup/addtaskunlesscancelled(name_priority_operation_).md>) — Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [addTaskUnlessCancelled(priority:operation:)](<throwingdiscardingtaskgroup/addtaskunlesscancelled(priority_operation_).md>) — Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [cancelAll()](<throwingdiscardingtaskgroup/cancelall().md>) — Cancel all of the remaining tasks in the group.

## See Also

### Tasks

- [Task](task.md) — A unit of asynchronous work.
- [TaskGroup](taskgroup.md) — A group that contains dynamically created child tasks.
- [withTaskGroup(of:returning:isolation:body:)](<withtaskgroup(of_returning_isolation_body_).md>) — Starts a new scope that can contain a dynamic number of child tasks.
- [ThrowingTaskGroup](throwingtaskgroup.md) — A group that contains throwing, dynamically created child tasks.
- [withThrowingTaskGroup(of:returning:isolation:body:)](<withthrowingtaskgroup(of_returning_isolation_body_).md>) — Starts a new scope that can contain a dynamic number of throwing child tasks.
- [TaskPriority](taskpriority.md) — The priority of a task.
- [DiscardingTaskGroup](discardingtaskgroup.md) — A discarding group that contains dynamically created child tasks.
- [withDiscardingTaskGroup(returning:isolation:body:)](<withdiscardingtaskgroup(returning_isolation_body_).md>) — Starts a new scope that can contain a dynamic number of child tasks.
- [withThrowingDiscardingTaskGroup(returning:isolation:body:)](<withthrowingdiscardingtaskgroup(returning_isolation_body_).md>) — Starts a new scope that can contain a dynamic number of child tasks.
- [UnsafeCurrentTask](unsafecurrenttask.md) — An unsafe reference to the current task.

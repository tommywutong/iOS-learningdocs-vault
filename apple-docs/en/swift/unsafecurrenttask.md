---
title: UnsafeCurrentTask
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsafecurrenttask
source_url: 'https://developer.apple.com/documentation/swift/unsafecurrenttask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafecurrenttask.json'
content_hash: 'sha256:13a807c2ddb839c3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# UnsafeCurrentTask

<sub>Structure</sub>

An unsafe reference to the current task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct UnsafeCurrentTask
```

## Overview

To get an instance of `UnsafeCurrentTask` for the current task, call the `withUnsafeCurrentTask(body:)` method. Don’t store an unsafe task reference for use outside that method’s closure. Storing an unsafe reference doesn’t affect the task’s actual life cycle, and the behavior of accessing an unsafe task reference outside of the `withUnsafeCurrentTask(body:)` method’s closure isn’t defined.

Only APIs on `UnsafeCurrentTask` that are also part of `Task` are safe to invoke from a task other than the task that this `UnsafeCurrentTask` instance refers to. Calling other APIs from another task is undefined behavior, breaks invariants in other parts of the program running on this task, and may lead to crashes or data loss.

For information about the language-level concurrency model that `UnsafeCurrentTask` is part of, see [Concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/).

## Relationships

- **Conforms To**: [Equatable](equatable.md), [Hashable](hashable.md)

## Topics

### Getting an Unsafe Reference to the Current Task

- [withUnsafeCurrentTask(body:)](<withunsafecurrenttask(body_)-6gvhl.md>) — Calls a closure with an unsafe reference to the current task.
- [withUnsafeCurrentTask(body:)](<withunsafecurrenttask(body_)-udlb.md>) — Calls a closure with an unsafe reference to the current task.

### Instance Properties

- [basePriority](unsafecurrenttask/basepriority.md) — The current task’s base priority.
- [hasActiveCancellationShield](unsafecurrenttask/hasactivecancellationshield.md) — Checks if this task is executing in a scope with a task cancellation shield activated by the `withTaskCancellationShield(operation:)` function. _(beta)_
- [isCancelled](unsafecurrenttask/iscancelled.md) — A Boolean value that indicates whether the current task was canceled.
- [name](unsafecurrenttask/name.md) — Return the task’s name, if it was set during its creation. _(beta)_
- [priority](unsafecurrenttask/priority.md) — The current task’s priority.
- [unownedTaskExecutor](unsafecurrenttask/unownedtaskexecutor.md) — The current [TaskExecutor](taskexecutor.md) preference, if this task has one configured.

### Instance Methods

- [cancel()](<unsafecurrenttask/cancel().md>) — Cancel the current task.
- [escalatePriority(to:)](<unsafecurrenttask/escalatepriority(to_).md>) — Escalate the task `priority` of the passed in task to the `newPriority`.

### Default Implementations

- [Equatable Implementations](unsafecurrenttask/equatable-implementations.md)
- [Hashable Implementations](unsafecurrenttask/hashable-implementations.md)

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
- [ThrowingDiscardingTaskGroup](throwingdiscardingtaskgroup.md) — A throwing discarding group that contains dynamically created child tasks.
- [withThrowingDiscardingTaskGroup(returning:isolation:body:)](<withthrowingdiscardingtaskgroup(returning_isolation_body_).md>) — Starts a new scope that can contain a dynamic number of child tasks.

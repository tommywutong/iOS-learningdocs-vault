---
title: ThrowingTaskGroup
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/throwingtaskgroup
source_url: 'https://developer.apple.com/documentation/swift/throwingtaskgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/throwingtaskgroup.json'
content_hash: 'sha256:0a9c69bed4d6292c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# ThrowingTaskGroup

<sub>Structure</sub>

A group that contains throwing, dynamically created child tasks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct ThrowingTaskGroup<ChildTaskResult, Failure> where ChildTaskResult : Sendable, Failure : Error
```

## Overview

To create a throwing task group, call the `withThrowingTaskGroup(of:returning:body:)` method.

Don’t use a task group from outside the task where you created it. In most cases, the Swift type system prevents a task group from escaping like that because adding a child task to a task group is a mutating operation, and mutation operations can’t be performed from concurrent execution contexts like a child task.

Refer to [TaskGroup](taskgroup.md) documentation for detailed discussion of semantics shared between all task groups.

### Cancellation behavior

A task group becomes canceled in one of the following ways:

- when [cancelAll()](<throwingtaskgroup/cancelall().md>) is invoked on it,
- when an error is thrown out of the `withThrowingTaskGroup(...) { }` closure,
- when the [Task](task.md) running this task group is canceled.

Since a `ThrowingTaskGroup` is a structured concurrency primitive, cancellation is automatically propagated through all of its child-tasks (and their child tasks).

A canceled task group can still keep adding tasks, however they will start being immediately canceled, and may act accordingly to this. To avoid adding new tasks to an already canceled task group, use `addTaskUnlessCancelled(priority:body:)` rather than the plain `addTask(priority:body:)` which adds tasks unconditionally.

For information about the language-level concurrency model that `ThrowingTaskGroup` is part of, see [Concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/).

> [!info] See Also
> [TaskGroup](taskgroup.md)

> [!info] See Also
> [DiscardingTaskGroup](discardingtaskgroup.md)

> [!info] See Also
> [ThrowingDiscardingTaskGroup](throwingdiscardingtaskgroup.md)

## Relationships

- **Conforms To**: [AsyncSequence](asyncsequence.md), [BitwiseCopyable](bitwisecopyable.md), [Copyable](copyable.md), [Escapable](escapable.md)

## Topics

### Adding Tasks to a Throwing Task Group

- [addTask(priority:operation:)](<throwingtaskgroup/addtask(priority_operation_).md>) — Adds a child task to the group.
- [addTask(executorPreference:priority:operation:)](<throwingtaskgroup/addtask(executorpreference_priority_operation_).md>) — Adds a child task to the group.
- [addTask(name:priority:operation:)](<throwingtaskgroup/addtask(name_priority_operation_).md>) — Adds a child task to the group.
- [addTask(name:executorPreference:priority:operation:)](<throwingtaskgroup/addtask(name_executorpreference_priority_operation_).md>) — Adds a child task to the group.
- [addTaskUnlessCancelled(priority:operation:)](<throwingtaskgroup/addtaskunlesscancelled(priority_operation_).md>) — Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [addTaskUnlessCancelled(name:executorPreference:priority:operation:)](<throwingtaskgroup/addtaskunlesscancelled(name_executorpreference_priority_operation_).md>) — Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [addTaskUnlessCancelled(executorPreference:priority:operation:)](<throwingtaskgroup/addtaskunlesscancelled(executorpreference_priority_operation_).md>) — Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [addTaskUnlessCancelled(name:priority:operation:)](<throwingtaskgroup/addtaskunlesscancelled(name_priority_operation_).md>) — Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [addImmediateTask(name:priority:executorPreference:operation:)](<throwingtaskgroup/addimmediatetask(name_priority_executorpreference_operation_).md>) — Add a child task to the group and immediately start running it in the context of the calling thread/task.
- [addImmediateTaskUnlessCancelled(name:priority:executorPreference:operation:)](<throwingtaskgroup/addimmediatetaskunlesscancelled(name_priority_executorpreference_operation_).md>) — Add a child task to the group and immediately start running it in the context of the calling thread/task.

### Accessing Individual Results

- [next()](<throwingtaskgroup/next().md>)
- [nextResult()](<throwingtaskgroup/nextresult().md>) — Wait for the next child task to complete, and return a result containing either the value that the child task returned or the error that it threw.
- [next(isolation:)](<throwingtaskgroup/next(isolation_).md>) — Wait for the next child task to complete, and return the value it returned or rethrow the error it threw.
- [isEmpty](throwingtaskgroup/isempty.md) — A Boolean value that indicates whether the group has any remaining tasks.
- [waitForAll()](<throwingtaskgroup/waitforall().md>) — Wait for all of the group’s remaining tasks to complete.

### Accessing an Asynchronous Sequence of Results

- [makeAsyncIterator()](<throwingtaskgroup/makeasynciterator().md>) — Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [allSatisfy(_:)](<throwingtaskgroup/allsatisfy(__).md>) — Returns a Boolean value that indicates whether all elements produced by the asynchronous sequence satisfy the given predicate.
- [compactMap(_:)](<throwingtaskgroup/compactmap(__)-944nh.md>) — Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [compactMap(_:)](<throwingtaskgroup/compactmap(__)-7mgi5.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [contains(_:)](<throwingtaskgroup/contains(__).md>) — Returns a Boolean value that indicates whether the asynchronous sequence contains the given element.
- [contains(where:)](<throwingtaskgroup/contains(where_).md>) — Returns a Boolean value that indicates whether the asynchronous sequence contains an element that satisfies the given predicate.
- [drop(while:)](<throwingtaskgroup/drop(while_).md>) — Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [dropFirst(_:)](<throwingtaskgroup/dropfirst(__).md>) — Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [filter(_:)](<throwingtaskgroup/filter(__).md>) — Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.
- [first(where:)](<throwingtaskgroup/first(where_).md>) — Returns the first element of the sequence that satisfies the given predicate.
- [map(_:)](<throwingtaskgroup/map(__)-58nrv.md>) — Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [map(_:)](<throwingtaskgroup/map(__)-4a4ju.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [max()](<throwingtaskgroup/max().md>) — Returns the maximum element in an asynchronous sequence of comparable elements.
- [max(by:)](<throwingtaskgroup/max(by_).md>) — Returns the maximum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [min()](<throwingtaskgroup/min().md>) — Returns the minimum element in an asynchronous sequence of comparable elements.
- [min(by:)](<throwingtaskgroup/min(by_).md>) — Returns the minimum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [prefix(_:)](<throwingtaskgroup/prefix(__).md>) — Returns an asynchronous sequence, up to the specified maximum length, containing the initial elements of the base asynchronous sequence.
- [prefix(while:)](<throwingtaskgroup/prefix(while_).md>) — Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given predicate.
- [reduce(_:_:)](<throwingtaskgroup/reduce(____).md>) — Returns the result of combining the elements of the asynchronous sequence using the given closure.
- [reduce(into:_:)](<throwingtaskgroup/reduce(into___).md>) — Returns the result of combining the elements of the asynchronous sequence using the given closure, given a mutable initial value.

### Canceling Tasks

- [isCancelled](throwingtaskgroup/iscancelled.md) — A Boolean value that indicates whether the group was canceled.
- [cancelAll()](<throwingtaskgroup/cancelall().md>) — Cancel all of the remaining tasks in the group.

### Supporting Types

- [Element](throwingtaskgroup/element.md) — The type of element produced by this asynchronous sequence.
- [Iterator](throwingtaskgroup/iterator.md) — A type that provides an iteration interface over the results of tasks added to the group.
- [AsyncIterator](throwingtaskgroup/asynciterator.md) — The type of asynchronous iterator that produces elements of this asynchronous sequence.

### Deprecated

- [add(priority:operation:)](<throwingtaskgroup/add(priority_operation_).md>) _(deprecated)_
- [async(priority:operation:)](<throwingtaskgroup/async(priority_operation_).md>) _(deprecated)_
- [asyncUnlessCancelled(priority:operation:)](<throwingtaskgroup/asyncunlesscancelled(priority_operation_).md>) _(deprecated)_
- [nextResult(isolation:)](<throwingtaskgroup/nextresult(isolation_).md>) _(deprecated)_
- [spawn(priority:operation:)](<throwingtaskgroup/spawn(priority_operation_).md>) _(deprecated)_
- [spawnUnlessCancelled(priority:operation:)](<throwingtaskgroup/spawnunlesscancelled(priority_operation_).md>) _(deprecated)_
- [waitForAll(isolation:)](<throwingtaskgroup/waitforall(isolation_).md>) _(deprecated)_

### Default Implementations

- [AsyncSequence Implementations](throwingtaskgroup/asyncsequence-implementations.md)

## See Also

### Tasks

- [Task](task.md) — A unit of asynchronous work.
- [TaskGroup](taskgroup.md) — A group that contains dynamically created child tasks.
- [withTaskGroup(of:returning:isolation:body:)](<withtaskgroup(of_returning_isolation_body_).md>) — Starts a new scope that can contain a dynamic number of child tasks.
- [withThrowingTaskGroup(of:returning:isolation:body:)](<withthrowingtaskgroup(of_returning_isolation_body_).md>) — Starts a new scope that can contain a dynamic number of throwing child tasks.
- [TaskPriority](taskpriority.md) — The priority of a task.
- [DiscardingTaskGroup](discardingtaskgroup.md) — A discarding group that contains dynamically created child tasks.
- [withDiscardingTaskGroup(returning:isolation:body:)](<withdiscardingtaskgroup(returning_isolation_body_).md>) — Starts a new scope that can contain a dynamic number of child tasks.
- [ThrowingDiscardingTaskGroup](throwingdiscardingtaskgroup.md) — A throwing discarding group that contains dynamically created child tasks.
- [withThrowingDiscardingTaskGroup(returning:isolation:body:)](<withthrowingdiscardingtaskgroup(returning_isolation_body_).md>) — Starts a new scope that can contain a dynamic number of child tasks.
- [UnsafeCurrentTask](unsafecurrenttask.md) — An unsafe reference to the current task.

---
title: 'withThrowingTaskGroup(of:returning:isolation:body:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/withthrowingtaskgroup(of:returning:isolation:body:)'
source_url: 'https://developer.apple.com/documentation/swift/withthrowingtaskgroup(of:returning:isolation:body:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/withthrowingtaskgroup%28of%3Areturning%3Aisolation%3Abody%3A%29.json'
content_hash: 'sha256:03a5e6ca974d7400'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# withThrowingTaskGroup(of:returning:isolation:body:)

<sub>Function</sub>

Starts a new scope that can contain a dynamic number of throwing child tasks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: macOS 15.0, iOS 18.0, watchOS 11.0, tvOS 18.0, visionOS 2.0)
func withThrowingTaskGroup<ChildTaskResult, GroupResult>(of childTaskResultType: ChildTaskResult.Type = ChildTaskResult.self, returning returnType: GroupResult.Type = GroupResult.self, isolation: isolated (any Actor)? = #isolation, body: (inout ThrowingTaskGroup<ChildTaskResult, any Error>) async throws -> GroupResult) async rethrows -> GroupResult where ChildTaskResult : Sendable
```

## Discussion

A group _always_ waits for all of its child tasks to complete before it returns. Even canceled tasks must run until completion before this function returns. Canceled child tasks cooperatively react to cancellation and attempt to return as early as possible. After this function returns, the task group is always empty.

To collect the results of the group’s child tasks, you can use a `for`-`await`-`in` loop:

```swift
var sum = 0
for try await result in group {
    sum += result
}
```

If you need more control or only a few results, you can call `next()` directly:

```swift
guard let first = try await group.next() else {
    group.cancelAll()
    return 0
}
let second = await group.next() ?? 0
group.cancelAll()
return first + second
```

## Error Handling

Throwing an error in one of the child tasks of a task group doesn’t immediately cancel the other tasks in that group. However, throwing out of the `body` of the `withThrowingTaskGroup` method does cancel the group, and all of its child tasks. For example, if you call `next()` in the task group and propagate its error, all other tasks are canceled. For example, in the code below, nothing is canceled and the group doesn’t throw an error:

```swift
try await withThrowingTaskGroup(of: Void.self) { group in
    group.addTask { throw SomeError() }
}
```

In contrast, this example throws `SomeError` and cancels all of the tasks in the group:

```swift
try await withThrowingTaskGroup(of: Void.self) { group in
    group.addTask { throw SomeError() }
    try await group.next()
}
```

An individual task throws its error in the corresponding call to `Group.next()`, which gives you a chance to handle the individual error or to let the group rethrow the error.

Refer to [TaskGroup](taskgroup.md) documentation for detailed discussion of semantics shared between all task groups.

> [!info] See Also
> [TaskGroup](taskgroup.md)

> [!info] See Also
> [ThrowingTaskGroup](throwingtaskgroup.md)

> [!info] See Also
> [ThrowingDiscardingTaskGroup](throwingdiscardingtaskgroup.md)

## See Also

### Tasks

- [Task](task.md) — A unit of asynchronous work.
- [TaskGroup](taskgroup.md) — A group that contains dynamically created child tasks.
- [withTaskGroup(of:returning:isolation:body:)](<withtaskgroup(of_returning_isolation_body_).md>) — Starts a new scope that can contain a dynamic number of child tasks.
- [ThrowingTaskGroup](throwingtaskgroup.md) — A group that contains throwing, dynamically created child tasks.
- [TaskPriority](taskpriority.md) — The priority of a task.
- [DiscardingTaskGroup](discardingtaskgroup.md) — A discarding group that contains dynamically created child tasks.
- [withDiscardingTaskGroup(returning:isolation:body:)](<withdiscardingtaskgroup(returning_isolation_body_).md>) — Starts a new scope that can contain a dynamic number of child tasks.
- [ThrowingDiscardingTaskGroup](throwingdiscardingtaskgroup.md) — A throwing discarding group that contains dynamically created child tasks.
- [withThrowingDiscardingTaskGroup(returning:isolation:body:)](<withthrowingdiscardingtaskgroup(returning_isolation_body_).md>) — Starts a new scope that can contain a dynamic number of child tasks.
- [UnsafeCurrentTask](unsafecurrenttask.md) — An unsafe reference to the current task.

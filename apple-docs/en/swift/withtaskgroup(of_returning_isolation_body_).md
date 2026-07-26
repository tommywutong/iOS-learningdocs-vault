---
title: 'withTaskGroup(of:returning:isolation:body:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/withtaskgroup(of:returning:isolation:body:)'
source_url: 'https://developer.apple.com/documentation/swift/withtaskgroup(of:returning:isolation:body:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/withtaskgroup%28of%3Areturning%3Aisolation%3Abody%3A%29.json'
content_hash: 'sha256:67005b8e76b4becf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# withTaskGroup(of:returning:isolation:body:)

<sub>Function</sub>

Starts a new scope that can contain a dynamic number of child tasks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: macOS 15.0, iOS 18.0, watchOS 11.0, tvOS 18.0, visionOS 2.0)
func withTaskGroup<ChildTaskResult, GroupResult>(of childTaskResultType: ChildTaskResult.Type = ChildTaskResult.self, returning returnType: GroupResult.Type = GroupResult.self, isolation: isolated (any Actor)? = #isolation, body: (inout TaskGroup<ChildTaskResult>) async -> GroupResult) async -> GroupResult where ChildTaskResult : Sendable
```

## Discussion

A group _always_ waits for all of its child tasks to complete before it returns. Even canceled tasks must run until completion before this function returns. Canceled child tasks cooperatively react to cancellation and attempt to return as early as possible. After this function returns, the task group is always empty.

To collect the results of the group’s child tasks, you can use a `for`-`await`-`in` loop:

```swift
var sum = 0
for await result in group {
    sum += result
}
```

If you need more control or only a few results, you can call `next()` directly:

```swift
guard let first = await group.next() else {
    group.cancelAll()
    return 0
}
let second = await group.next() ?? 0
group.cancelAll()
return first + second
```

Refer to [TaskGroup](taskgroup.md) documentation for detailed discussion of semantics shared between all task groups.

> [!info] See Also
> [TaskGroup](taskgroup.md)

## See Also

### Tasks

- [Task](task.md) — A unit of asynchronous work.
- [TaskGroup](taskgroup.md) — A group that contains dynamically created child tasks.
- [ThrowingTaskGroup](throwingtaskgroup.md) — A group that contains throwing, dynamically created child tasks.
- [withThrowingTaskGroup(of:returning:isolation:body:)](<withthrowingtaskgroup(of_returning_isolation_body_).md>) — Starts a new scope that can contain a dynamic number of throwing child tasks.
- [TaskPriority](taskpriority.md) — The priority of a task.
- [DiscardingTaskGroup](discardingtaskgroup.md) — A discarding group that contains dynamically created child tasks.
- [withDiscardingTaskGroup(returning:isolation:body:)](<withdiscardingtaskgroup(returning_isolation_body_).md>) — Starts a new scope that can contain a dynamic number of child tasks.
- [ThrowingDiscardingTaskGroup](throwingdiscardingtaskgroup.md) — A throwing discarding group that contains dynamically created child tasks.
- [withThrowingDiscardingTaskGroup(returning:isolation:body:)](<withthrowingdiscardingtaskgroup(returning_isolation_body_).md>) — Starts a new scope that can contain a dynamic number of child tasks.
- [UnsafeCurrentTask](unsafecurrenttask.md) — An unsafe reference to the current task.

---
title: 'next(isolation:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/taskgroup/next(isolation:)'
source_url: 'https://developer.apple.com/documentation/swift/taskgroup/next(isolation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/taskgroup/next%28isolation%3A%29.json'
content_hash: 'sha256:ebceaebf63467a6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [TaskGroup](../taskgroup.md)

# next(isolation:)

<sub>Instance Method</sub>

Waits for the next child task to complete, and returns the value it returned.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: macOS 15.0, iOS 18.0, watchOS 11.0, tvOS 18.0, visionOS 2.0)
mutating func next(isolation: isolated (any Actor)? = #isolation) async -> ChildTaskResult?
```

## Return Value

The value returned by the next child task that completes.

## Discussion

The values returned by successive calls to this method appear in the order that the tasks _completed_, not in the order that those tasks were added to the task group. For example:

```swift
group.addTask { 1 }
group.addTask { 2 }

print(await group.next())
// Prints either "2" or "1".
```

If there aren’t any pending tasks in the task group, this method returns `nil`, which lets you write the following to wait for a single task to complete:

```swift
if let first = try await group.next() {
   return first
}
```

It also lets you write code like the following to wait for all the child tasks to complete, collecting the values they returned:

```swift
while let value = try await group.next() {
   collected += value
}
return collected
```

Awaiting on an empty group immediately returns `nil` without suspending.

You can also use a `for`-`await`-`in` loop to collect results of a task group:

```swift
for await try value in group {
    collected += value
}
```

Don’t call this method from outside the task where you created this task group. In most cases, the Swift type system prevents this mistake. For example, because the `add(priority:operation:)` method is mutating, that method can’t be called from a concurrent execution context like a child task.

## See Also

### Accessing Individual Results

- [next()](<next().md>)
- [isEmpty](isempty.md) — A Boolean value that indicates whether the group has any remaining tasks.
- [waitForAll()](<waitforall().md>) — Wait for all of the group’s remaining tasks to complete.

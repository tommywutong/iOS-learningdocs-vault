---
title: nextResult()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/throwingtaskgroup/nextresult()
source_url: 'https://developer.apple.com/documentation/swift/throwingtaskgroup/nextresult()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/throwingtaskgroup/nextresult%28%29.json'
content_hash: 'sha256:69dcb4b474c4e670'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ThrowingTaskGroup](../throwingtaskgroup.md)

# nextResult()

<sub>Instance Method</sub>

Wait for the next child task to complete, and return a result containing either the value that the child task returned or the error that it threw.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated(nonsending) mutating func nextResult() async -> Result<ChildTaskResult, Failure>?
```

## Return Value

A `Result.success` value containing the value that the child task returned, or a `Result.failure` value containing the error that the child task threw.

## Discussion

The values returned by successive calls to this method appear in the order that the tasks _completed_, not in the order that those tasks were added to the task group. For example:

```swift
group.addTask { 1 }
group.addTask { 2 }

guard let result = await group.nextResult() else {
    return  // No task to wait on, which won't happen in this example.
}

switch result {
case .success(let value): print(value)
case .failure(let error): print("Failure: \(error)")
}
// Prints either "2" or "1".
```

If the next child task throws an error and you propagate that error from this method out of the body of a call to the `ThrowingTaskGroup.withThrowingTaskGroup(of:returning:body:)` method, then all remaining child tasks in that group are implicitly canceled.

> [!info] See Also
> `next()`

## See Also

### Accessing Individual Results

- [next()](<next().md>)
- [next(isolation:)](<next(isolation_).md>) — Wait for the next child task to complete, and return the value it returned or rethrow the error it threw.
- [isEmpty](isempty.md) — A Boolean value that indicates whether the group has any remaining tasks.
- [waitForAll()](<waitforall().md>) — Wait for all of the group’s remaining tasks to complete.

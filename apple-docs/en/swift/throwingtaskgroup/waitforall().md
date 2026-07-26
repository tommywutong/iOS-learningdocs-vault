---
title: waitForAll()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/throwingtaskgroup/waitforall()
source_url: 'https://developer.apple.com/documentation/swift/throwingtaskgroup/waitforall()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/throwingtaskgroup/waitforall%28%29.json'
content_hash: 'sha256:78b9e3f96bd01621'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ThrowingTaskGroup](../throwingtaskgroup.md)

# waitForAll()

<sub>Instance Method</sub>

Wait for all of the group’s remaining tasks to complete.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated(nonsending) mutating func waitForAll() async throws
```

## Discussion

If any of the tasks throw, the _first_ error thrown is captured and re-thrown by this method although the task group is _not_ canceled when this happens.

### Cancelling the task group on first error

If you want to cancel the task group, and all “sibling” tasks, whenever any of child tasks throws an error, use the following pattern instead:

```swift
while !group.isEmpty {
    do {
        try await group.next()
    } catch is CancellationError {
        // we decide that cancellation errors thrown by children,
        // should not cause cancellation of the entire group.
        continue;
    } catch {
        // other errors though we print and cancel the group,
        // and all of the remaining child tasks within it.
        print("Error: \(error)")
        group.cancelAll()
    }
}
assert(group.isEmpty())
```

> [!danger] Throws
> The _first_ error that was thrown by a child task during draining all the tasks. This first error is stored until all other tasks have completed, and is re-thrown afterwards.

## See Also

### Accessing Individual Results

- [next()](<next().md>)
- [nextResult()](<nextresult().md>) — Wait for the next child task to complete, and return a result containing either the value that the child task returned or the error that it threw.
- [next(isolation:)](<next(isolation_).md>) — Wait for the next child task to complete, and return the value it returned or rethrow the error it threw.
- [isEmpty](isempty.md) — A Boolean value that indicates whether the group has any remaining tasks.

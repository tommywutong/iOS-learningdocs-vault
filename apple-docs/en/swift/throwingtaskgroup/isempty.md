---
title: isEmpty
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/throwingtaskgroup/isempty
source_url: 'https://developer.apple.com/documentation/swift/throwingtaskgroup/isempty'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/throwingtaskgroup/isempty.json'
content_hash: 'sha256:9dcbf008cbb111de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ThrowingTaskGroup](../throwingtaskgroup.md)

# isEmpty

<sub>Instance Property</sub>

A Boolean value that indicates whether the group has any remaining tasks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isEmpty: Bool { get }
```

## Return Value

`true` if the group has no pending tasks; otherwise `false`.

## Discussion

At the start of the body of a `withThrowingTaskGroup(of:returning:body:)` call, the task group is always empty.

It’s guaranteed to be empty when returning from that body because a task group waits for all child tasks to complete before returning.

## See Also

### Accessing Individual Results

- [next()](<next().md>)
- [nextResult()](<nextresult().md>) — Wait for the next child task to complete, and return a result containing either the value that the child task returned or the error that it threw.
- [next(isolation:)](<next(isolation_).md>) — Wait for the next child task to complete, and return the value it returned or rethrow the error it threw.
- [waitForAll()](<waitforall().md>) — Wait for all of the group’s remaining tasks to complete.

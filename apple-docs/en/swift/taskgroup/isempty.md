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
doc_path: /documentation/swift/taskgroup/isempty
source_url: 'https://developer.apple.com/documentation/swift/taskgroup/isempty'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/taskgroup/isempty.json'
content_hash: 'sha256:6ff611a78f495f38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [TaskGroup](../taskgroup.md)

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

At the start of the body of a `withTaskGroup(of:returning:body:)` call, the task group is always empty. It’s guaranteed to be empty when returning from that body because a task group waits for all child tasks to complete before returning.

## See Also

### Accessing Individual Results

- [next()](<next().md>)
- [next(isolation:)](<next(isolation_).md>) — Waits for the next child task to complete, and returns the value it returned.
- [waitForAll()](<waitforall().md>) — Wait for all of the group’s remaining tasks to complete.

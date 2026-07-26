---
title: next()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/taskgroup/iterator/next()
source_url: 'https://developer.apple.com/documentation/swift/taskgroup/iterator/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/taskgroup/iterator/next%28%29.json'
content_hash: 'sha256:7eb31cb5ac0c39c5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [TaskGroup](../../taskgroup.md) · [Iterator](../iterator.md)

# next()

<sub>Instance Method</sub>

Advances to and returns the result of the next child task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next() async -> TaskGroup<ChildTaskResult>.Iterator.Element?
```

## Return Value

The value returned by the next child task that completes, or `nil` if there are no remaining child tasks,

## Discussion

The elements returned from this method appear in the order that the tasks _completed_, not in the order that those tasks were added to the task group. After this method returns `nil`, this iterator is guaranteed to never produce more values.

For more information about the iteration order and semantics, see `TaskGroup.next()`.

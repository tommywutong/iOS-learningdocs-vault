---
title: 'next(isolation:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/throwingtaskgroup/iterator/next(isolation:)'
source_url: 'https://developer.apple.com/documentation/swift/throwingtaskgroup/iterator/next(isolation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/throwingtaskgroup/iterator/next%28isolation%3A%29.json'
content_hash: 'sha256:2d8a7d0a2988bac0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [ThrowingTaskGroup](../../throwingtaskgroup.md) · [Iterator](../iterator.md)

# next(isolation:)

<sub>Instance Method</sub>

Advances to and returns the result of the next child task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next(isolation actor: isolated (any Actor)?) async throws(Failure) -> ThrowingTaskGroup<ChildTaskResult, Failure>.Iterator.Element?
```

## Return Value

The value returned by the next child task that completes, or `nil` if there are no remaining child tasks,

## Discussion

The elements returned from this method appear in the order that the tasks _completed_, not in the order that those tasks were added to the task group. After this method returns `nil`, this iterator is guaranteed to never produce more values.

For more information about the iteration order and semantics, see `ThrowingTaskGroup.next()`

> [!danger] Throws
> The error thrown by the next child task that completes.

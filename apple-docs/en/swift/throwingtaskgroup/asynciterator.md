---
title: ThrowingTaskGroup.AsyncIterator
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/throwingtaskgroup/asynciterator
source_url: 'https://developer.apple.com/documentation/swift/throwingtaskgroup/asynciterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/throwingtaskgroup/asynciterator.json'
content_hash: 'sha256:3d4a231edf760516'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ThrowingTaskGroup](../throwingtaskgroup.md)

# ThrowingTaskGroup.AsyncIterator

<sub>Type Alias</sub>

The type of asynchronous iterator that produces elements of this asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias AsyncIterator = ThrowingTaskGroup<ChildTaskResult, Failure>.Iterator
```

## See Also

### Supporting Types

- [Element](element.md) — The type of element produced by this asynchronous sequence.
- [Iterator](iterator.md) — A type that provides an iteration interface over the results of tasks added to the group.

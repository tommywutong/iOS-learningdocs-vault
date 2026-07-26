---
title: TaskGroup.Iterator
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/taskgroup/iterator
source_url: 'https://developer.apple.com/documentation/swift/taskgroup/iterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/taskgroup/iterator.json'
content_hash: 'sha256:20fc44d713d1bfd1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [TaskGroup](../taskgroup.md)

# TaskGroup.Iterator

<sub>Structure</sub>

A type that provides an iteration interface over the results of tasks added to the group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Iterator
```

## Overview

The elements returned by this iterator appear in the order that the tasks _completed_, not in the order that those tasks were added to the task group.

This iterator terminates after all tasks have completed. After iterating over the results of each task, it’s valid to make a new iterator for the task group, which you can use to iterate over the results of new tasks you add to the group. For example:

```swift
group.addTask { 1 }
for await r in group { print(r) }

// Add a new child task and iterate again.
group.addTask { 2 }
for await r in group { print(r) }
```

> [!info] See Also
> `TaskGroup.next()`

## Relationships

- **Conforms To**: [AsyncIteratorProtocol](../asynciteratorprotocol.md)

## Topics

### Instance Methods

- [cancel()](<iterator/cancel().md>)
- [next()](<iterator/next().md>) — Advances to and returns the result of the next child task.
- [next(isolation:)](<iterator/next(isolation_).md>) — Advances to and returns the result of the next child task.

### Type Aliases

- [Element](iterator/element.md)

### Default Implementations

- [AsyncIteratorProtocol Implementations](iterator/asynciteratorprotocol-implementations.md)

## See Also

### Supporting Types

- [Element](element.md) — The type of element produced by this asynchronous sequence.
- [AsyncIterator](asynciterator.md) — The type of asynchronous iterator that produces elements of this asynchronous sequence.

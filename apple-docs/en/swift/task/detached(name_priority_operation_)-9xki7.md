---
title: 'detached(name:priority:operation:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/task/detached(name:priority:operation:)-9xki7'
source_url: 'https://developer.apple.com/documentation/swift/task/detached(name:priority:operation:)-9xki7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/task/detached%28name%3Apriority%3Aoperation%3A%29-9xki7.json'
content_hash: 'sha256:1afda364513967f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Task](../task.md)

# detached(name:priority:operation:)

<sub>Type Method</sub>

Runs the given nonthrowing operation asynchronously as part of a new _unstructured_ _detached_ top-level task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult static func detached(name: String? = nil, priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async -> Success) -> Task<Success, Never>
```

## Parameters

- `name` — Human readable name of the task.

- `priority` — The priority of the operation task. Omit this parameter or pass `nil` to inherit the enclosing context’s base priority.

- `operation` — The operation to perform.

## Return Value

A reference to the task.

## Discussion

Don’t use a detached unstructured task if it’s possible to model the operation using structured concurrency features like child tasks. Child tasks inherit the parent task’s priority and task-local storage, and canceling a parent task automatically cancels all of its child tasks. You need to handle these considerations manually with a detached task.

You need to keep a reference to the task if you want to cancel it by calling the `Task.cancel()` method. Discarding your reference to a task doesn’t implicitly cancel that task, it only makes it impossible for you to explicitly cancel the task.

## See Also

### Creating a Detached Task

- [detached(name:priority:operation:)](<detached(name_priority_operation_)-795w1.md>) — Runs the given throwing operation asynchronously as part of a new _unstructured_ _detached_ top-level task.
- [detached(name:executorPreference:priority:operation:)](<detached(name_executorpreference_priority_operation_)-6r16s.md>) — Runs the given throwing operation asynchronously as part of a new _unstructured_ _detached_ top-level task.
- [detached(name:executorPreference:priority:operation:)](<detached(name_executorpreference_priority_operation_)-75ffe.md>) — Runs the given nonthrowing operation asynchronously as part of a new _unstructured_ _detached_ top-level task.

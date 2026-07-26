---
title: 'init(name:priority:operation:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/task/init(name:priority:operation:)-2dll5'
source_url: 'https://developer.apple.com/documentation/swift/task/init(name:priority:operation:)-2dll5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/task/init%28name%3Apriority%3Aoperation%3A%29-2dll5.json'
content_hash: 'sha256:736fb2ad924369b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Task](../task.md)

# init(name:priority:operation:)

<sub>Initializer</sub>

Runs the given nonthrowing operation asynchronously as part of a new _unstructured_ top-level task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult init(name: String? = nil, priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async -> Success)
```

## Parameters

- `name` — Human readable name of the task.

- `priority` — The priority of the operation task.

- `operation` — The operation to perform.

## Return Value

A reference to the task.

## Discussion

You need to keep a reference to the task if you want to cancel it by calling the `Task.cancel()` method. Discarding your reference to a task doesn’t implicitly cancel that task, it only makes it impossible for you to explicitly cancel the task.

## See Also

### Creating a Task

- [init(name:priority:operation:)](<init(name_priority_operation_)-43wmk.md>) — Runs the given throwing operation asynchronously as part of a new _unstructured_ top-level task.
- [init(name:executorPreference:priority:operation:)](<init(name_executorpreference_priority_operation_)-59bfi.md>) — Runs the given throwing operation asynchronously as part of a new _unstructured_ top-level task.
- [init(name:executorPreference:priority:operation:)](<init(name_executorpreference_priority_operation_)-81pay.md>) — Runs the given nonthrowing operation asynchronously as part of a new _unstructured_ top-level task.
- [currentPriority](currentpriority.md) — The current task’s priority.
- [basePriority](basepriority.md) — The current task’s base priority.
- [withTaskPriorityEscalationHandler(operation:onPriorityEscalated:)](<../withtaskpriorityescalationhandler(operation_onpriorityescalated_).md>) — Runs the passed `operation` while registering a task priority escalation handler. The handler will be triggered concurrently to the current task if the current is subject to priority escalation.

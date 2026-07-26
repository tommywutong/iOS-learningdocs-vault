---
title: basePriority
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/task/basepriority
source_url: 'https://developer.apple.com/documentation/swift/task/basepriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/task/basepriority.json'
content_hash: 'sha256:da76de3439e435d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Task](../task.md)

# basePriority

<sub>Type Property</sub>

The current task’s base priority.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var basePriority: TaskPriority? { get }
```

## Discussion

If you access this property outside of any task, this returns nil

## See Also

### Creating a Task

- [init(name:priority:operation:)](<init(name_priority_operation_)-2dll5.md>) — Runs the given nonthrowing operation asynchronously as part of a new _unstructured_ top-level task.
- [init(name:priority:operation:)](<init(name_priority_operation_)-43wmk.md>) — Runs the given throwing operation asynchronously as part of a new _unstructured_ top-level task.
- [init(name:executorPreference:priority:operation:)](<init(name_executorpreference_priority_operation_)-59bfi.md>) — Runs the given throwing operation asynchronously as part of a new _unstructured_ top-level task.
- [init(name:executorPreference:priority:operation:)](<init(name_executorpreference_priority_operation_)-81pay.md>) — Runs the given nonthrowing operation asynchronously as part of a new _unstructured_ top-level task.
- [currentPriority](currentpriority.md) — The current task’s priority.
- [withTaskPriorityEscalationHandler(operation:onPriorityEscalated:)](<../withtaskpriorityescalationhandler(operation_onpriorityescalated_).md>) — Runs the passed `operation` while registering a task priority escalation handler. The handler will be triggered concurrently to the current task if the current is subject to priority escalation.

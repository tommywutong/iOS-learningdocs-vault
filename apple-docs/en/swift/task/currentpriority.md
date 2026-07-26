---
title: currentPriority
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/task/currentpriority
source_url: 'https://developer.apple.com/documentation/swift/task/currentpriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/task/currentpriority.json'
content_hash: 'sha256:d64dff1e2f000385'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Task](../task.md)

# currentPriority

<sub>Type Property</sub>

The current task’s priority.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var currentPriority: TaskPriority { get }
```

## Discussion

If you access this property outside of any task, this queries the system to determine the priority at which the current function is running. If the system can’t provide a priority, this property’s value is `Priority.default`.

## See Also

### Creating a Task

- [init(name:priority:operation:)](<init(name_priority_operation_)-2dll5.md>) — Runs the given nonthrowing operation asynchronously as part of a new _unstructured_ top-level task.
- [init(name:priority:operation:)](<init(name_priority_operation_)-43wmk.md>) — Runs the given throwing operation asynchronously as part of a new _unstructured_ top-level task.
- [init(name:executorPreference:priority:operation:)](<init(name_executorpreference_priority_operation_)-59bfi.md>) — Runs the given throwing operation asynchronously as part of a new _unstructured_ top-level task.
- [init(name:executorPreference:priority:operation:)](<init(name_executorpreference_priority_operation_)-81pay.md>) — Runs the given nonthrowing operation asynchronously as part of a new _unstructured_ top-level task.
- [basePriority](basepriority.md) — The current task’s base priority.
- [withTaskPriorityEscalationHandler(operation:onPriorityEscalated:)](<../withtaskpriorityescalationhandler(operation_onpriorityescalated_).md>) — Runs the passed `operation` while registering a task priority escalation handler. The handler will be triggered concurrently to the current task if the current is subject to priority escalation.

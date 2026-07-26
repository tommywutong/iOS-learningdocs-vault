---
title: 'withTaskPriorityEscalationHandler(operation:onPriorityEscalated:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/withtaskpriorityescalationhandler(operation:onpriorityescalated:)'
source_url: 'https://developer.apple.com/documentation/swift/withtaskpriorityescalationhandler(operation:onpriorityescalated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/withtaskpriorityescalationhandler%28operation%3Aonpriorityescalated%3A%29.json'
content_hash: 'sha256:c9046b55b67024ce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# withTaskPriorityEscalationHandler(operation:onPriorityEscalated:)

<sub>Function</sub>

Runs the passed `operation` while registering a task priority escalation handler. The handler will be triggered concurrently to the current task if the current is subject to priority escalation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated(nonsending) func withTaskPriorityEscalationHandler<T, E>(operation: nonisolated(nonsending) () async throws(E) -> T, onPriorityEscalated handler: @Sendable (TaskPriority, TaskPriority) -> Void) async throws(E) -> T where E : Error
```

## Parameters

- `operation` — The operation during which to listen for priority escalation

- `handler` — Handler to invoke, concurrently to `operation`, when priority escalation happens. The first argument is the old priority (before escalation), and the second argument is the new escalated priority.

## Return Value

The value returned by `operation`

## Discussion

The handler may perform additional actions upon priority escalation, but cannot influence how the escalation influences the task, i.e. the task’s priority will be escalated regardless of actions performed in the handler.

The handler will only trigger if a priority escalation occurs while the operation is in progress.

If multiple task escalation handlers are nested they will all be triggered.

Task escalation propagates through structured concurrency child-tasks.

> [!danger] Throws
> When the `operation` throws an error

## See Also

### Creating a Task

- [init(name:priority:operation:)](<task/init(name_priority_operation_)-2dll5.md>) — Runs the given nonthrowing operation asynchronously as part of a new _unstructured_ top-level task.
- [init(name:priority:operation:)](<task/init(name_priority_operation_)-43wmk.md>) — Runs the given throwing operation asynchronously as part of a new _unstructured_ top-level task.
- [init(name:executorPreference:priority:operation:)](<task/init(name_executorpreference_priority_operation_)-59bfi.md>) — Runs the given throwing operation asynchronously as part of a new _unstructured_ top-level task.
- [init(name:executorPreference:priority:operation:)](<task/init(name_executorpreference_priority_operation_)-81pay.md>) — Runs the given nonthrowing operation asynchronously as part of a new _unstructured_ top-level task.
- [currentPriority](task/currentpriority.md) — The current task’s priority.
- [basePriority](task/basepriority.md) — The current task’s base priority.

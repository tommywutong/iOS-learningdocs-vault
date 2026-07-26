---
title: 'addTask(priority:operation:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/throwingtaskgroup/addtask(priority:operation:)'
source_url: 'https://developer.apple.com/documentation/swift/throwingtaskgroup/addtask(priority:operation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/throwingtaskgroup/addtask%28priority%3Aoperation%3A%29.json'
content_hash: 'sha256:dda86b7e82f02eef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ThrowingTaskGroup](../throwingtaskgroup.md)

# addTask(priority:operation:)

<sub>Instance Method</sub>

Adds a child task to the group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func addTask(priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async throws -> ChildTaskResult)
```

## Parameters

- `priority` — The priority of the operation task. Omit this parameter or pass `nil` to inherit the task group’s base priority.

- `operation` — The operation to execute as part of the task group.

## Discussion

This method doesn’t throw an error, even if the child task does. Instead, the corresponding call to `ThrowingTaskGroup.next()` rethrows that error.

## See Also

### Adding Tasks to a Throwing Task Group

- [addTask(executorPreference:priority:operation:)](<addtask(executorpreference_priority_operation_).md>) — Adds a child task to the group.
- [addTask(name:priority:operation:)](<addtask(name_priority_operation_).md>) — Adds a child task to the group.
- [addTask(name:executorPreference:priority:operation:)](<addtask(name_executorpreference_priority_operation_).md>) — Adds a child task to the group.
- [addTaskUnlessCancelled(priority:operation:)](<addtaskunlesscancelled(priority_operation_).md>) — Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [addTaskUnlessCancelled(name:executorPreference:priority:operation:)](<addtaskunlesscancelled(name_executorpreference_priority_operation_).md>) — Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [addTaskUnlessCancelled(executorPreference:priority:operation:)](<addtaskunlesscancelled(executorpreference_priority_operation_).md>) — Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [addTaskUnlessCancelled(name:priority:operation:)](<addtaskunlesscancelled(name_priority_operation_).md>) — Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [addImmediateTask(name:priority:executorPreference:operation:)](<addimmediatetask(name_priority_executorpreference_operation_).md>) — Add a child task to the group and immediately start running it in the context of the calling thread/task.
- [addImmediateTaskUnlessCancelled(name:priority:executorPreference:operation:)](<addimmediatetaskunlesscancelled(name_priority_executorpreference_operation_).md>) — Add a child task to the group and immediately start running it in the context of the calling thread/task.

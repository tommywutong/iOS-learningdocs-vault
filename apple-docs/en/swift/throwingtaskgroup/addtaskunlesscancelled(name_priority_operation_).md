---
title: 'addTaskUnlessCancelled(name:priority:operation:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/throwingtaskgroup/addtaskunlesscancelled(name:priority:operation:)'
source_url: 'https://developer.apple.com/documentation/swift/throwingtaskgroup/addtaskunlesscancelled(name:priority:operation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/throwingtaskgroup/addtaskunlesscancelled%28name%3Apriority%3Aoperation%3A%29.json'
content_hash: 'sha256:fa6af491e63e402a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ThrowingTaskGroup](../throwingtaskgroup.md)

# addTaskUnlessCancelled(name:priority:operation:)

<sub>Instance Method</sub>

Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func addTaskUnlessCancelled(name: String?, priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async throws -> ChildTaskResult) -> Bool
```

## Parameters

- `name` — Human readable name of this task.

- `priority` — The priority of the operation task. Omit this parameter or pass `nil` to inherit the task group’s base priority.

- `operation` — The operation to execute as part of the task group.

## Return Value

`true` if the child task was added to the group; otherwise `false`.

## Discussion

This method doesn’t throw an error, even if the child task does. Instead, the corresponding call to `ThrowingTaskGroup.next()` rethrows that error.

## See Also

### Adding Tasks to a Throwing Task Group

- [addTask(priority:operation:)](<addtask(priority_operation_).md>) — Adds a child task to the group.
- [addTask(executorPreference:priority:operation:)](<addtask(executorpreference_priority_operation_).md>) — Adds a child task to the group.
- [addTask(name:priority:operation:)](<addtask(name_priority_operation_).md>) — Adds a child task to the group.
- [addTask(name:executorPreference:priority:operation:)](<addtask(name_executorpreference_priority_operation_).md>) — Adds a child task to the group.
- [addTaskUnlessCancelled(priority:operation:)](<addtaskunlesscancelled(priority_operation_).md>) — Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [addTaskUnlessCancelled(name:executorPreference:priority:operation:)](<addtaskunlesscancelled(name_executorpreference_priority_operation_).md>) — Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [addTaskUnlessCancelled(executorPreference:priority:operation:)](<addtaskunlesscancelled(executorpreference_priority_operation_).md>) — Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [addImmediateTask(name:priority:executorPreference:operation:)](<addimmediatetask(name_priority_executorpreference_operation_).md>) — Add a child task to the group and immediately start running it in the context of the calling thread/task.
- [addImmediateTaskUnlessCancelled(name:priority:executorPreference:operation:)](<addimmediatetaskunlesscancelled(name_priority_executorpreference_operation_).md>) — Add a child task to the group and immediately start running it in the context of the calling thread/task.

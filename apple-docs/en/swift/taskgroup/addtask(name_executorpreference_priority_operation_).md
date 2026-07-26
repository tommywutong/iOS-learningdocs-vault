---
title: 'addTask(name:executorPreference:priority:operation:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/taskgroup/addtask(name:executorpreference:priority:operation:)'
source_url: 'https://developer.apple.com/documentation/swift/taskgroup/addtask(name:executorpreference:priority:operation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/taskgroup/addtask%28name%3Aexecutorpreference%3Apriority%3Aoperation%3A%29.json'
content_hash: 'sha256:0761b57d58a8ec13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [TaskGroup](../taskgroup.md)

# addTask(name:executorPreference:priority:operation:)

<sub>Instance Method</sub>

Adds a child task to the group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func addTask(name: String?, executorPreference taskExecutor: (any TaskExecutor)? = nil, priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async -> ChildTaskResult)
```

## Parameters

- `name` — Human readable name of this task.

- `taskExecutor` — The task executor that the child task should be started on and keep using. Explicitly passing `nil` as the executor preference is equivalent to calling the `addTask` method without a preference, and effectively means to inherit the outer context’s executor preference. You can also pass the [globalConcurrentExecutor](../globalconcurrentexecutor.md) global executor explicitly.

- `priority` — The priority of the operation task. Omit this parameter or pass `nil` to inherit the task group’s base priority.

- `operation` — The operation to execute as part of the task group.

## See Also

### Adding Tasks to a Task Group

- [addTask(priority:operation:)](<addtask(priority_operation_).md>) — Adds a child task to the group.
- [addTask(name:priority:operation:)](<addtask(name_priority_operation_).md>) — Adds a child task to the group.
- [addTask(executorPreference:priority:operation:)](<addtask(executorpreference_priority_operation_).md>) — Adds a child task to the group.
- [addTaskUnlessCancelled(name:executorPreference:priority:operation:)](<addtaskunlesscancelled(name_executorpreference_priority_operation_).md>) — Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [addTaskUnlessCancelled(executorPreference:priority:operation:)](<addtaskunlesscancelled(executorpreference_priority_operation_).md>) — Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [addTaskUnlessCancelled(name:priority:operation:)](<addtaskunlesscancelled(name_priority_operation_).md>) — Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [addTaskUnlessCancelled(priority:operation:)](<addtaskunlesscancelled(priority_operation_).md>) — Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [addImmediateTask(name:priority:executorPreference:operation:)](<addimmediatetask(name_priority_executorpreference_operation_).md>) — Add a child task to the group and immediately start running it in the context of the calling thread/task.
- [addImmediateTaskUnlessCancelled(name:priority:executorPreference:operation:)](<addimmediatetaskunlesscancelled(name_priority_executorpreference_operation_).md>) — Add a child task to the group and immediately start running it in the context of the calling thread/task.

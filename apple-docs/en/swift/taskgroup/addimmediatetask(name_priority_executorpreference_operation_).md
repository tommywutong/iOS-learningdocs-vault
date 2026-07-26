---
title: 'addImmediateTask(name:priority:executorPreference:operation:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/taskgroup/addimmediatetask(name:priority:executorpreference:operation:)'
source_url: 'https://developer.apple.com/documentation/swift/taskgroup/addimmediatetask(name:priority:executorpreference:operation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/taskgroup/addimmediatetask%28name%3Apriority%3Aexecutorpreference%3Aoperation%3A%29.json'
content_hash: 'sha256:4d2be814181beb07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [TaskGroup](../taskgroup.md)

# addImmediateTask(name:priority:executorPreference:operation:)

<sub>Instance Method</sub>

Add a child task to the group and immediately start running it in the context of the calling thread/task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func addImmediateTask(name: String? = nil, priority: TaskPriority? = nil, executorPreference taskExecutor: consuming (any TaskExecutor)? = nil, operation: sending @escaping @isolated(any) () async -> ChildTaskResult)
```

## Parameters

- `name` — Human readable name of this task.

- `priority` — The priority of the operation task. Omit this parameter or pass `nil` to inherit the task group’s base priority.

- `taskExecutor` — The task executor that the child task should be started on and keep using. Explicitly passing `nil` as the executor preference is equivalent to calling the `addImmediateTask` method without a preference, and effectively means to inherit the outer context’s executor preference. You can also pass the [globalConcurrentExecutor](../globalconcurrentexecutor.md) global executor explicitly.

- `operation` — The operation to execute as part of the task group.

## Discussion

This function _starts_ the created task on the calling context. The task will continue executing on the caller’s context until it suspends, and after suspension will resume on the adequate executor. For a nonisolated operation this means running on the global concurrent pool, and on an isolated operation it means the appropriate executor of that isolation context.

As indicated by the lack of `async` on this method, this method does _not_ suspend, and instead takes over the calling task’s (thread’s) execution in a synchronous manner.

Other than the execution semantics discussed above, the created task is semantically equivalent to its basic version which can be created using `TaskGroup/addTask`.

## See Also

### Adding Tasks to a Task Group

- [addTask(priority:operation:)](<addtask(priority_operation_).md>) — Adds a child task to the group.
- [addTask(name:priority:operation:)](<addtask(name_priority_operation_).md>) — Adds a child task to the group.
- [addTask(executorPreference:priority:operation:)](<addtask(executorpreference_priority_operation_).md>) — Adds a child task to the group.
- [addTask(name:executorPreference:priority:operation:)](<addtask(name_executorpreference_priority_operation_).md>) — Adds a child task to the group.
- [addTaskUnlessCancelled(name:executorPreference:priority:operation:)](<addtaskunlesscancelled(name_executorpreference_priority_operation_).md>) — Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [addTaskUnlessCancelled(executorPreference:priority:operation:)](<addtaskunlesscancelled(executorpreference_priority_operation_).md>) — Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [addTaskUnlessCancelled(name:priority:operation:)](<addtaskunlesscancelled(name_priority_operation_).md>) — Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [addTaskUnlessCancelled(priority:operation:)](<addtaskunlesscancelled(priority_operation_).md>) — Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [addImmediateTaskUnlessCancelled(name:priority:executorPreference:operation:)](<addimmediatetaskunlesscancelled(name_priority_executorpreference_operation_).md>) — Add a child task to the group and immediately start running it in the context of the calling thread/task.

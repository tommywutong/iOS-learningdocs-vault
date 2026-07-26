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
doc_path: '/documentation/swift/discardingtaskgroup/addtask(name:executorpreference:priority:operation:)'
source_url: 'https://developer.apple.com/documentation/swift/discardingtaskgroup/addtask(name:executorpreference:priority:operation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/discardingtaskgroup/addtask%28name%3Aexecutorpreference%3Apriority%3Aoperation%3A%29.json'
content_hash: 'sha256:513f8bbe8f8c73a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DiscardingTaskGroup](../discardingtaskgroup.md)

# addTask(name:executorPreference:priority:operation:)

<sub>Instance Method</sub>

Adds a child task to the group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func addTask(name: String?, executorPreference taskExecutor: (any TaskExecutor)? = nil, priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async -> Void)
```

## Parameters

- `name` — Human readable name of this task.

- `taskExecutor` — The task executor that the child task should be started on and keep using. Explicitly passing `nil` as the executor preference is equivalent to calling the `addTask` method without a preference, and effectively means to inherit the outer context’s executor preference. You can also pass the [globalConcurrentExecutor](../globalconcurrentexecutor.md) global executor explicitly.

- `priority` — The priority of the operation task. Omit this parameter or pass `nil` to inherit the task group’s base priority.

- `operation` — The operation to execute as part of the task group.

---
title: 'addTaskUnlessCancelled(executorPreference:priority:operation:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/discardingtaskgroup/addtaskunlesscancelled(executorpreference:priority:operation:)'
source_url: 'https://developer.apple.com/documentation/swift/discardingtaskgroup/addtaskunlesscancelled(executorpreference:priority:operation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/discardingtaskgroup/addtaskunlesscancelled%28executorpreference%3Apriority%3Aoperation%3A%29.json'
content_hash: 'sha256:c7eaafb552a91eac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DiscardingTaskGroup](../discardingtaskgroup.md)

# addTaskUnlessCancelled(executorPreference:priority:operation:)

<sub>Instance Method</sub>

Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func addTaskUnlessCancelled(executorPreference taskExecutor: (any TaskExecutor)? = nil, priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async -> Void) -> Bool
```

## Parameters

- `taskExecutor` — The task executor that the child task should be started on and keep using. Explicitly passing `nil` as the executor preference is equivalent to calling the `addTaskUnlessCancelled` method without a preference, and effectively means to inherit the outer context’s executor preference. You can also pass the [globalConcurrentExecutor](../globalconcurrentexecutor.md) global executor explicitly.

- `priority` — The priority of the operation task. Omit this parameter or pass `nil` to inherit the task group’s base priority.

- `operation` — The operation to execute as part of the task group.

## Return Value

`true` if the child task was added to the group; otherwise `false`.

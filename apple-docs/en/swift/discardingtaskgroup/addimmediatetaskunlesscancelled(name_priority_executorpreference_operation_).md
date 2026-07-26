---
title: 'addImmediateTaskUnlessCancelled(name:priority:executorPreference:operation:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/discardingtaskgroup/addimmediatetaskunlesscancelled(name:priority:executorpreference:operation:)'
source_url: 'https://developer.apple.com/documentation/swift/discardingtaskgroup/addimmediatetaskunlesscancelled(name:priority:executorpreference:operation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/discardingtaskgroup/addimmediatetaskunlesscancelled%28name%3Apriority%3Aexecutorpreference%3Aoperation%3A%29.json'
content_hash: 'sha256:27a9ee27f612a261'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DiscardingTaskGroup](../discardingtaskgroup.md)

# addImmediateTaskUnlessCancelled(name:priority:executorPreference:operation:)

<sub>Instance Method</sub>

Add a child task to the group and immediately start running it in the context of the calling thread/task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func addImmediateTaskUnlessCancelled(name: String? = nil, priority: TaskPriority? = nil, executorPreference taskExecutor: consuming (any TaskExecutor)? = nil, operation: sending @escaping @isolated(any) () async -> Void) -> Bool
```

## Parameters

- `name` — Human readable name of this task.

- `priority` — The priority of the operation task. Omit this parameter or pass `nil` to inherit the task group’s base priority.

- `taskExecutor` — The task executor that the child task should be started on and keep using. Explicitly passing `nil` as the executor preference is equivalent to calling the `addImmediateTaskUnlessCancelled` method without a preference, and effectively means to inherit the outer context’s executor preference. You can also pass the [globalConcurrentExecutor](../globalconcurrentexecutor.md) global executor explicitly.

- `operation` — The operation to execute as part of the task group.

## Return Value

`true` if the child task was added to the group; otherwise `false`.

## Discussion

This function _starts_ the created task on the calling context. The task will continue executing on the caller’s context until it suspends, and after suspension will resume on the adequate executor. For a nonisolated operation this means running on the global concurrent pool, and on an isolated operation it means the appropriate executor of that isolation context.

As indicated by the lack of `async` on this method, this method does _not_ suspend, and instead takes over the calling task’s (thread’s) execution in a synchronous manner.

Other than the execution semantics discussed above, the created task is semantically equivalent to its basic version which can be created using `DiscardingTaskGroup/addTask`.

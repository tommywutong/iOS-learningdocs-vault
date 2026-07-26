---
title: 'immediateDetached(name:priority:executorPreference:operation:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/task/immediatedetached(name:priority:executorpreference:operation:)-7h41b'
source_url: 'https://developer.apple.com/documentation/swift/task/immediatedetached(name:priority:executorpreference:operation:)-7h41b'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/task/immediatedetached%28name%3Apriority%3Aexecutorpreference%3Aoperation%3A%29-7h41b.json'
content_hash: 'sha256:aad09f5387c0a236'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Task](../task.md)

# immediateDetached(name:priority:executorPreference:operation:)

<sub>Type Method</sub>

Create and immediately start running a new detached task in the context of the calling thread/task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult static func immediateDetached(name: String? = nil, priority: TaskPriority? = nil, executorPreference taskExecutor: consuming (any TaskExecutor)? = nil, operation: sending @escaping @isolated(any) () async -> Success) -> Task<Success, Never>
```

## Parameters

- `name` — The high-level human-readable name given for this task

- `priority` — The priority of the task. Pass `nil` to use the [basePriority](basepriority.md) of the current task (if there is one).

- `taskExecutor` — The task executor that the child task should be started on and keep using. Explicitly passing `nil` as the executor preference is equivalent to no preference, and effectively means to inherit the outer context’s executor preference. You can also pass the [globalConcurrentExecutor](../globalconcurrentexecutor.md) global executor explicitly.

- `operation` — The operation to be run immediately upon entering the task.

## Return Value

A reference to the unstructured task which may be awaited on.

## Discussion

This function _starts_ the created task on the calling context. The task will continue executing on the caller’s context until it suspends, and after suspension will resume on the adequate executor. For a nonisolated operation this means running on the global concurrent pool, and on an isolated operation it means the appropriate executor of that isolation context.

As indicated by the lack of `async` on this method, this method does _not_ suspend, and instead takes over the calling task’s (thread’s) execution in a synchronous manner.

Other than the execution semantics discussed above, the created task is semantically equivalent to a task created using the `Task/detached` function.

## See Also

### Creating a Task that Starts Immediately

- [immediate(name:priority:executorPreference:operation:)](<immediate(name_priority_executorpreference_operation_)-88o80.md>) — Create and immediately start running a new task in the context of the calling thread/task.
- [immediate(name:priority:executorPreference:operation:)](<immediate(name_priority_executorpreference_operation_)-9bghc.md>) — Create and immediately start running a new task in the context of the calling thread/task.
- [immediateDetached(name:priority:executorPreference:operation:)](<immediatedetached(name_priority_executorpreference_operation_)-52ipd.md>) — Create and immediately start running a new detached task in the context of the calling thread/task.

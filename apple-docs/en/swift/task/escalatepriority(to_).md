---
title: 'escalatePriority(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/task/escalatepriority(to:)'
source_url: 'https://developer.apple.com/documentation/swift/task/escalatepriority(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/task/escalatepriority%28to%3A%29.json'
content_hash: 'sha256:c19d37555b08dfcd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Task](../task.md)

# escalatePriority(to:)

<sub>Instance Method</sub>

Manually escalate the task `priority` of this task to the `newPriority`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func escalatePriority(to newPriority: TaskPriority)
```

## Parameters

- `newPriority` — The new priority the task should continue executing on

## Discussion

> [!warning] Warning
> This API should rarely be used, and instead you can rely on structured concurrency and implicit priority escalation which happens when a higher priority task awaits on a result of a lower priority task.
>
> I.e. using `await` on the target task usually is the correct way to escalate the target task to the current priority of the calling task, especially because in such setup if the waiting task gets escalated, the waited on task would be escalated automatically as well.

The concurrency runtime is free to interpret and handle escalation depending on platform characteristics.

Priority escalation is propagated to child tasks of the waited-on task, and will trigger any priority escalation handlers, if any were registered.

Escalation can only _increase_ the priority of a task, and de-escalating priority is not supported.

This method can be called from any task or thread.

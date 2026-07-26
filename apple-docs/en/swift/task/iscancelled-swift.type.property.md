---
title: isCancelled
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/task/iscancelled-swift.type.property
source_url: 'https://developer.apple.com/documentation/swift/task/iscancelled-swift.type.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/task/iscancelled-swift.type.property.json'
content_hash: 'sha256:24dd59f1d00e6298'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Task](../task.md)

# isCancelled

<sub>Type Property</sub>

A Boolean value that indicates whether the task should stop executing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var isCancelled: Bool { get }
```

## Discussion

After the value of this property becomes `true`, it remains `true` indefinitely. There is no way to uncancel a task.

### Interaction with Task Cancellation Shields

Cancellation may be suppressed by an active task cancellation shield (`withTaskCancellationShield(operation:)`), which may cause `isCancelled` to return `false` even though the task has been cancelled externally.

> [!info] See Also
> [checkCancellation()](<checkcancellation().md>)

> [!info] See Also
> `withTaskCancellationShield(operation:)`

## See Also

### Canceling Tasks

- [CancellationError](../cancellationerror.md) — An error that indicates a task was canceled.
- [cancel()](<cancel().md>) — Cancels this task.
- [isCancelled](iscancelled-swift.property.md) — A Boolean value that indicates whether the task should stop executing.
- [checkCancellation()](<checkcancellation().md>) — Throws an error if the task was canceled.
- [withTaskCancellationHandler(operation:onCancel:)](<../withtaskcancellationhandler(operation_oncancel_).md>) — Execute an operation with a cancellation handler that’s immediately invoked if the current task is canceled.
- [withTaskCancellationHandler(operation:onCancel:isolation:)](<../withtaskcancellationhandler(operation_oncancel_isolation_).md>) — Execute an operation with a cancellation handler that’s immediately invoked if the current task is canceled.

---
title: isCancelled
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/task/iscancelled-swift.property
source_url: 'https://developer.apple.com/documentation/swift/task/iscancelled-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/task/iscancelled-swift.property.json'
content_hash: 'sha256:99a1d2f83e332a5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Task](../task.md)

# isCancelled

<sub>Instance Property</sub>

A Boolean value that indicates whether the task should stop executing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isCancelled: Bool { get }
```

## Discussion

After the value of this property becomes `true`, it remains `true` indefinitely. There is no way to uncancel a task.

This property returns the actual cancellation state of the task, regardless of whether a cancellation shield is active. Use `Task/isCancelled` (the static property) if you need cancellation checking that respects active shields.

### Instance property isCancelled ignores Task Cancellation Shields

The instance property `task.isCancelled` is not contextual and therefore does not respect cancellation shields. If a task was cancelled and is executing with an active cancellation shield, these properties will return the _actual_ cancellation status of the specific task.

Prefer using `Task.isCancelled` (the static property) in most situations when checking the cancellation status from inside the task.

> [!info] See Also
> `Task/isCancelled`

> [!info] See Also
> [checkCancellation()](<checkcancellation().md>)

> [!info] See Also
> [hasActiveCancellationShield](hasactivecancellationshield.md)

> [!info] See Also
> `withTaskCancellationShield(operation:)`

## See Also

### Canceling Tasks

- [CancellationError](../cancellationerror.md) — An error that indicates a task was canceled.
- [cancel()](<cancel().md>) — Cancels this task.
- [isCancelled](iscancelled-swift.type.property.md) — A Boolean value that indicates whether the task should stop executing.
- [checkCancellation()](<checkcancellation().md>) — Throws an error if the task was canceled.
- [withTaskCancellationHandler(operation:onCancel:)](<../withtaskcancellationhandler(operation_oncancel_).md>) — Execute an operation with a cancellation handler that’s immediately invoked if the current task is canceled.
- [withTaskCancellationHandler(operation:onCancel:isolation:)](<../withtaskcancellationhandler(operation_oncancel_isolation_).md>) — Execute an operation with a cancellation handler that’s immediately invoked if the current task is canceled.

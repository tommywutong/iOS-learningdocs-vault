---
title: checkCancellation()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/task/checkcancellation()
source_url: 'https://developer.apple.com/documentation/swift/task/checkcancellation()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/task/checkcancellation%28%29.json'
content_hash: 'sha256:2f1d67a68734fa63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Task](../task.md)

# checkCancellation()

<sub>Type Method</sub>

Throws an error if the task was canceled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func checkCancellation() throws
```

## Discussion

The error is always an instance of `CancellationError`.

> [!info] See Also
> `isCancelled()`

## See Also

### Canceling Tasks

- [CancellationError](../cancellationerror.md) — An error that indicates a task was canceled.
- [cancel()](<cancel().md>) — Cancels this task.
- [isCancelled](iscancelled-swift.property.md) — A Boolean value that indicates whether the task should stop executing.
- [isCancelled](iscancelled-swift.type.property.md) — A Boolean value that indicates whether the task should stop executing.
- [withTaskCancellationHandler(operation:onCancel:)](<../withtaskcancellationhandler(operation_oncancel_).md>) — Execute an operation with a cancellation handler that’s immediately invoked if the current task is canceled.
- [withTaskCancellationHandler(operation:onCancel:isolation:)](<../withtaskcancellationhandler(operation_oncancel_isolation_).md>) — Execute an operation with a cancellation handler that’s immediately invoked if the current task is canceled.

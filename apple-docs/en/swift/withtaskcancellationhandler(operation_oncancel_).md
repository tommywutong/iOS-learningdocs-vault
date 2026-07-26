---
title: 'withTaskCancellationHandler(operation:onCancel:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/withtaskcancellationhandler(operation:oncancel:)'
source_url: 'https://developer.apple.com/documentation/swift/withtaskcancellationhandler(operation:oncancel:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/withtaskcancellationhandler%28operation%3Aoncancel%3A%29.json'
content_hash: 'sha256:8d5a44595a07d58b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# withTaskCancellationHandler(operation:onCancel:)

<sub>Function</sub>

Execute an operation with a cancellation handler that’s immediately invoked if the current task is canceled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated(nonsending) func withTaskCancellationHandler<Return, Failure>(operation: nonisolated(nonsending) () async throws(Failure) -> Return, onCancel handler: sending () -> Void) async throws(Failure) -> Return where Failure : Error
```

## Parameters

- `operation` — The operation to perform.

- `handler` — A closure to execute on cancellation. If the task is canceled, this closure is called at most once; otherwise, it isn’t called.

## Discussion

This differs from the operation cooperatively checking for cancellation and reacting to it in that the cancellation handler is _always_ and _immediately_ invoked when the task is canceled. For example, even if the operation is running code that never checks for cancellation, a cancellation handler still runs and provides a chance to run some cleanup code:

```swift
await withTaskCancellationHandler {
  var sum = 0
  while condition {
    sum += 1
  }
  return sum
} onCancel: {
  // This onCancel closure might execute concurrently with the operation.
  condition.cancel()
}
```

### Execution order and semantics

The `operation` closure is always invoked, even when the `withTaskCancellationHandler(operation:onCancel:)` method is called from a task that was already canceled.

When `withTaskCancellationHandler(operation:onCancel:)` is used in a task that has already been canceled, the cancellation handler will be executed immediately before the `operation` closure gets to execute.

This allows the cancellation handler to set some external “canceled” flag that the operation may be _atomically_ checking for in order to avoid performing any actual work once the operation gets to run.

The `operation` closure executes on the calling execution context, and doesn’t suspend or change execution context unless code contained within the closure does so. In other words, the potential suspension point of the `withTaskCancellationHandler(operation:onCancel:)` never suspends by itself before executing the operation.

If cancellation occurs while the operation is running, the cancellation handler executes _concurrently_ with the operation.

### Cancellation handlers and locks

Cancellation handlers which acquire locks must take care to avoid deadlock. The cancellation handler may be invoked while holding internal locks associated with the task or other tasks.  Other operations on the task, such as resuming a continuation, may acquire these same internal locks. Therefore, if a cancellation handler must acquire a lock, other code should not cancel tasks or resume continuations while holding that lock.

## See Also

### Canceling Tasks

- [CancellationError](cancellationerror.md) — An error that indicates a task was canceled.
- [cancel()](<task/cancel().md>) — Cancels this task.
- [isCancelled](task/iscancelled-swift.property.md) — A Boolean value that indicates whether the task should stop executing.
- [isCancelled](task/iscancelled-swift.type.property.md) — A Boolean value that indicates whether the task should stop executing.
- [checkCancellation()](<task/checkcancellation().md>) — Throws an error if the task was canceled.
- [withTaskCancellationHandler(operation:onCancel:isolation:)](<withtaskcancellationhandler(operation_oncancel_isolation_).md>) — Execute an operation with a cancellation handler that’s immediately invoked if the current task is canceled.

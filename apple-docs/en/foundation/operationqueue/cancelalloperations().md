---
title: cancelAllOperations()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/operationqueue/cancelalloperations()
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/cancelalloperations()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/cancelalloperations%28%29.json'
content_hash: 'sha256:d6d4f8beb7cda5db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OperationQueue](../operationqueue.md)

# cancelAllOperations()

<sub>Instance Method</sub>

Cancels all queued and executing operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancelAllOperations()
```

## Discussion

This method calls the [- cancel](<../operation/cancel().md>) method on all operations currently in the queue.

Canceling the operations does not automatically remove them from the queue or stop those that are currently executing. For operations that are queued and waiting execution, the queue must still attempt to execute the operation before recognizing that it is canceled and moving it to the finished state. For operations that are already executing, the operation object itself must check for cancellation and stop what it is doing so that it can move to the finished state. In both cases, a finished (or canceled) operation is still given a chance to execute its completion block before it is removed from the queue.

## See Also

### Related Documentation

- [- cancel](<../operation/cancel().md>) — Advises the operation object that it should stop executing its task.

### Managing Operations in the Queue

- [- addOperation:](<addoperation(__)-64o8a.md>) — Adds the specified operation to the receiver.
- [- addOperations:waitUntilFinished:](<addoperations(__waituntilfinished_).md>) — Adds the specified operations to the queue.
- [- addOperationWithBlock:](<addoperation(__)-5s294.md>) — Wraps the specified block in an operation and adds it to the receiver.
- [- addBarrierBlock:](<addbarrierblock(__).md>) — Invokes a block when the queue finishes all enqueued operations, and prevents subsequent operations from starting until the block has completed.
- [- waitUntilAllOperationsAreFinished](<waituntilalloperationsarefinished().md>) — Blocks the current thread until all the receiver’s queued and executing operations finish executing.
- [operations](operations.md) — The operations currently in the queue. _(deprecated)_
- [operationCount](operationcount.md) — The number of operations currently in the queue. _(deprecated)_

---
title: 'addBarrierBlock(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/operationqueue/addbarrierblock(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/addbarrierblock(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/addbarrierblock%28_%3A%29.json'
content_hash: 'sha256:8eb3f8c97d45a2e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OperationQueue](../operationqueue.md)

# addBarrierBlock(_:)

<sub>Instance Method</sub>

Invokes a block when the queue finishes all enqueued operations, and prevents subsequent operations from starting until the block has completed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addBarrierBlock(_ barrier: @escaping @Sendable () -> Void)
```

## Parameters

- `barrier` — The block to invoke after all currently enqueued operations have finished. Operations you add after the barrier block don’t start until the block has completed.

## Discussion

This method is similar to [dispatch_barrier_async](../../dispatch/dispatch_barrier_async.md).

## See Also

### Managing Operations in the Queue

- [- addOperation:](<addoperation(__)-64o8a.md>) — Adds the specified operation to the receiver.
- [- addOperations:waitUntilFinished:](<addoperations(__waituntilfinished_).md>) — Adds the specified operations to the queue.
- [- addOperationWithBlock:](<addoperation(__)-5s294.md>) — Wraps the specified block in an operation and adds it to the receiver.
- [- cancelAllOperations](<cancelalloperations().md>) — Cancels all queued and executing operations.
- [- waitUntilAllOperationsAreFinished](<waituntilalloperationsarefinished().md>) — Blocks the current thread until all the receiver’s queued and executing operations finish executing.
- [operations](operations.md) — The operations currently in the queue. _(deprecated)_
- [operationCount](operationcount.md) — The number of operations currently in the queue. _(deprecated)_

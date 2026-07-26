---
title: waitUntilAllOperationsAreFinished()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/operationqueue/waituntilalloperationsarefinished()
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/waituntilalloperationsarefinished()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/waituntilalloperationsarefinished%28%29.json'
content_hash: 'sha256:e54c1274f01c1238'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OperationQueue](../operationqueue.md)

# waitUntilAllOperationsAreFinished()

<sub>Instance Method</sub>

Blocks the current thread until all the receiver’s queued and executing operations finish executing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func waitUntilAllOperationsAreFinished()
```

## Discussion

When called, this method blocks the current thread and waits for the receiver’s current and queued operations to finish executing. While the current thread is blocked, the receiver continues to launch already queued operations and monitor those that are executing. During this time, the current thread cannot add operations to the queue, but other threads may. Once all of the pending operations are finished, this method returns.

If there are no operations in the queue, this method returns immediately.

## See Also

### Managing Operations in the Queue

- [- addOperation:](<addoperation(__)-64o8a.md>) — Adds the specified operation to the receiver.
- [- addOperations:waitUntilFinished:](<addoperations(__waituntilfinished_).md>) — Adds the specified operations to the queue.
- [- addOperationWithBlock:](<addoperation(__)-5s294.md>) — Wraps the specified block in an operation and adds it to the receiver.
- [- addBarrierBlock:](<addbarrierblock(__).md>) — Invokes a block when the queue finishes all enqueued operations, and prevents subsequent operations from starting until the block has completed.
- [- cancelAllOperations](<cancelalloperations().md>) — Cancels all queued and executing operations.
- [operations](operations.md) — The operations currently in the queue. _(deprecated)_
- [operationCount](operationcount.md) — The number of operations currently in the queue. _(deprecated)_

---
title: 'addOperation(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/operationqueue/addoperation(_:)-64o8a'
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/addoperation(_:)-64o8a'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/addoperation%28_%3A%29-64o8a.json'
content_hash: 'sha256:52031aa2a2a4861b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OperationQueue](../operationqueue.md)

# addOperation(_:)

<sub>Instance Method</sub>

Adds the specified operation to the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addOperation(_ op: Operation)
```

## Parameters

- `op` — The operation to be added to the queue.

## Discussion

Once added, the specified operation remains in the queue until it finishes executing.

> [!important] Important
> An operation object can be in at most one operation queue at a time and this method throws an [NSInvalidArgumentException](../nsexceptionname/invalidargumentexception.md) exception if the operation is already in another queue. Similarly, this method throws an [NSInvalidArgumentException](../nsexceptionname/invalidargumentexception.md) exception if the operation is currently executing or has already finished executing.

## See Also

### Related Documentation

- [- cancel](<../operation/cancel().md>) — Advises the operation object that it should stop executing its task.
- [executing](../operation/isexecuting.md) — A Boolean value indicating whether the operation is currently executing.

### Managing Operations in the Queue

- [- addOperations:waitUntilFinished:](<addoperations(__waituntilfinished_).md>) — Adds the specified operations to the queue.
- [- addOperationWithBlock:](<addoperation(__)-5s294.md>) — Wraps the specified block in an operation and adds it to the receiver.
- [- addBarrierBlock:](<addbarrierblock(__).md>) — Invokes a block when the queue finishes all enqueued operations, and prevents subsequent operations from starting until the block has completed.
- [- cancelAllOperations](<cancelalloperations().md>) — Cancels all queued and executing operations.
- [- waitUntilAllOperationsAreFinished](<waituntilalloperationsarefinished().md>) — Blocks the current thread until all the receiver’s queued and executing operations finish executing.
- [operations](operations.md) — The operations currently in the queue. _(deprecated)_
- [operationCount](operationcount.md) — The number of operations currently in the queue. _(deprecated)_

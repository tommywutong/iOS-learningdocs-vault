---
title: 'addOperation(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/operationqueue/addoperation(_:)-5s294'
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/addoperation(_:)-5s294'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/addoperation%28_%3A%29-5s294.json'
content_hash: 'sha256:7fd3a76715110b88'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OperationQueue](../operationqueue.md)

# addOperation(_:)

<sub>Instance Method</sub>

Wraps the specified block in an operation and adds it to the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addOperation(_ block: @escaping @Sendable () -> Void)
```

## Parameters

- `block` — The block to execute from the operation. The block takes no parameters and has no return value.

## Discussion

This method adds a single block to the receiver by first wrapping it in an operation object. You should not attempt to get a reference to the newly created operation object or determine its type information.

## See Also

### Related Documentation

- [- cancel](<../operation/cancel().md>) — Advises the operation object that it should stop executing its task.
- [executing](../operation/isexecuting.md) — A Boolean value indicating whether the operation is currently executing.

### Managing Operations in the Queue

- [- addOperation:](<addoperation(__)-64o8a.md>) — Adds the specified operation to the receiver.
- [- addOperations:waitUntilFinished:](<addoperations(__waituntilfinished_).md>) — Adds the specified operations to the queue.
- [- addBarrierBlock:](<addbarrierblock(__).md>) — Invokes a block when the queue finishes all enqueued operations, and prevents subsequent operations from starting until the block has completed.
- [- cancelAllOperations](<cancelalloperations().md>) — Cancels all queued and executing operations.
- [- waitUntilAllOperationsAreFinished](<waituntilalloperationsarefinished().md>) — Blocks the current thread until all the receiver’s queued and executing operations finish executing.
- [operations](operations.md) — The operations currently in the queue. _(deprecated)_
- [operationCount](operationcount.md) — The number of operations currently in the queue. _(deprecated)_

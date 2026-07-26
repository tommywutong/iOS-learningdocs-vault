---
title: operations
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.5+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/operationqueue/operations
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/operations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/operations.json'
content_hash: 'sha256:b0fc9d47552d1b88'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OperationQueue](../operationqueue.md)

# operations

<sub>Instance Property</sub>

The operations currently in the queue.

> [!warning] Deprecated
> To avoid race conditions while accessing operations, use [- addBarrierBlock:](<addbarrierblock(__).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var operations: [Operation] { get }
```

## Discussion

The array in this property contains zero or more [Operation](../operation.md) objects in the order you added them to the queue. This order doesn’t necessarily reflect the order in which the queue invokes those operations.

You can use this property to access the operations queued at any given moment. Operations remain queued until they finish their task. Therefore, the array may contain operations that are currently running or waiting to run. The list may also contain operations that were running when you retrieved the array but have subsequently finished.

You can monitor changes to the value of this property using [Key-value observing](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KVO.html#//apple_ref/doc/uid/TP40008195-CH16) (KVO). Configure an observer to monitor the [operations](operations.md) key path of the operation queue.

## See Also

### Managing Operations in the Queue

- [- addOperation:](<addoperation(__)-64o8a.md>) — Adds the specified operation to the receiver.
- [- addOperations:waitUntilFinished:](<addoperations(__waituntilfinished_).md>) — Adds the specified operations to the queue.
- [- addOperationWithBlock:](<addoperation(__)-5s294.md>) — Wraps the specified block in an operation and adds it to the receiver.
- [- addBarrierBlock:](<addbarrierblock(__).md>) — Invokes a block when the queue finishes all enqueued operations, and prevents subsequent operations from starting until the block has completed.
- [- cancelAllOperations](<cancelalloperations().md>) — Cancels all queued and executing operations.
- [- waitUntilAllOperationsAreFinished](<waituntilalloperationsarefinished().md>) — Blocks the current thread until all the receiver’s queued and executing operations finish executing.
- [operationCount](operationcount.md) — The number of operations currently in the queue. _(deprecated)_

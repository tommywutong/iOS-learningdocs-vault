---
title: operationCount
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（27.0 起废弃）, iPadOS 4.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.6+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/operationqueue/operationcount
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/operationcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/operationcount.json'
content_hash: 'sha256:ccaaeeb163064615'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OperationQueue](../operationqueue.md)

# operationCount

<sub>Instance Property</sub>

The number of operations currently in the queue.

> [!warning] Deprecated
> To avoid race conditions while accessing operations, use [- addBarrierBlock:](<addbarrierblock(__).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var operationCount: Int { get }
```

## Discussion

Because the number of operations in the queue changes as those operations finish executing, the value returned by this property reflects the instantaneous number of operations at the time the property was accessed. By the time you use the value, the actual number of operations may be different. As a result, do not use this value for object enumerations or other precise calculations.

You may monitor changes to the value of this property using [Key-value observing](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KVO.html#//apple_ref/doc/uid/TP40008195-CH16). Configure an observer to monitor the [operationCount](operationcount.md) key path of the operation queue.

## See Also

### Managing Operations in the Queue

- [- addOperation:](<addoperation(__)-64o8a.md>) — Adds the specified operation to the receiver.
- [- addOperations:waitUntilFinished:](<addoperations(__waituntilfinished_).md>) — Adds the specified operations to the queue.
- [- addOperationWithBlock:](<addoperation(__)-5s294.md>) — Wraps the specified block in an operation and adds it to the receiver.
- [- addBarrierBlock:](<addbarrierblock(__).md>) — Invokes a block when the queue finishes all enqueued operations, and prevents subsequent operations from starting until the block has completed.
- [- cancelAllOperations](<cancelalloperations().md>) — Cancels all queued and executing operations.
- [- waitUntilAllOperationsAreFinished](<waituntilalloperationsarefinished().md>) — Blocks the current thread until all the receiver’s queued and executing operations finish executing.
- [operations](operations.md) — The operations currently in the queue. _(deprecated)_

---
title: 'addOperations(_:waitUntilFinished:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/operationqueue/addoperations(_:waituntilfinished:)'
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/addoperations(_:waituntilfinished:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/addoperations%28_%3Awaituntilfinished%3A%29.json'
content_hash: 'sha256:2231e61c17998f24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OperationQueue](../operationqueue.md)

# addOperations(_:waitUntilFinished:)

<sub>Instance Method</sub>

Adds the specified operations to the queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addOperations(_ ops: [Operation], waitUntilFinished wait: Bool)
```

## Parameters

- `ops` — The operations to be added to the queue.

- `wait` — If [true](../../swift/true.md), the current thread is blocked until all of the specified operations finish executing. If [false](../../swift/false.md), the operations are added to the queue and control returns immediately to the caller.

## Discussion

An operation object can be in at most one operation queue at a time and cannot be added if it is currently executing or finished. This method throws an `NSInvalidArgumentException` exception if any of those error conditions are true for any of the operations in the `ops` parameter.

Once added, the specified `operation` remains in the queue until its [finished](../operation/isfinished.md) method returns [true](../../swift/true.md).

## See Also

### Managing Operations in the Queue

- [- addOperation:](<addoperation(__)-64o8a.md>) — Adds the specified operation to the receiver.
- [- addOperationWithBlock:](<addoperation(__)-5s294.md>) — Wraps the specified block in an operation and adds it to the receiver.
- [- addBarrierBlock:](<addbarrierblock(__).md>) — Invokes a block when the queue finishes all enqueued operations, and prevents subsequent operations from starting until the block has completed.
- [- cancelAllOperations](<cancelalloperations().md>) — Cancels all queued and executing operations.
- [- waitUntilAllOperationsAreFinished](<waituntilalloperationsarefinished().md>) — Blocks the current thread until all the receiver’s queued and executing operations finish executing.
- [operations](operations.md) — The operations currently in the queue. _(deprecated)_
- [operationCount](operationcount.md) — The number of operations currently in the queue. _(deprecated)_

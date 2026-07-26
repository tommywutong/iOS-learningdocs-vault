---
title: underlyingQueue
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/operationqueue/underlyingqueue
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/underlyingqueue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/underlyingqueue.json'
content_hash: 'sha256:16c87a6890e92ab9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OperationQueue](../operationqueue.md)

# underlyingQueue

<sub>Instance Property</sub>

The dispatch queue that the operation queue uses to invoke operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
unowned(unsafe) var underlyingQueue: dispatch_queue_t? { get set }
```

## Discussion

The default value of this property is `nil`. You can set the value of this property to an existing dispatch queue to have enqueued operations interspersed with blocks submitted to that dispatch queue.

The value of this property should only be set if there are no operations in the queue; setting the value of this property when [operationCount](operationcount.md) is not equal to `0` raises an [NSInvalidArgumentException](../nsexceptionname/invalidargumentexception.md). The value of this property must not be the value returned by [dispatch_get_main_queue](../../dispatch/dispatch_get_main_queue.md). The quality-of-service level set for the underlying dispatch queue overrides any value set for the operation queue’s [qualityOfService](qualityofservice.md) property.

> [!note] Note
> This property automatically retains its assigned queue if `OS_OBJECT_IS_OBJC` is [true](../../swift/true.md).

## See Also

### Configuring the Queue

- [name](name.md) — The name of the operation queue.

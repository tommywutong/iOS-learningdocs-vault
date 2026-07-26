---
title: isSuspended
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/operationqueue/issuspended
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/issuspended'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/issuspended.json'
content_hash: 'sha256:3aa0669a1e6fd9fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OperationQueue](../operationqueue.md)

# isSuspended

<sub>Instance Property</sub>

A Boolean value indicating whether the queue is actively scheduling operations for execution.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isSuspended: Bool { get set }
```

## Discussion

When the value of this property is [false](../../swift/false.md), the queue actively starts operations that are in the queue and ready to execute. Setting this property to [true](../../swift/true.md) prevents the queue from starting any queued operations, but already executing operations continue to execute. You may continue to add operations to a queue that is suspended but those operations are not scheduled for execution until you change this property to [false](../../swift/false.md).

Operations are removed from the queue only when they finish executing. However, in order to finish executing, an operation must first be started. Because a suspended queue does not start any new operations, it does not remove any operations (including cancelled operations) that are currently queued and not executing.

You may monitor changes to the value of this property using [Key-value observing](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KVO.html#//apple_ref/doc/uid/TP40008195-CH16). Configure an observer to monitor the [suspended](issuspended.md) key path of the operation queue.

The default value of this property is [false](../../swift/false.md).

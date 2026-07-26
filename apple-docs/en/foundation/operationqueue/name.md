---
title: name
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/operationqueue/name
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/name.json'
content_hash: 'sha256:7fbf128f08c3f355'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OperationQueue](../operationqueue.md)

# name

<sub>Instance Property</sub>

The name of the operation queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var name: String? { get set }
```

## Discussion

Names provide a way for you to identify your operation queues at run time. Tools may also use this name to provide additional context during debugging or analysis of your code.

The default value of this property is a string containing the memory address of the operation queue. You may monitor changes to the value of this property using [Key-value observing](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KVO.html#//apple_ref/doc/uid/TP40008195-CH16). Configure an observer to monitor the [name](name.md) key path of the operation queue.

## See Also

### Configuring the Queue

- [underlyingQueue](underlyingqueue.md) — The dispatch queue that the operation queue uses to invoke operations.

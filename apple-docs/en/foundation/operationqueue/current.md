---
title: current
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/operationqueue/current
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/current'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/current.json'
content_hash: 'sha256:43d13d25e81ba62e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OperationQueue](../operationqueue.md)

# current

<sub>Type Property</sub>

Returns the operation queue that launched the current operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var current: OperationQueue? { get }
```

## Return Value

The operation queue that started the operation or `nil` if the queue could not be determined.

## Discussion

You can use this method from within a running operation object to get a reference to the operation queue that started it. Calling this method from outside the context of a running operation typically results in `nil` being returned.

## See Also

### Related Documentation

- [Concurrency Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091)

### Accessing Specific Operation Queues

- [mainQueue](main.md) — Returns the operation queue associated with the main thread.

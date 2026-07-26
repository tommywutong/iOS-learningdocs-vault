---
title: main
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/operationqueue/main
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/main'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/main.json'
content_hash: 'sha256:616078ca2a4fbc07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OperationQueue](../operationqueue.md)

# main

<sub>Type Property</sub>

Returns the operation queue associated with the main thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var main: OperationQueue { get }
```

## Return Value

The default operation queue bound to the main thread.

## Discussion

The returned queue executes one operation at a time on the app’s main thread. The execution of operations on the main thread is interleaved with the other tasks that must execute on the main thread, such as the servicing of events and the updating of an app’s user interface. The queue executes those operations in the run loop common modes, as represented by the [NSRunLoopCommonModes](../runloop/mode/common.md) constant. The value of the [underlyingQueue](underlyingqueue.md) property for the queue is the dispatch queue for the main thread; this property cannot be set to another value.

## See Also

### Accessing Specific Operation Queues

- [currentQueue](current.md) — Returns the operation queue that launched the current operation.

---
title: defaultMaxConcurrentOperationCount
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/operationqueue/defaultmaxconcurrentoperationcount
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/defaultmaxconcurrentoperationcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/defaultmaxconcurrentoperationcount.json'
content_hash: 'sha256:00ef94bb42cf394a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OperationQueue](../operationqueue.md)

# defaultMaxConcurrentOperationCount

<sub>Type Property</sub>

The default maximum number of operations to invoke concurrently in a queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var defaultMaxConcurrentOperationCount: Int { get }
```

## Discussion

The operation queue determines this number dynamically based on current system conditions.

## See Also

### Managing the Execution of Operations

- [qualityOfService](qualityofservice.md) — The default service level to apply to operations that the queue invokes.
- [maxConcurrentOperationCount](maxconcurrentoperationcount.md) — The maximum number of queued operations that can run at the same time.

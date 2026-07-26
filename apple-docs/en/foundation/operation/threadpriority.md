---
title: threadPriority
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（8.0 起废弃）, iPadOS 4.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.6+（10.10 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/operation/threadpriority
source_url: 'https://developer.apple.com/documentation/foundation/operation/threadpriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operation/threadpriority.json'
content_hash: 'sha256:a0a27484b029d498'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Operation](../operation.md)

# threadPriority

<sub>Instance Property</sub>

The thread priority to use when executing the operation

> [!warning] Deprecated
> Use [qualityOfService](qualityofservice.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var threadPriority: Double { get set }
```

## See Also

### Configuring the Execution Priority

- [qualityOfService](qualityofservice.md) — The relative amount of importance for granting system resources to the operation.
- [queuePriority](queuepriority-swift.property.md) — The execution priority of the operation in an operation queue.

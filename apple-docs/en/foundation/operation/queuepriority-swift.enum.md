---
title: Operation.QueuePriority
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/operation/queuepriority-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/operation/queuepriority-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operation/queuepriority-swift.enum.json'
content_hash: 'sha256:3428b4c10c2bbcff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Operation](../operation.md)

# Operation.QueuePriority

<sub>Enumeration</sub>

These constants let you prioritize the order in which operations execute.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum QueuePriority
```

## Overview

You can use these constants to specify the relative ordering of operations that are waiting to be started in an operation queue. You should always use these constants (and not the defined value) for determining priority.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSOperationQueuePriorityVeryLow](queuepriority-swift.enum/verylow.md) — Operations receive very low priority for execution.
- [NSOperationQueuePriorityLow](queuepriority-swift.enum/low.md) — Operations receive low priority for execution.
- [NSOperationQueuePriorityNormal](queuepriority-swift.enum/normal.md) — Operations receive the normal priority for execution.
- [NSOperationQueuePriorityHigh](queuepriority-swift.enum/high.md) — Operations receive high priority for execution.
- [NSOperationQueuePriorityVeryHigh](queuepriority-swift.enum/veryhigh.md) — Operations receive very high priority for execution.

### Initializers

- [init(rawValue:)](<queuepriority-swift.enum/init(rawvalue_).md>)

## See Also

### Constants

- [QualityOfService](../qualityofservice.md) — Constants that indicate the nature and importance of work to the system.

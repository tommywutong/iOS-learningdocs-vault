---
title: QualityOfService
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/qualityofservice
source_url: 'https://developer.apple.com/documentation/foundation/qualityofservice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/qualityofservice.json'
content_hash: 'sha256:25b8b55c45a798f0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# QualityOfService

<sub>Enumeration</sub>

Constants that indicate the nature and importance of work to the system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum QualityOfService
```

## Overview

Work with higher quality of service classes receive more resources than work with lower quality of service classes whenever there’s resource contention.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [NSQualityOfServiceUserInteractive](qualityofservice/userinteractive.md)
- [NSQualityOfServiceUserInitiated](qualityofservice/userinitiated.md)
- [NSQualityOfServiceUtility](qualityofservice/utility.md)
- [NSQualityOfServiceBackground](qualityofservice/background.md)
- [NSQualityOfServiceDefault](qualityofservice/default.md)

### Initializers

- [init(rawValue:)](<qualityofservice/init(rawvalue_).md>)

## See Also

### Constants

- [QueuePriority](operation/queuepriority-swift.enum.md) — These constants let you prioritize the order in which operations execute.

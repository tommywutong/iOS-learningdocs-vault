---
title: NSBackgroundActivityScheduler.Result
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsbackgroundactivityscheduler/result
source_url: 'https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/result'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbackgroundactivityscheduler/result.json'
content_hash: 'sha256:b1f5cb9ff1d417bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSBackgroundActivityScheduler](../nsbackgroundactivityscheduler.md)

# NSBackgroundActivityScheduler.Result

<sub>Enumeration</sub>

These constants indicate whether background activity has been completed successfully or whether additional processing should be deferred until a more optimal time.

<sub>macOS</sub>

```swift
enum Result
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSBackgroundActivityResultFinished](result/finished.md) — The activity has finished executing. If the activity repeats, the next invocation is scheduled by the system.
- [NSBackgroundActivityResultDeferred](result/deferred.md) — System conditions have changed since the time the activity began executing, and deferral of additional work is recommended.

### Initializers

- [init(rawValue:)](<result/init(rawvalue_).md>)

## See Also

### Constants

- [QualityOfService](../qualityofservice.md) — Constants that indicate the nature and importance of work to the system.

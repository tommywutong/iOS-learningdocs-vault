---
title: OperationQueue.SchedulerOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/operationqueue/scheduleroptions
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/scheduleroptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/scheduleroptions.json'
content_hash: 'sha256:b7a12b62b4f3d37f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OperationQueue](../operationqueue.md)

# OperationQueue.SchedulerOptions

<sub>Structure</sub>

A type that defines options the operation queue accepts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SchedulerOptions
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## See Also

### Scheduling Operations

- [schedule(after:tolerance:options:_:)](<schedule(after_tolerance_options___).md>) — Performs the action at some time after the specified date, optionally taking into account tolerance if possible.
- [schedule(after:interval:tolerance:options:_:)](<schedule(after_interval_tolerance_options___).md>) — Performs the action at some time after the specified date, at the specified frequency, optionally taking into account tolerance if possible.
- [schedule(options:_:)](<schedule(options___).md>) — Performs the action at the next possible opportunity.
- [now](now.md) — The operation queue’s definition of the current moment in time.
- [minimumTolerance](minimumtolerance.md) — The minimum tolerance the dispatch queue scheduler allows.
- [SchedulerTimeType](schedulertimetype.md) — The scheduler time type the operation queue uses.

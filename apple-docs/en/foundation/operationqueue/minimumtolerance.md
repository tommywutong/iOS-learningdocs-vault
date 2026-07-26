---
title: minimumTolerance
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/operationqueue/minimumtolerance
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/minimumtolerance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/minimumtolerance.json'
content_hash: 'sha256:c0aaa81a8a364dcf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OperationQueue](../operationqueue.md)

# minimumTolerance

<sub>Instance Property</sub>

The minimum tolerance the dispatch queue scheduler allows.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var minimumTolerance: OperationQueue.SchedulerTimeType.Stride { get }
```

## See Also

### Scheduling Operations

- [schedule(after:tolerance:options:_:)](<schedule(after_tolerance_options___).md>) — Performs the action at some time after the specified date, optionally taking into account tolerance if possible.
- [schedule(after:interval:tolerance:options:_:)](<schedule(after_interval_tolerance_options___).md>) — Performs the action at some time after the specified date, at the specified frequency, optionally taking into account tolerance if possible.
- [schedule(options:_:)](<schedule(options___).md>) — Performs the action at the next possible opportunity.
- [now](now.md) — The operation queue’s definition of the current moment in time.
- [SchedulerTimeType](schedulertimetype.md) — The scheduler time type the operation queue uses.
- [SchedulerOptions](scheduleroptions.md) — A type that defines options the operation queue accepts.

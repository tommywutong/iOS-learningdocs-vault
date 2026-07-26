---
title: now
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/operationqueue/now
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/now'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/now.json'
content_hash: 'sha256:71e9fe3a877ea87b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OperationQueue](../operationqueue.md)

# now

<sub>Instance Property</sub>

The operation queue’s definition of the current moment in time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var now: OperationQueue.SchedulerTimeType { get }
```

## See Also

### Scheduling Operations

- [schedule(after:tolerance:options:_:)](<schedule(after_tolerance_options___).md>) — Performs the action at some time after the specified date, optionally taking into account tolerance if possible.
- [schedule(after:interval:tolerance:options:_:)](<schedule(after_interval_tolerance_options___).md>) — Performs the action at some time after the specified date, at the specified frequency, optionally taking into account tolerance if possible.
- [schedule(options:_:)](<schedule(options___).md>) — Performs the action at the next possible opportunity.
- [minimumTolerance](minimumtolerance.md) — The minimum tolerance the dispatch queue scheduler allows.
- [SchedulerTimeType](schedulertimetype.md) — The scheduler time type the operation queue uses.
- [SchedulerOptions](scheduleroptions.md) — A type that defines options the operation queue accepts.

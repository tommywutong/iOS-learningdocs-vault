---
title: 'schedule(after:tolerance:options:_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/operationqueue/schedule(after:tolerance:options:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/schedule(after:tolerance:options:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/schedule%28after%3Atolerance%3Aoptions%3A_%3A%29.json'
content_hash: 'sha256:9738b3ab599e303f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OperationQueue](../operationqueue.md)

# schedule(after:tolerance:options:_:)

<sub>Instance Method</sub>

Performs the action at some time after the specified date, optionally taking into account tolerance if possible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func schedule(after date: OperationQueue.SchedulerTimeType, tolerance: OperationQueue.SchedulerTimeType.Stride, options: OperationQueue.SchedulerOptions?, _ action: @escaping () -> Void)
```

## See Also

### Scheduling Operations

- [schedule(after:interval:tolerance:options:_:)](<schedule(after_interval_tolerance_options___).md>) — Performs the action at some time after the specified date, at the specified frequency, optionally taking into account tolerance if possible.
- [schedule(options:_:)](<schedule(options___).md>) — Performs the action at the next possible opportunity.
- [now](now.md) — The operation queue’s definition of the current moment in time.
- [minimumTolerance](minimumtolerance.md) — The minimum tolerance the dispatch queue scheduler allows.
- [SchedulerTimeType](schedulertimetype.md) — The scheduler time type the operation queue uses.
- [SchedulerOptions](scheduleroptions.md) — A type that defines options the operation queue accepts.

---
title: 'schedule(options:_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/operationqueue/schedule(options:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/schedule(options:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/schedule%28options%3A_%3A%29.json'
content_hash: 'sha256:938f780c34d9be5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OperationQueue](../operationqueue.md)

# schedule(options:_:)

<sub>Instance Method</sub>

Performs the action at the next possible opportunity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func schedule(options: OperationQueue.SchedulerOptions?, _ action: @escaping () -> Void)
```

## See Also

### Scheduling Operations

- [schedule(after:tolerance:options:_:)](<schedule(after_tolerance_options___).md>) — Performs the action at some time after the specified date, optionally taking into account tolerance if possible.
- [schedule(after:interval:tolerance:options:_:)](<schedule(after_interval_tolerance_options___).md>) — Performs the action at some time after the specified date, at the specified frequency, optionally taking into account tolerance if possible.
- [now](now.md) — The operation queue’s definition of the current moment in time.
- [minimumTolerance](minimumtolerance.md) — The minimum tolerance the dispatch queue scheduler allows.
- [SchedulerTimeType](schedulertimetype.md) — The scheduler time type the operation queue uses.
- [SchedulerOptions](scheduleroptions.md) — A type that defines options the operation queue accepts.

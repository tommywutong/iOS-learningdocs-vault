---
title: 'schedule(after:tolerance:options:_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/runloop/schedule(after:tolerance:options:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/runloop/schedule(after:tolerance:options:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/schedule%28after%3Atolerance%3Aoptions%3A_%3A%29.json'
content_hash: 'sha256:b810702dbf2b49e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RunLoop](../runloop.md)

# schedule(after:tolerance:options:_:)

<sub>Instance Method</sub>

Performs the action at some time after the specified date, using the specified tolerance and options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func schedule(after date: RunLoop.SchedulerTimeType, tolerance: RunLoop.SchedulerTimeType.Stride, options: RunLoop.SchedulerOptions?, _ action: @escaping () -> Void)
```

## See Also

### Scheduling Combine Publishers

- [schedule(options:_:)](<schedule(options___).md>) — Performs the action at some time after the specified date, using the scheduler’s minimum tolerance.
- [schedule(after:interval:tolerance:options:_:)](<schedule(after_interval_tolerance_options___).md>) — Performs the action at some time after the specified date, at the specified frequency, using the specified tolerance and options.
- [minimumTolerance](minimumtolerance.md) — The minimum tolerance the run loop scheduler allows.
- [now](now.md) — The run loop scheduler’s definition of the current moment in time.
- [SchedulerTimeType](schedulertimetype.md) — The scheduler time type that the run loop uses.
- [SchedulerOptions](scheduleroptions.md) — A set of options that affect the operation of the run loop scheduler.

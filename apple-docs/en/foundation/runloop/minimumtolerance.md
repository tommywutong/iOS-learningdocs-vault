---
title: minimumTolerance
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/runloop/minimumtolerance
source_url: 'https://developer.apple.com/documentation/foundation/runloop/minimumtolerance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/minimumtolerance.json'
content_hash: 'sha256:406b2fd0ea927bd2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RunLoop](../runloop.md)

# minimumTolerance

<sub>Instance Property</sub>

The minimum tolerance the run loop scheduler allows.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var minimumTolerance: RunLoop.SchedulerTimeType.Stride { get }
```

## See Also

### Scheduling Combine Publishers

- [schedule(options:_:)](<schedule(options___).md>) — Performs the action at some time after the specified date, using the scheduler’s minimum tolerance.
- [schedule(after:tolerance:options:_:)](<schedule(after_tolerance_options___).md>) — Performs the action at some time after the specified date, using the specified tolerance and options.
- [schedule(after:interval:tolerance:options:_:)](<schedule(after_interval_tolerance_options___).md>) — Performs the action at some time after the specified date, at the specified frequency, using the specified tolerance and options.
- [now](now.md) — The run loop scheduler’s definition of the current moment in time.
- [SchedulerTimeType](schedulertimetype.md) — The scheduler time type that the run loop uses.
- [SchedulerOptions](scheduleroptions.md) — A set of options that affect the operation of the run loop scheduler.

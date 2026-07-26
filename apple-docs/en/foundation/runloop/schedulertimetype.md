---
title: RunLoop.SchedulerTimeType
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/runloop/schedulertimetype
source_url: 'https://developer.apple.com/documentation/foundation/runloop/schedulertimetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/schedulertimetype.json'
content_hash: 'sha256:2dac1ca2c111a5b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RunLoop](../runloop.md)

# RunLoop.SchedulerTimeType

<sub>Structure</sub>

The scheduler time type that the run loop uses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SchedulerTimeType
```

## Relationships

- **Conforms To**: [Comparable](../../swift/comparable.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [Strideable](../../swift/strideable.md)

## Topics

### Creating Scheduler Times

- [init(_:)](<schedulertimetype/init(__).md>) — Initializes a run loop scheduler time with the given date.

### Working with Scheduler Time Intervals

- [Stride](schedulertimetype/stride.md) — The interval by which run loop times advance.
- [advanced(by:)](<schedulertimetype/advanced(by_).md>) — Returns a run loop scheduler time calculated by advancing this instance’s time by the given interval.
- [distance(to:)](<schedulertimetype/distance(to_).md>) — Returns the distance to another run loop scheduler time.

### Inspecting Properties

- [date](schedulertimetype/date.md) — The date this type represents.

## See Also

### Scheduling Combine Publishers

- [schedule(options:_:)](<schedule(options___).md>) — Performs the action at some time after the specified date, using the scheduler’s minimum tolerance.
- [schedule(after:tolerance:options:_:)](<schedule(after_tolerance_options___).md>) — Performs the action at some time after the specified date, using the specified tolerance and options.
- [schedule(after:interval:tolerance:options:_:)](<schedule(after_interval_tolerance_options___).md>) — Performs the action at some time after the specified date, at the specified frequency, using the specified tolerance and options.
- [minimumTolerance](minimumtolerance.md) — The minimum tolerance the run loop scheduler allows.
- [now](now.md) — The run loop scheduler’s definition of the current moment in time.
- [SchedulerOptions](scheduleroptions.md) — A set of options that affect the operation of the run loop scheduler.

---
title: OperationQueue.SchedulerTimeType
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/operationqueue/schedulertimetype
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/schedulertimetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/schedulertimetype.json'
content_hash: 'sha256:c5006fa203b16136'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OperationQueue](../operationqueue.md)

# OperationQueue.SchedulerTimeType

<sub>Structure</sub>

The scheduler time type the operation queue uses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SchedulerTimeType
```

## Relationships

- **Conforms To**: [Comparable](../../swift/comparable.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [Strideable](../../swift/strideable.md)

## Topics

### Creating Scheduler Time Types

- [init(_:)](<schedulertimetype/init(__).md>) — Creates an operation queue scheduler time with the given date.

### Managing Scheduler Time Type Properties

- [date](schedulertimetype/date.md) — The date this type represents.
- [advanced(by:)](<schedulertimetype/advanced(by_).md>) — Calculates an operation queue scheduler time by advancing the scheduler time type’s date by the given interval.
- [distance(to:)](<schedulertimetype/distance(to_).md>) — The distance to another operation queue scheduler time.
- [Stride](schedulertimetype/stride.md) — The interval by which operation queue times advance.

## See Also

### Scheduling Operations

- [schedule(after:tolerance:options:_:)](<schedule(after_tolerance_options___).md>) — Performs the action at some time after the specified date, optionally taking into account tolerance if possible.
- [schedule(after:interval:tolerance:options:_:)](<schedule(after_interval_tolerance_options___).md>) — Performs the action at some time after the specified date, at the specified frequency, optionally taking into account tolerance if possible.
- [schedule(options:_:)](<schedule(options___).md>) — Performs the action at the next possible opportunity.
- [now](now.md) — The operation queue’s definition of the current moment in time.
- [minimumTolerance](minimumtolerance.md) — The minimum tolerance the dispatch queue scheduler allows.
- [SchedulerOptions](scheduleroptions.md) — A type that defines options the operation queue accepts.

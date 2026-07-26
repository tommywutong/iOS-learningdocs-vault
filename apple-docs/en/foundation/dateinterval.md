---
title: DateInterval
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/dateinterval
source_url: 'https://developer.apple.com/documentation/foundation/dateinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateinterval.json'
content_hash: 'sha256:f07eeca2bd5029a0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# DateInterval

<sub>Structure</sub>

The span of time between a specific start date and end date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DateInterval
```

## Overview

DateInterval represents a closed date interval in the form of [startDate, endDate].  It is possible for the start and end dates to be the same with a duration of 0.  DateInterval does not support reverse intervals i.e. intervals where the duration is less than 0 and the end date occurs earlier in time than the start date.

## Relationships

- **Conforms To**: [Comparable](../swift/comparable.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [IntentValueConvertible](../appintents/intentvalueconvertible.md), [IntentValueExpressing](../appintents/intentvalueexpressing.md), [ReferenceConvertible](referenceconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Date Interval

- [init()](<dateinterval/init().md>) — Initializes an interval with start and end dates set to the current date and the duration set to `0`.
- [init(start:duration:)](<dateinterval/init(start_duration_).md>) — Initializes an interval with the specified start date and duration.
- [init(start:end:)](<dateinterval/init(start_end_).md>) — Initializes an interval with the specified start and end date.

### Accessing Start Date, End Date, and Duration

- [start](dateinterval/start.md) — The start date.
- [end](dateinterval/end.md) — The end date.
- [duration](dateinterval/duration.md) — The duration.

### Determining Intersections

- [intersection(with:)](<dateinterval/intersection(with_).md>) — Returns an interval that represents the interval where the given date interval and the current instance intersect.
- [intersects(_:)](<dateinterval/intersects(__).md>) — Indicates whether this interval intersects the specified interval.

### Determining Whether a Date Occurs Within a Date Interval

- [contains(_:)](<dateinterval/contains(__).md>) — Indicates whether this interval contains the given date.

### Using Reference Types

- [NSDateInterval](nsdateinterval.md) — An object representing the span of time between a specific start date and end date.

### Instance Methods

- [compare(_:)](<dateinterval/compare(__).md>) — Compares two intervals.

## See Also

### Date Representations

- [Date](date.md) — A specific point in time, independent of any calendar or time zone.
- [TimeInterval](timeinterval.md) — A number of seconds.

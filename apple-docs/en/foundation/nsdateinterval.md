---
title: NSDateInterval
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdateinterval
source_url: 'https://developer.apple.com/documentation/foundation/nsdateinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdateinterval.json'
content_hash: 'sha256:551a9deae093df70'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSDateInterval

<sub>Class</sub>

An object representing the span of time between a specific start date and end date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSDateInterval
```

## Overview

In Swift, this object bridges to [DateInterval](dateinterval.md); use [NSDateInterval](nsdateinterval.md) when you need reference semantics or other Foundation-specific behavior.

An `NSDateInterval` object represents a closed interval between two dates. The `NSDateInterval` class provides a programmatic interface for calculating the duration of a time interval and determining whether a date falls within it, as well as comparing date intervals and checking to see whether they intersect.

An `NSDateInterval` object consists of a [startDate](nsdateinterval/startdate.md) and an [endDate](nsdateinterval/enddate.md). The [startDate](nsdateinterval/startdate.md) and [endDate](nsdateinterval/enddate.md) of a date interval can be equal, in which case its [duration](nsdateinterval/duration.md) is `0`. However, [endDate](nsdateinterval/enddate.md) cannot occur earlier than [startDate](nsdateinterval/startdate.md).

You can use the [DateIntervalFormatter](dateintervalformatter.md) class to create string representations of `NSDateInterval` objects that are suitable for display in the current locale.

> [!important] Important
> The Swift overlay to the Foundation framework provides the [DateInterval](dateinterval.md) structure, which bridges to the `NSDateInterval` class. For more information about value types, see [Working with Foundation Types](../swift/working-with-foundation-types.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating Date Intervals

- [- init](<nsdateinterval/init().md>) — Initializes a date interval by setting the start and end date to the current date.
- [- initWithStartDate:duration:](<nsdateinterval/init(start_duration_).md>) — Initializes a date interval with a given start date and duration.
- [- initWithStartDate:endDate:](<nsdateinterval/init(start_end_).md>) — Initializes a date interval from a given start date and end date.
- [- initWithCoder:](<nsdateinterval/init(coder_).md>) — Returns a date interval initialized from data in the given unarchiver.

### Accessing Start Date, End Date, and Duration

- [startDate](nsdateinterval/startdate.md) — The start date of the date interval.
- [endDate](nsdateinterval/enddate.md) — The end date of the date interval.
- [duration](nsdateinterval/duration.md) — The duration of the date interval.

### Comparing Date Intervals

- [- compare:](<nsdateinterval/compare(__).md>) — Compares the receiver with the specified date interval.
- [- isEqualToDateInterval:](<nsdateinterval/isequal(to_).md>) — Indicates whether the receiver is equal to the specified date interval.

### Determining Intersections

- [- intersectsDateInterval:](<nsdateinterval/intersects(__).md>) — Indicates whether the receiver intersects with the specified date interval.
- [- intersectionWithDateInterval:](<nsdateinterval/intersection(with_).md>) — Returns the intersection between the receiver and the specified date interval.

### Determining Whether a Date Occurs Within a Date Interval

- [- containsDate:](<nsdateinterval/contains(__).md>) — Indicates whether the receiver contains the specified date.

### Initializers

- [init(startDate:duration:)](<nsdateinterval/init(startdate_duration_).md>)
- [init(startDate:endDate:)](<nsdateinterval/init(startdate_enddate_).md>)

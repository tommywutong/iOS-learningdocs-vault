---
title: Date
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date
source_url: 'https://developer.apple.com/documentation/foundation/date'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date.json'
content_hash: 'sha256:c6ff6a65a8dc08fd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Date

<sub>Structure</sub>

A specific point in time, independent of any calendar or time zone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Date
```

## Overview

A [Date](date.md) value encapsulates a single point in time, independent of any particular calendrical system or time zone. Date values represent a time interval relative to an absolute reference date.

The [Date](date.md) structure provides methods for comparing dates, calculating the time interval between two dates, and creating a new date from a time interval relative to another date. Use date values in conjunction with [DateFormatter](dateformatter.md) instances to create localized representations of dates and times and with [Calendar](calendar.md) instances to perform calendar arithmetic.

[Date](date.md) bridges to the [NSDate](nsdate.md) class. You can use these interchangeably in code that interacts with Objective-C APIs.

## Relationships

- **Conforms To**: [CKRecordValueProtocol](../cloudkit/ckrecordvalueprotocol.md), [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md), [Comparable](../swift/comparable.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [IntentValueConvertible](../appintents/intentvalueconvertible.md), [IntentValueExpressing](../appintents/intentvalueexpressing.md), [Plottable](../charts/plottable.md), [PrimitivePlottableProtocol](../charts/primitiveplottableprotocol.md), [ReferenceConvertible](referenceconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Strideable](../swift/strideable.md)

## Topics

### Creating a Date

- [init()](<date/init().md>) — Creates a date value initialized to the current date and time.
- [init(timeIntervalSinceNow:)](<date/init(timeintervalsincenow_).md>) — Creates a date value initialized relative to the current date and time by a given number of seconds.
- [init(timeInterval:since:)](<date/init(timeinterval_since_).md>) — Creates a date value initialized relative to another given date by a given number of seconds.
- [init(timeIntervalSinceReferenceDate:)](<date/init(timeintervalsincereferencedate_).md>) — Creates a date value initialized relative to 00:00:00 UTC on 1 January 2001 by a given number of seconds.
- [init(timeIntervalSince1970:)](<date/init(timeintervalsince1970_).md>) — Creates a date value initialized relative to 00:00:00 UTC on 1 January 1970 by a given number of seconds.

### Retrieving the Current Date

- [now](date/now.md) — Returns a date instance that represents the current date and time, at the moment of access.

### Getting Temporal Boundaries

- [distantFuture](date/distantfuture.md) — A date value representing a date in the distant future.
- [distantPast](date/distantpast.md) — A date value representing a date in the distant past.

### Comparing Dates

- [==(_:_:)](<date/==(____).md>) — Returns true if the two `Date` values represent the same point in time.
- [\>(_:_:)](<date/_(____)-880ns.md>) — Returns true if the left hand `Date` is later in time than the right hand `Date`.
- [\<(_:_:)](<date/_(____)-42kro.md>) — Returns true if the left hand `Date` is earlier in time than the right hand `Date`.
- [compare(_:)](<date/compare(__).md>) — Compares another date to this one.
- [distance(to:)](<date/distance(to_).md>) — Returns the distance from this date to another date, specified as a time interval.

### Getting Time Intervals

- [timeIntervalSince(_:)](<date/timeintervalsince(__).md>) — Returns the interval between this date and another given date.
- [timeIntervalSinceNow](date/timeintervalsincenow.md) — The time interval between the date value and the current date and time.
- [timeIntervalSinceReferenceDate](date/timeintervalsincereferencedate-swift.property.md) — The interval between the date value and 00:00:00 UTC on 1 January 2001.
- [timeIntervalSince1970](date/timeintervalsince1970.md) — The interval between the date value and 00:00:00 UTC on 1 January 1970.
- [timeIntervalSinceReferenceDate](date/timeintervalsincereferencedate-swift.type.property.md) — The interval between 00:00:00 UTC on 1 January 2001 and the current date and time.
- [timeIntervalBetween1970AndReferenceDate](date/timeintervalbetween1970andreferencedate.md) — The number of seconds from 1 January 1970 to the reference date, 1 January 2001.
- [Stride](date/stride.md) — A type alias to define the stride of a date.

### Adding or Subtracting a Time Interval

- [addTimeInterval(_:)](<date/addtimeinterval(__).md>) — Adds a time interval to this date.
- [addingTimeInterval(_:)](<date/addingtimeinterval(__).md>) — Creates a new date value by adding a time interval to this date.
- [advanced(by:)](<date/advanced(by_).md>) — Returns a date offset the specified time interval from this date.
- [+(_:_:)](<date/+(____).md>) — Returns a date with a specified amount of time added to it.
- [+=(_:_:)](<date/+=(____).md>) — Adds a time interval to a date.
- [-(_:_:)](<date/-(____).md>) — Returns a `Date` with a specified amount of time subtracted from it.
- [-=(_:_:)](<date/-=(____).md>) — Subtract a `TimeInterval` from a `Date`.

### Formatting a Date

- [formatted()](<date/formatted().md>) — Generates a locale-aware string representation of a date using the default date format style.
- [formatted(date:time:)](<date/formatted(date_time_).md>) — Generates a locale-aware string representation of a date using specified date and time format styles.
- [formatted(_:)](<date/formatted(__).md>) — Generates a locale-aware string representation of a date using the specified date format style.
- [FormatStyle](date/formatstyle.md) — A structure that creates a locale-appropriate string representation of a date instance and converts strings of dates and times into date instances.
- [RelativeFormatStyle](date/relativeformatstyle.md) — A format style that forms locale-aware string representations of a relative date or time.
- [IntervalFormatStyle](date/intervalformatstyle.md) — A format style that creates string representations of date intervals.
- [ISO8601Format(_:)](<date/iso8601format(__).md>) — Generates a locale-aware string representation of a date using the ISO 8601 date format.
- [ISO8601FormatStyle](date/iso8601formatstyle.md) — A type that converts between dates and their ISO-8601 string representations.

### Describing Dates

- [description](date/description.md) — The representation is useful for debugging only. There are a number of options to acquire a formatted string for a date including: date formatters (see [NSDateFormatter](//apple_ref/occ/cl/NSDateFormatter) and [Data Formatting Guide](//apple_ref/doc/uid/10000029i)), and the `Date` function `description(locale:)`.
- [description(with:)](<date/description(with_).md>) — Returns a string representation of the receiver using the given locale.
- [customPlaygroundQuickLook](date/customplaygroundquicklook.md) — A custom playground Quick Look for the date. _(deprecated)_

### Working with notification messages

- [SystemClockDidChangeMessage](date/systemclockdidchangemessage.md) — A message the system sends when the system clock changes.

### Using Reference Types

- [NSDate](nsdate.md) — A representation of a specific point in time, independent of any calendar or time zone.

### Structures

- [AnchoredRelativeFormatStyle](date/anchoredrelativeformatstyle.md) — A relative format style that is detached from the system time, and instead formats an anchor date relative to the format input.
- [AttributedStyle](date/attributedstyle.md) — A structure that creates a locale-appropriate attributed string representation of a date instance. _(deprecated)_
- [ComponentsFormatStyle](date/componentsformatstyle.md) — A style for formatting a date interval in terms of specific date components.
- [FormatString](date/formatstring.md) — A type that represents a fixed date format string using string interpolation.
- [HTTPFormatStyle](date/httpformatstyle.md) — Options for generating and parsing string representations of dates following the HTTP date format from [RFC 9110 § 5.6.7](https://www.rfc-editor.org/rfc/rfc9110.html#http.date).
- [ParseStrategy](date/parsestrategy.md) — Options for parsing string representations of dates to create a `Date` instance.
- [VerbatimFormatStyle](date/verbatimformatstyle.md) — A style that formats a date with an explicitly-specified style.

### Initializers

- [init(_:strategy:)](<date/init(__strategy_)-2oqi.md>)
- [init(_:strategy:)](<date/init(__strategy_)-6cq9s.md>)

### Type Aliases

- [Specification](date/specification.md)
- [UnwrappedType](date/unwrappedtype.md)
- [ValueType](date/valuetype.md)

### Type Properties

- [defaultResolverSpecification](date/defaultresolverspecification.md)

### Default Implementations

- [CustomStringConvertible Implementations](date/customstringconvertible-implementations.md)
- [Strideable Implementations](date/strideable-implementations.md)

## See Also

### Date Representations

- [DateInterval](dateinterval.md) — The span of time between a specific start date and end date.
- [TimeInterval](timeinterval.md) — A number of seconds.

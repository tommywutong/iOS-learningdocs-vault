---
title: DateComponents
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/datecomponents
source_url: 'https://developer.apple.com/documentation/foundation/datecomponents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponents.json'
content_hash: 'sha256:c176c3a8f8b65894'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# DateComponents

<sub>Structure</sub>

A date or time specified in terms of units (such as year, month, day, hour, and minute) to be evaluated in a calendar system and time zone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DateComponents
```

## Overview

`DateComponents` encapsulates the components of a date in an extendable, structured manner.

It is used to specify a date by providing the temporal components that make up a date and time in a particular calendar: hour, minutes, seconds, day, month, year, and so on. It can also be used to specify a duration of time, for example, 5 hours and 16 minutes. A `DateComponents` is not required to define all the component fields.

When a new instance of `DateComponents` is created, the date components are set to `nil`.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [IntentValueConvertible](../appintents/intentvalueconvertible.md), [IntentValueExpressing](../appintents/intentvalueexpressing.md), [ReferenceConvertible](referenceconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing Date Components

- [init(calendar:timeZone:era:year:month:day:hour:minute:second:nanosecond:weekday:weekdayOrdinal:quarter:weekOfMonth:weekOfYear:yearForWeekOfYear:)](<datecomponents/init(calendar_timezone_era_year_month_day_hour_minute_second_nanosecond_weekday_weekdayordinal_quarter_weekofmonth_weekofyear_yearforweekofyear_).md>) — Initializes a date components value, optionally specifying values for its fields.
- [calendar](datecomponents/calendar.md) — The calendar used to interpret the other values in this structure.
- [timeZone](datecomponents/timezone.md) — A time zone.

### Validating a Date

- [isValidDate](datecomponents/isvaliddate.md) — Indicates whether the current combination of properties represents a date which exists in the current calendar.
- [isValidDate(in:)](<datecomponents/isvaliddate(in_).md>) — Indicates whether the current combination of properties represents a date which exists in the specified calendar.
- [date](datecomponents/date.md) — The date calculated from the current components using the stored calendar.

### Accessing Months and Years

- [era](datecomponents/era.md) — An era or count of eras.
- [year](datecomponents/year.md) — A year or count of years.
- [yearForWeekOfYear](datecomponents/yearforweekofyear.md) — The year corresponding to a week-counting week.
- [quarter](datecomponents/quarter.md) — A quarter or count of quarters.
- [month](datecomponents/month.md) — A month or count of months.
- [isLeapMonth](datecomponents/isleapmonth.md) — Set to true if these components represent a leap month.

### Accessing Weeks and Days

- [weekOfMonth](datecomponents/weekofmonth.md) — A week of the month or a count of weeks of the month.
- [weekOfYear](datecomponents/weekofyear.md) — A week of the year or count of the weeks of the year.
- [weekday](datecomponents/weekday.md) — A weekday or count of weekdays.
- [weekdayOrdinal](datecomponents/weekdayordinal.md) — A weekday ordinal or count of weekday ordinals.
- [day](datecomponents/day.md) — A day or count of days.

### Accessing Hours and Seconds

- [hour](datecomponents/hour.md) — An hour or count of hours.
- [minute](datecomponents/minute.md) — A minute or count of minutes.
- [second](datecomponents/second.md) — A second or count of seconds.
- [nanosecond](datecomponents/nanosecond.md) — A nanosecond or count of nanoseconds.

### Accessing Calendar Components

- [value(for:)](<datecomponents/value(for_).md>) — Returns the value of one of the properties, using an enumeration value instead of a property name.
- [setValue(_:for:)](<datecomponents/setvalue(__for_).md>) — Set the value of one of the properties, using an enumeration value instead of a property name.
- [Component](calendar/component.md) — An enumeration for the various components of a calendar date.

### Using Reference Types

- [NSDateComponents](nsdatecomponents.md) — An object that specifies a date or time in terms of units (such as year, month, day, hour, and minute) to be evaluated in a calendar system and time zone.

### Structures

- [HTTPFormatStyle](datecomponents/httpformatstyle.md) — Converts `DateComponents` into RFC 9110-compatible “HTTP date” `String`, and parses in the reverse direction. This parser does not do validation on the individual values of the components. An optional date can be created from the result using `Calendar(identifier: .gregorian).date(from: ...)`. When formatting, missing or invalid fields are filled with default values: `Sun`, `01`, `Jan`, `2000`, `00:00:00`, `GMT`. Note that missing fields may result in an invalid date or time. Other values in the `DateComponents` are ignored.
- [ISO8601FormatStyle](datecomponents/iso8601formatstyle.md) — Options for generating and parsing string representations of dates following the ISO 8601 standard.

### Initializers

- [init(_:strategy:)](<datecomponents/init(__strategy_)-62hv8.md>) — Creates a new `DateComponents` by parsing the given string representation.
- [init(_:strategy:)](<datecomponents/init(__strategy_)-84m93.md>) — Creates a new `DateComponents` by parsing the given representation.
- [init(subscriptionPeriod:)](<datecomponents/init(subscriptionperiod_).md>)

### Instance Properties

- [dayOfYear](datecomponents/dayofyear.md) — A day of the year. For example, in the Gregorian calendar, can go from 1 to 365 or 1 to 366 in leap years.
- [isRepeatedDay](datecomponents/isrepeatedday.md) — Set to true if these components represent a repeated day.

### Instance Methods

- [formatted(_:)](<datecomponents/formatted(__).md>) — Converts `self` to its textual representation.

### Type Aliases

- [Specification](datecomponents/specification.md)
- [UnwrappedType](datecomponents/unwrappedtype.md)
- [ValueType](datecomponents/valuetype.md)

### Type Properties

- [defaultResolverSpecification](datecomponents/defaultresolverspecification.md)

## See Also

### Calendrical Calculations

- [Calendar](calendar.md) — A definition of the relationships between calendar units and absolute points in time, providing features for calculation and comparison of dates.
- [TimeZone](timezone.md) — Information about standard time conventions associated with a specific geopolitical region.

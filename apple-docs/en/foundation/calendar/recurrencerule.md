---
title: Calendar.RecurrenceRule
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/recurrencerule
source_url: 'https://developer.apple.com/documentation/foundation/calendar/recurrencerule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/recurrencerule.json'
content_hash: 'sha256:9723368f3b92c7d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# Calendar.RecurrenceRule

<sub>Structure</sub>

A rule which specifies how often an event should repeat in the future

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct RecurrenceRule
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [IntentValueConvertible](../../appintents/intentvalueconvertible.md), [IntentValueExpressing](../../appintents/intentvalueexpressing.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Type Aliases

- [Specification](recurrencerule/specification.md)
- [UnwrappedType](recurrencerule/unwrappedtype.md)
- [ValueType](recurrencerule/valuetype.md)

### Initializers

- [init(calendar:frequency:interval:end:matchingPolicy:repeatedTimePolicy:months:daysOfTheYear:daysOfTheMonth:weeks:weekdays:hours:minutes:seconds:setPositions:)](<recurrencerule/init(calendar_frequency_interval_end_matchingpolicy_repeatedtimepolicy_months_daysoftheyear_daysofthemonth_weeks_weekdays_hours_minutes_seconds_setpositions_).md>)

### Type Properties

- [defaultResolverSpecification](recurrencerule/defaultresolverspecification.md)

### Structures

- [End](recurrencerule/end-swift.struct.md) — When a recurring event stops recurring.
- [Month](recurrencerule/month.md) — Uniquely identifies a month in any calendar system.

### Instance Properties

- [calendar](recurrencerule/calendar.md) — The calendar in which the recurrence occurs
- [daysOfTheMonth](recurrencerule/daysofthemonth.md) — On which days in the month the event should occur
- [daysOfTheYear](recurrencerule/daysoftheyear.md) — On which days of the year the event may occur.
- [end](recurrencerule/end-swift.property.md) — For how long the event repeats
- [frequency](recurrencerule/frequency-swift.property.md) — How often the event repeats
- [hours](recurrencerule/hours.md) — On which hours of a 24-hour day the event should repeat.
- [interval](recurrencerule/interval.md) — At what interval to repeat
- [matchingPolicy](recurrencerule/matchingpolicy.md) — What to do when a recurrence is not a valid date
- [minutes](recurrencerule/minutes.md) — On which minutes of the hour the event should repeat. Accepts values between 0 and 59
- [months](recurrencerule/months.md) — On which months the event should occur.
- [repeatedTimePolicy](recurrencerule/repeatedtimepolicy.md) — What to do when there are multiple recurrences occurring at the same time of the day but in different time zones due to a daylight saving transition.
- [seconds](recurrencerule/seconds.md) — On which seconds of the minute the event should repeat. Valid values between 0 and 60
- [setPositions](recurrencerule/setpositions.md) — Which occurrences within every interval should be returned
- [weekdays](recurrencerule/weekdays.md) — On which days of the week the event should occur
- [weeks](recurrencerule/weeks.md) — On which weeks of the year the event should occur.

### Instance Methods

- [recurrences(of:in:)](<recurrencerule/recurrences(of_in_)-4y30t.md>) — Find recurrences of the given date
- [recurrences(of:in:)](<recurrencerule/recurrences(of_in_)-7b1ww.md>) — Find recurrences of the given date
- [recurrences(of:in:)](<recurrencerule/recurrences(of_in_)-7k3ha.md>) — Find recurrences of the given date
- [recurrences(of:in:)](<recurrencerule/recurrences(of_in_)-8l967.md>) — Find recurrences of the given date
- [recurrences(of:in:)](<recurrencerule/recurrences(of_in_)-9qfbm.md>) — Find recurrences of the given date

### Type Methods

- [daily(calendar:interval:end:matchingPolicy:repeatedTimePolicy:months:daysOfTheMonth:weekdays:hours:minutes:seconds:setPositions:)](<recurrencerule/daily(calendar_interval_end_matchingpolicy_repeatedtimepolicy_months_daysofthemonth_weekdays_hours_minutes_seconds_setpositions_).md>) — A recurrence that repeats every `interval` days
- [hourly(calendar:interval:end:matchingPolicy:repeatedTimePolicy:months:daysOfTheYear:daysOfTheMonth:weekdays:hours:minutes:seconds:setPositions:)](<recurrencerule/hourly(calendar_interval_end_matchingpolicy_repeatedtimepolicy_months_daysoftheyear_daysofthemonth_weekdays_hours_minutes_seconds_setpositions_).md>) — A recurrence that repeats every `interval` hours
- [minutely(calendar:interval:end:matchingPolicy:repeatedTimePolicy:months:daysOfTheYear:daysOfTheMonth:weekdays:hours:minutes:seconds:setPositions:)](<recurrencerule/minutely(calendar_interval_end_matchingpolicy_repeatedtimepolicy_months_daysoftheyear_daysofthemonth_weekdays_hours_minutes_seconds_setpositions_).md>) — A recurrence that repeats every `interval` minutes
- [monthly(calendar:interval:end:matchingPolicy:repeatedTimePolicy:months:daysOfTheMonth:weekdays:hours:minutes:seconds:setPositions:)](<recurrencerule/monthly(calendar_interval_end_matchingpolicy_repeatedtimepolicy_months_daysofthemonth_weekdays_hours_minutes_seconds_setpositions_).md>) — A recurrence that repeats every `interval` months
- [weekly(calendar:interval:end:matchingPolicy:repeatedTimePolicy:months:weekdays:hours:minutes:seconds:setPositions:)](<recurrencerule/weekly(calendar_interval_end_matchingpolicy_repeatedtimepolicy_months_weekdays_hours_minutes_seconds_setpositions_).md>) — A recurrence that repeats every `interval` weeks
- [yearly(calendar:interval:end:matchingPolicy:repeatedTimePolicy:months:daysOfTheYear:daysOfTheMonth:weeks:weekdays:hours:minutes:seconds:setPositions:)](<recurrencerule/yearly(calendar_interval_end_matchingpolicy_repeatedtimepolicy_months_daysoftheyear_daysofthemonth_weeks_weekdays_hours_minutes_seconds_setpositions_).md>) — A recurrence that repeats every `interval` years

### Enumerations

- [Frequency](recurrencerule/frequency-swift.enum.md) — How often a recurring event repeats
- [Weekday](recurrencerule/weekday.md)

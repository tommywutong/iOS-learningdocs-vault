---
title: Calendar
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar
source_url: 'https://developer.apple.com/documentation/foundation/calendar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar.json'
content_hash: 'sha256:d6e832ffee0c52eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Calendar

<sub>Structure</sub>

A definition of the relationships between calendar units and absolute points in time, providing features for calculation and comparison of dates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Calendar
```

## Overview

`Calendar` encapsulates information about systems of reckoning time in which the beginning, length, and divisions of a year are defined. It provides information about the calendar and support for calendrical computations such as determining the range of a given calendrical unit and adding units to a given absolute time.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [ReferenceConvertible](referenceconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Calendar

- [Identifier](calendar/identifier-swift.enum.md) — An enumeration for the available calendars.

### Getting the User’s Calendar

- [autoupdatingCurrent](calendar/autoupdatingcurrent.md) — A calendar that tracks changes to user’s preferred calendar.
- [current](calendar/current.md) — The user’s current calendar.

### Extracting Components

- [date(_:matchesComponents:)](<calendar/date(__matchescomponents_).md>) — Determines if the date has all of the specified date components.
- [component(_:from:)](<calendar/component(__from_).md>) — Returns the value for one component of a date.
- [dateComponents(_:from:)](<calendar/datecomponents(__from_).md>) — Returns all the date components of a date, using the calendar time zone.
- [dateComponents(_:from:to:)](<calendar/datecomponents(__from_to_)-2kcg.md>) — Returns the difference between two dates.
- [dateComponents(_:from:to:)](<calendar/datecomponents(__from_to_)-5g20t.md>) — Returns the difference between two dates specified as `DateComponents`.
- [dateComponents(in:from:)](<calendar/datecomponents(in_from_).md>) — Returns all the date components of a date, as if in a given time zone (instead of the `Calendar` time zone).
- [Component](calendar/component.md) — An enumeration for the various components of a calendar date.

### Getting Calendar Information

- [identifier](calendar/identifier-swift.property.md) — The identifier of the calendar.
- [locale](calendar/locale.md) — The locale of the calendar.
- [firstWeekday](calendar/firstweekday.md) — The first day of the week for the calendar.
- [minimumDaysInFirstWeek](calendar/minimumdaysinfirstweek.md) — The number of minimum days in the first week.
- [timeZone](calendar/timezone.md) — The time zone of the calendar.
- [maximumRange(of:)](<calendar/maximumrange(of_).md>) — The maximum range limits of the values that a given component can take on.
- [minimumRange(of:)](<calendar/minimumrange(of_).md>) — Returns the minimum range limits of the values that a given component can take on.
- [ordinality(of:in:for:)](<calendar/ordinality(of_in_for_).md>) — Returns, for a given absolute time, the ordinal number of a smaller calendar component (such as a day) within a specified larger calendar component (such as a week).
- [range(of:in:for:)](<calendar/range(of_in_for_).md>) — Returns the range of absolute time values that a smaller calendar component (such as a day) can take on in a larger calendar component (such as a month) that includes a specified absolute time.

### Scanning Dates

- [startOfDay(for:)](<calendar/startofday(for_).md>) — Returns the first moment of a given Date, as a Date.
- [enumerateDates(startingAfter:matching:matchingPolicy:repeatedTimePolicy:direction:using:)](<calendar/enumeratedates(startingafter_matching_matchingpolicy_repeatedtimepolicy_direction_using_).md>) — Computes the dates which match (or most closely match) a given set of components, and calls the closure once for each of them, until the enumeration is stopped.
- [nextDate(after:matching:matchingPolicy:repeatedTimePolicy:direction:)](<calendar/nextdate(after_matching_matchingpolicy_repeatedtimepolicy_direction_).md>) — Computes the next date which matches (or most closely matches) a given set of components.
- [MatchingPolicy](calendar/matchingpolicy.md) — A hint to the search algorithm to control the method used for searching for dates.
- [RepeatedTimePolicy](calendar/repeatedtimepolicy.md) — Determines which result to use when a time is repeated on a day in a calendar (for example, during a daylight saving transition when the times between 2:00am and 3:00am may happen twice).

### Calculating Dates from Components

- [date(from:)](<calendar/date(from_).md>) — Returns a date created from the specified components.
- [date(byAdding:to:wrappingComponents:)](<calendar/date(byadding_to_wrappingcomponents_).md>) — Returns a new `Date` representing the date calculated by adding components to a given date.
- [date(byAdding:value:to:wrappingComponents:)](<calendar/date(byadding_value_to_wrappingcomponents_).md>) — Returns a new `Date` representing the date calculated by adding an amount of a specific component to a given date.
- [date(bySetting:value:of:)](<calendar/date(bysetting_value_of_).md>) — Returns a new `Date` representing the date calculated by setting a specific component to a given time, and trying to keep lower components the same.  If the component already has that value, this may result in a date which is the same as the given date.
- [date(bySettingHour:minute:second:of:matchingPolicy:repeatedTimePolicy:direction:)](<calendar/date(bysettinghour_minute_second_of_matchingpolicy_repeatedtimepolicy_direction_).md>) — Returns a new `Date` representing the date calculated by setting hour, minute, and second to a given time on a specified `Date`.

### Calculating Intervals

- [dateInterval(of:for:)](<calendar/dateinterval(of_for_).md>) — Returns the starting time and duration of a given calendar component that contains a given date.
- [dateInterval(of:start:interval:for:)](<calendar/dateinterval(of_start_interval_for_).md>) — Returns, via two inout parameters, the starting time and duration of a given calendar component that contains a given date.
- [dateIntervalOfWeekend(containing:)](<calendar/dateintervalofweekend(containing_).md>) — Returns a `DateInterval` of the weekend contained by the given date, or `nil` if the date is not in a weekend.
- [dateIntervalOfWeekend(containing:start:interval:)](<calendar/dateintervalofweekend(containing_start_interval_).md>) — Find the range of the weekend around the given date, returned via two by-reference parameters.
- [nextWeekend(startingAfter:direction:)](<calendar/nextweekend(startingafter_direction_).md>) — Returns a `DateInterval` of the next weekend, which starts strictly after the given date.
- [nextWeekend(startingAfter:start:interval:direction:)](<calendar/nextweekend(startingafter_start_interval_direction_).md>) — Returns the range of the next weekend via two inout parameters. The weekend starts strictly after the given date.
- [SearchDirection](calendar/searchdirection.md) — The direction in time to search.

### Comparing Dates

- [compare(_:to:toGranularity:)](<calendar/compare(__to_togranularity_).md>) — Compares two dates down to the specified component.
- [isDate(_:equalTo:toGranularity:)](<calendar/isdate(__equalto_togranularity_).md>) — Returns a Boolean value indicating whether two dates are equal down to the specified component.
- [isDate(_:inSameDayAs:)](<calendar/isdate(__insamedayas_).md>) — Returns a Boolean value indicating whether a date is within the same day as another date.
- [isDateInToday(_:)](<calendar/isdateintoday(__).md>) — Returns a Boolean value indicating whether the given date is within today.
- [isDateInTomorrow(_:)](<calendar/isdateintomorrow(__).md>) — Returns a Boolean value indicating whether the given date is within tomorrow.
- [isDateInYesterday(_:)](<calendar/isdateinyesterday(__).md>) — Returns a Boolean value indicating whether the given date is within yesterday.
- [isDateInWeekend(_:)](<calendar/isdateinweekend(__).md>) — Returns a Boolean value indicating whether the given date is within a weekend period.

### Getting AM and PM symbols

- [amSymbol](calendar/amsymbol.md) — The symbol used to represent “AM”, localized to the Calendar’s `locale`.
- [pmSymbol](calendar/pmsymbol.md) — The symbol used to represent “PM”, localized to the Calendar’s `locale`.

### Getting Weekday Symbols

- [weekdaySymbols](calendar/weekdaysymbols.md) — A list of weekdays in this calendar, localized to the Calendar’s `locale`.
- [shortWeekdaySymbols](calendar/shortweekdaysymbols.md) — A list of shorter-named weekdays in this calendar, localized to the Calendar’s `locale`.
- [veryShortWeekdaySymbols](calendar/veryshortweekdaysymbols.md) — A list of very-shortly-named weekdays in this calendar, localized to the Calendar’s `locale`.
- [standaloneWeekdaySymbols](calendar/standaloneweekdaysymbols.md) — A list of standalone weekday names in this calendar, localized to the Calendar’s `locale`.
- [shortStandaloneWeekdaySymbols](calendar/shortstandaloneweekdaysymbols.md) — A list of shorter-named standalone weekdays in this calendar, localized to the Calendar’s `locale`.
- [veryShortStandaloneWeekdaySymbols](calendar/veryshortstandaloneweekdaysymbols.md) — A list of very-shortly-named weekdays in this calendar, localized to the Calendar’s `locale`.

### Getting Month Symbols

- [monthSymbols](calendar/monthsymbols.md) — A list of months in this calendar, localized to the Calendar’s `locale`.
- [shortMonthSymbols](calendar/shortmonthsymbols.md) — A list of shorter-named months in this calendar, localized to the Calendar’s `locale`.
- [veryShortMonthSymbols](calendar/veryshortmonthsymbols.md) — A list of very-shortly-named months in this calendar, localized to the Calendar’s `locale`.
- [standaloneMonthSymbols](calendar/standalonemonthsymbols.md) — A list of standalone months in this calendar, localized to the Calendar’s `locale`.
- [shortStandaloneMonthSymbols](calendar/shortstandalonemonthsymbols.md) — A list of shorter-named standalone months in this calendar, localized to the Calendar’s `locale`.
- [veryShortStandaloneMonthSymbols](calendar/veryshortstandalonemonthsymbols.md) — A list of very-shortly-named standalone months in this calendar, localized to the Calendar’s `locale`.

### Getting Quarter Symbols

- [quarterSymbols](calendar/quartersymbols.md) — A list of quarter names in this calendar, localized to the Calendar’s `locale`.
- [shortQuarterSymbols](calendar/shortquartersymbols.md) — A list of shorter-named quarters in this calendar, localized to the Calendar’s `locale`.
- [standaloneQuarterSymbols](calendar/standalonequartersymbols.md) — A list of standalone quarter names in this calendar, localized to the Calendar’s `locale`.
- [shortStandaloneQuarterSymbols](calendar/shortstandalonequartersymbols.md) — A list of shorter-named standalone quarters in this calendar, localized to the Calendar’s `locale`.

### Getting Era Symbols

- [eraSymbols](calendar/erasymbols.md) — A list of eras in this calendar, localized to the Calendar’s `locale`.
- [longEraSymbols](calendar/longerasymbols.md) — A list of longer-named eras in this calendar, localized to the Calendar’s `locale`.

### Working with notification messages

- [CalendarDayChangedMessage](calendar/calendardaychangedmessage.md) — A message sent by a calendar when the system’s calendar day changes, as determined by the system calendar, locale, and time zone.

### Using Reference Types

- [NSCalendar](nscalendar.md) — A definition of the relationships between calendar units and absolute points in time, providing features for calculation and comparison of dates.

### Structures

- [RecurrenceRule](calendar/recurrencerule.md) — A rule which specifies how often an event should repeat in the future

### Initializers

- [init(identifier:)](<calendar/init(identifier_).md>) — Returns a new Calendar.

### Instance Methods

- [dates(byAdding:startingAt:in:wrappingComponents:)](<calendar/dates(byadding_startingat_in_wrappingcomponents_).md>) — Returns a sequence of `Date`s, calculated by repeatedly adding an amount of `DateComponents` to a starting `Date` and then to each subsequent result. If a range is supplied, the sequence terminates if the next result is not contained in the range. The starting point does not need to be contained in the range, but if the first result is outside of the range then the result will be an empty sequence.
- [dates(byAdding:value:startingAt:in:wrappingComponents:)](<calendar/dates(byadding_value_startingat_in_wrappingcomponents_).md>) — Returns a sequence of `Date`s, calculated by adding a scaled amount of `Calendar.Component`s to a starting `Date`. If a range is supplied, the sequence terminates if the next result is not contained in the range. The starting point does not need to be contained in the range, but if the first result is outside of the range then the result will be an empty sequence.
- [dates(byMatching:startingAt:in:matchingPolicy:repeatedTimePolicy:direction:)](<calendar/dates(bymatching_startingat_in_matchingpolicy_repeatedtimepolicy_direction_).md>) — Computes the dates which match (or most closely match) a given set of components, returned as a `Sequence`.

## See Also

### Calendrical Calculations

- [DateComponents](datecomponents.md) — A date or time specified in terms of units (such as year, month, day, hour, and minute) to be evaluated in a calendar system and time zone.
- [TimeZone](timezone.md) — Information about standard time conventions associated with a specific geopolitical region.

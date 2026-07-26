---
title: 'CFCalendarGetOrdinalityOfUnit(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcalendargetordinalityofunit(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcalendargetordinalityofunit(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcalendargetordinalityofunit%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:7ec0536f8417d7bf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCalendarGetOrdinalityOfUnit(_:_:_:_:)

<sub>Function</sub>

Returns the ordinal number of a calendrical unit within a larger unit at a specified absolute time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCalendarGetOrdinalityOfUnit(_ calendar: CFCalendar!, _ smallerUnit: CFCalendarUnit, _ biggerUnit: CFCalendarUnit, _ at: CFAbsoluteTime) -> CFIndex
```

## Parameters

- `calendar` — The calendar to examine.

- `smallerUnit` — A calendar unit. For valid values see [CFCalendarUnit](cfcalendarunit.md).

- `biggerUnit` — A calendar unit. For valid values see [CFCalendarUnit](cfcalendarunit.md).

- `at` — An absolute time.

## Return Value

The ordinal number of the calendar unit specified by `smallerUnit` within the calendar unit specified by `biggerUnit` at the absolute time `at`. For example, the time 00:45 is in the first hour of the day, and for units Hour and Day respectively, the result would be 1.

## Discussion

If the `biggerUnit` parameter is not logically bigger than the `smallerUnit` parameter in the calendar, or the given combination of units does not make sense (or is a computation which is undefined), the result is `kCFNotFound`.

## Discussion

The ordinality is in most cases not the same as the decomposed value of the unit. Typically return values are `1` and greater; an exception is the week-in-month calculation, which returns `0` for days before the first week in the month containing the date. Note that some computations can take a relatively long time to perform.

## See Also

### Getting Ranges of Units

- [CFCalendarGetRangeOfUnit](<cfcalendargetrangeofunit(________).md>) — Returns the range of values that one unit can take on within a larger unit during which a specific absolute time occurs.
- [CFCalendarGetTimeRangeOfUnit](<cfcalendargettimerangeofunit(__________).md>) — Returns by reference the start time and duration of a given calendar unit that contains a given absolute time.
- [CFCalendarGetMaximumRangeOfUnit](<cfcalendargetmaximumrangeofunit(____).md>) — Returns the maximum range limits of the values that a specified unit can take on in a given calendar.
- [CFCalendarGetMinimumRangeOfUnit](<cfcalendargetminimumrangeofunit(____).md>) — Returns the minimum range limits of the values that a specified unit can take on in a given calendar.

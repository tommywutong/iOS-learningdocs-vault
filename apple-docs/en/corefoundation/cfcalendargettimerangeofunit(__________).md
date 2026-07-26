---
title: 'CFCalendarGetTimeRangeOfUnit(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcalendargettimerangeofunit(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcalendargettimerangeofunit(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcalendargettimerangeofunit%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:bbef986f9e00a51b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCalendarGetTimeRangeOfUnit(_:_:_:_:_:)

<sub>Function</sub>

Returns by reference the start time and duration of a given calendar unit that contains a given absolute time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCalendarGetTimeRangeOfUnit(_ calendar: CFCalendar!, _ unit: CFCalendarUnit, _ at: CFAbsoluteTime, _ startp: UnsafeMutablePointer<CFAbsoluteTime>!, _ tip: UnsafeMutablePointer<CFTimeInterval>!) -> Bool
```

## Parameters

- `calendar` — The calendar to examine.

- `unit` — A calendar unit (for valid values, see [CFCalendarUnit](cfcalendarunit.md)).

- `at` — An absolute time.

- `startp` — Upon return, contains the beginning of the calendar unit specified by `unit` that contains the time `at`.

- `tip` — Upon return, contains the duration of the calendar unit specified by `unit` that contains the time `at`.

## Return Value

`true` if the values of `startp` and `tip` could be calculated, otherwise `false`.

## Discussion

The function may fail if, for example, you try to get the range of a `kCFCalendarUnitWeekday` and specify a time (`at`) that is during a weekend.

## See Also

### Getting Ranges of Units

- [CFCalendarGetRangeOfUnit](<cfcalendargetrangeofunit(________).md>) — Returns the range of values that one unit can take on within a larger unit during which a specific absolute time occurs.
- [CFCalendarGetOrdinalityOfUnit](<cfcalendargetordinalityofunit(________).md>) — Returns the ordinal number of a calendrical unit within a larger unit at a specified absolute time.
- [CFCalendarGetMaximumRangeOfUnit](<cfcalendargetmaximumrangeofunit(____).md>) — Returns the maximum range limits of the values that a specified unit can take on in a given calendar.
- [CFCalendarGetMinimumRangeOfUnit](<cfcalendargetminimumrangeofunit(____).md>) — Returns the minimum range limits of the values that a specified unit can take on in a given calendar.

---
title: 'CFCalendarGetRangeOfUnit(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcalendargetrangeofunit(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcalendargetrangeofunit(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcalendargetrangeofunit%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:510256fdec916164'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCalendarGetRangeOfUnit(_:_:_:_:)

<sub>Function</sub>

Returns the range of values that one unit can take on within a larger unit during which a specific absolute time occurs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCalendarGetRangeOfUnit(_ calendar: CFCalendar!, _ smallerUnit: CFCalendarUnit, _ biggerUnit: CFCalendarUnit, _ at: CFAbsoluteTime) -> CFRange
```

## Parameters

- `calendar` — The calendar to examine.

- `smallerUnit` — A calendar unit. For valid values see [CFCalendarUnit](cfcalendarunit.md).

- `biggerUnit` — A calendar unit. For valid values see [CFCalendarUnit](cfcalendarunit.md).

- `at` — An absolute time.

## Return Value

The range of values that the calendar unit specified by `smallerUnit` can take on within the calendar unit specified by `biggerUnit` that includes the absolute time `at`. For example, the range the Day unit can take on in the Month in which the absolute time lies.

## Discussion

If `biggerUnit` is not logically bigger than `smallerUnit` in the calendar, or the given combination of units does not make sense (or is a computation which is undefined), the result is `{kCFNotFound, kCFNotFound`}.

## See Also

### Getting Ranges of Units

- [CFCalendarGetOrdinalityOfUnit](<cfcalendargetordinalityofunit(________).md>) — Returns the ordinal number of a calendrical unit within a larger unit at a specified absolute time.
- [CFCalendarGetTimeRangeOfUnit](<cfcalendargettimerangeofunit(__________).md>) — Returns by reference the start time and duration of a given calendar unit that contains a given absolute time.
- [CFCalendarGetMaximumRangeOfUnit](<cfcalendargetmaximumrangeofunit(____).md>) — Returns the maximum range limits of the values that a specified unit can take on in a given calendar.
- [CFCalendarGetMinimumRangeOfUnit](<cfcalendargetminimumrangeofunit(____).md>) — Returns the minimum range limits of the values that a specified unit can take on in a given calendar.

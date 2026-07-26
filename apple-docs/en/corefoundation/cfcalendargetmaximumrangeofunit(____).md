---
title: 'CFCalendarGetMaximumRangeOfUnit(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcalendargetmaximumrangeofunit(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcalendargetmaximumrangeofunit(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcalendargetmaximumrangeofunit%28_%3A_%3A%29.json'
content_hash: 'sha256:bc89aaea7e5a1356'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCalendarGetMaximumRangeOfUnit(_:_:)

<sub>Function</sub>

Returns the maximum range limits of the values that a specified unit can take on in a given calendar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCalendarGetMaximumRangeOfUnit(_ calendar: CFCalendar!, _ unit: CFCalendarUnit) -> CFRange
```

## Parameters

- `calendar` — The calendar to examine.

- `unit` — A calendar unit. For valid values see [CFCalendarUnit](cfcalendarunit.md).

## Return Value

The maximum range limits of the values that the specified unit can take on in `calendar`. For example, in the Gregorian calendar the maximum ranges for the Day unit is 1-31.

## See Also

### Getting Ranges of Units

- [CFCalendarGetRangeOfUnit](<cfcalendargetrangeofunit(________).md>) — Returns the range of values that one unit can take on within a larger unit during which a specific absolute time occurs.
- [CFCalendarGetOrdinalityOfUnit](<cfcalendargetordinalityofunit(________).md>) — Returns the ordinal number of a calendrical unit within a larger unit at a specified absolute time.
- [CFCalendarGetTimeRangeOfUnit](<cfcalendargettimerangeofunit(__________).md>) — Returns by reference the start time and duration of a given calendar unit that contains a given absolute time.
- [CFCalendarGetMinimumRangeOfUnit](<cfcalendargetminimumrangeofunit(____).md>) — Returns the minimum range limits of the values that a specified unit can take on in a given calendar.

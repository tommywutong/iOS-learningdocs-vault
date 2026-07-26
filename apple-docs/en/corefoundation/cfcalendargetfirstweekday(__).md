---
title: 'CFCalendarGetFirstWeekday(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcalendargetfirstweekday(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcalendargetfirstweekday(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcalendargetfirstweekday%28_%3A%29.json'
content_hash: 'sha256:f8965aa06e27acb4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCalendarGetFirstWeekday(_:)

<sub>Function</sub>

Returns the index of first weekday for a specified calendar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCalendarGetFirstWeekday(_ calendar: CFCalendar!) -> CFIndex
```

## Parameters

- `calendar` — The calendar to examine.

## Return Value

The index of the first weekday of the specified calendar.

## See Also

### Getting and Setting Day Information

- [CFCalendarSetFirstWeekday](<cfcalendarsetfirstweekday(____).md>) — Sets the first weekday for a calendar.
- [CFCalendarGetMinimumDaysInFirstWeek](<cfcalendargetminimumdaysinfirstweek(__).md>) — Returns the minimum number of days in the first week of a specified calendar.
- [CFCalendarSetMinimumDaysInFirstWeek](<cfcalendarsetminimumdaysinfirstweek(____).md>) — Sets the minimum number of days in the first week of a specified calendar.

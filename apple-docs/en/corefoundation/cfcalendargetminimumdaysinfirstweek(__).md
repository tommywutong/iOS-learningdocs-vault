---
title: 'CFCalendarGetMinimumDaysInFirstWeek(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcalendargetminimumdaysinfirstweek(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcalendargetminimumdaysinfirstweek(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcalendargetminimumdaysinfirstweek%28_%3A%29.json'
content_hash: 'sha256:99f9f075e5905857'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCalendarGetMinimumDaysInFirstWeek(_:)

<sub>Function</sub>

Returns the minimum number of days in the first week of a specified calendar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCalendarGetMinimumDaysInFirstWeek(_ calendar: CFCalendar!) -> CFIndex
```

## Parameters

- `calendar` — The calendar to examine.

## Return Value

The minimum number of days in the first week of `calendar`.

## See Also

### Getting and Setting Day Information

- [CFCalendarGetFirstWeekday](<cfcalendargetfirstweekday(__).md>) — Returns the index of first weekday for a specified calendar.
- [CFCalendarSetFirstWeekday](<cfcalendarsetfirstweekday(____).md>) — Sets the first weekday for a calendar.
- [CFCalendarSetMinimumDaysInFirstWeek](<cfcalendarsetminimumdaysinfirstweek(____).md>) — Sets the minimum number of days in the first week of a specified calendar.

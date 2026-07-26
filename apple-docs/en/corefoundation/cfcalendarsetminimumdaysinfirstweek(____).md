---
title: 'CFCalendarSetMinimumDaysInFirstWeek(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcalendarsetminimumdaysinfirstweek(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcalendarsetminimumdaysinfirstweek(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcalendarsetminimumdaysinfirstweek%28_%3A_%3A%29.json'
content_hash: 'sha256:dae6822f2fa05768'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCalendarSetMinimumDaysInFirstWeek(_:_:)

<sub>Function</sub>

Sets the minimum number of days in the first week of a specified calendar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCalendarSetMinimumDaysInFirstWeek(_ calendar: CFCalendar!, _ mwd: CFIndex)
```

## Parameters

- `calendar` — The calendar to modify.

- `mwd` — The number to set as the minimum number of days in the first week of `calendar`.

## See Also

### Getting and Setting Day Information

- [CFCalendarGetFirstWeekday](<cfcalendargetfirstweekday(__).md>) — Returns the index of first weekday for a specified calendar.
- [CFCalendarSetFirstWeekday](<cfcalendarsetfirstweekday(____).md>) — Sets the first weekday for a calendar.
- [CFCalendarGetMinimumDaysInFirstWeek](<cfcalendargetminimumdaysinfirstweek(__).md>) — Returns the minimum number of days in the first week of a specified calendar.

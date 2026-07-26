---
title: 'CFCalendarSetFirstWeekday(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcalendarsetfirstweekday(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcalendarsetfirstweekday(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcalendarsetfirstweekday%28_%3A_%3A%29.json'
content_hash: 'sha256:a88c3a3a138bbe5a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCalendarSetFirstWeekday(_:_:)

<sub>Function</sub>

Sets the first weekday for a calendar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCalendarSetFirstWeekday(_ calendar: CFCalendar!, _ wkdy: CFIndex)
```

## Parameters

- `calendar` — The calendar to modify.

- `wkdy` — The index to set for the first weekday of `calendar`.

## See Also

### Getting and Setting Day Information

- [CFCalendarGetFirstWeekday](<cfcalendargetfirstweekday(__).md>) — Returns the index of first weekday for a specified calendar.
- [CFCalendarGetMinimumDaysInFirstWeek](<cfcalendargetminimumdaysinfirstweek(__).md>) — Returns the minimum number of days in the first week of a specified calendar.
- [CFCalendarSetMinimumDaysInFirstWeek](<cfcalendarsetminimumdaysinfirstweek(____).md>) — Sets the minimum number of days in the first week of a specified calendar.

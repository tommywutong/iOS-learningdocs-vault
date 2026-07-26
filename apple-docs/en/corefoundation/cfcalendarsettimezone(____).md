---
title: 'CFCalendarSetTimeZone(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcalendarsettimezone(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcalendarsettimezone(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcalendarsettimezone%28_%3A_%3A%29.json'
content_hash: 'sha256:83e25b2196714e33'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCalendarSetTimeZone(_:_:)

<sub>Function</sub>

Sets the time zone for a calendar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCalendarSetTimeZone(_ calendar: CFCalendar!, _ tz: CFTimeZone!)
```

## Parameters

- `calendar` — The calendar to modify.

- `tz` — The time zone to set for `calendar`.

## See Also

### Getting and Setting the Time Zone

- [CFCalendarCopyTimeZone](<cfcalendarcopytimezone(__).md>) — Returns a time zone object for a specified calendar.

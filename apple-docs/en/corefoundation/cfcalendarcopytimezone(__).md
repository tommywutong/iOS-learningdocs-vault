---
title: 'CFCalendarCopyTimeZone(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcalendarcopytimezone(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcalendarcopytimezone(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcalendarcopytimezone%28_%3A%29.json'
content_hash: 'sha256:fd1202327a6969f7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCalendarCopyTimeZone(_:)

<sub>Function</sub>

Returns a time zone object for a specified calendar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCalendarCopyTimeZone(_ calendar: CFCalendar!) -> CFTimeZone!
```

## Parameters

- `calendar` — The calendar to examine.

## Return Value

A copy of the time zone object for the specified calendar. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Getting and Setting the Time Zone

- [CFCalendarSetTimeZone](<cfcalendarsettimezone(____).md>) — Sets the time zone for a calendar.

---
title: 'CFCalendarCopyLocale(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcalendarcopylocale(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcalendarcopylocale(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcalendarcopylocale%28_%3A%29.json'
content_hash: 'sha256:ddd035e727ac537f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCalendarCopyLocale(_:)

<sub>Function</sub>

Returns a locale object for a specified calendar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCalendarCopyLocale(_ calendar: CFCalendar!) -> CFLocale!
```

## Parameters

- `calendar` — The calendar to examine.

## Return Value

A copy of the locale object for the specified calendar. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Getting and Setting the Locale

- [CFCalendarSetLocale](<cfcalendarsetlocale(____).md>) — Sets the locale for a calendar.

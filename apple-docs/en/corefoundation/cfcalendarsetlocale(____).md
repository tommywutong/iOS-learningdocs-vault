---
title: 'CFCalendarSetLocale(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcalendarsetlocale(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcalendarsetlocale(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcalendarsetlocale%28_%3A_%3A%29.json'
content_hash: 'sha256:d17e1368b8b0434a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCalendarSetLocale(_:_:)

<sub>Function</sub>

Sets the locale for a calendar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCalendarSetLocale(_ calendar: CFCalendar!, _ locale: CFLocale!)
```

## Parameters

- `calendar` — The calendar to modify.

- `locale` — The locale to set for `calendar`.

## See Also

### Getting and Setting the Locale

- [CFCalendarCopyLocale](<cfcalendarcopylocale(__).md>) — Returns a locale object for a specified calendar.

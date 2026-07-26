---
title: veryShortWeekdaySymbols
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/veryshortweekdaysymbols
source_url: 'https://developer.apple.com/documentation/foundation/calendar/veryshortweekdaysymbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/veryshortweekdaysymbols.json'
content_hash: 'sha256:ba320c9b162cdaad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# veryShortWeekdaySymbols

<sub>Instance Property</sub>

A list of very-shortly-named weekdays in this calendar, localized to the Calendar’s `locale`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var veryShortWeekdaySymbols: [String] { get }
```

## Discussion

For example, for English in the Gregorian calendar, returns `["S", "M", "T", "W", "T", "F", "S"]`.

> [!note] Note
> By default, Calendars have no locale set. If you wish to receive a localized answer, be sure to set the `locale` property first - most likely to `Locale.autoupdatingCurrent`.

## See Also

### Getting Weekday Symbols

- [weekdaySymbols](weekdaysymbols.md) — A list of weekdays in this calendar, localized to the Calendar’s `locale`.
- [shortWeekdaySymbols](shortweekdaysymbols.md) — A list of shorter-named weekdays in this calendar, localized to the Calendar’s `locale`.
- [standaloneWeekdaySymbols](standaloneweekdaysymbols.md) — A list of standalone weekday names in this calendar, localized to the Calendar’s `locale`.
- [shortStandaloneWeekdaySymbols](shortstandaloneweekdaysymbols.md) — A list of shorter-named standalone weekdays in this calendar, localized to the Calendar’s `locale`.
- [veryShortStandaloneWeekdaySymbols](veryshortstandaloneweekdaysymbols.md) — A list of very-shortly-named weekdays in this calendar, localized to the Calendar’s `locale`.

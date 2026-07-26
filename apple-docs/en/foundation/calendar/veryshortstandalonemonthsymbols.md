---
title: veryShortStandaloneMonthSymbols
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/veryshortstandalonemonthsymbols
source_url: 'https://developer.apple.com/documentation/foundation/calendar/veryshortstandalonemonthsymbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/veryshortstandalonemonthsymbols.json'
content_hash: 'sha256:a95d276ee28ac174'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# veryShortStandaloneMonthSymbols

<sub>Instance Property</sub>

A list of very-shortly-named standalone months in this calendar, localized to the Calendar’s `locale`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var veryShortStandaloneMonthSymbols: [String] { get }
```

## Discussion

For example, for English in the Gregorian calendar, returns `["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"]`.

> [!note] Note
> Stand-alone properties are for use in places like calendar headers. Non-stand-alone properties are for use in context (for example, “Saturday, November 12th”).

> [!note] Note
> By default, Calendars have no locale set. If you wish to receive a localized answer, be sure to set the `locale` property first - most likely to `Locale.autoupdatingCurrent`.

## See Also

### Getting Month Symbols

- [monthSymbols](monthsymbols.md) — A list of months in this calendar, localized to the Calendar’s `locale`.
- [shortMonthSymbols](shortmonthsymbols.md) — A list of shorter-named months in this calendar, localized to the Calendar’s `locale`.
- [veryShortMonthSymbols](veryshortmonthsymbols.md) — A list of very-shortly-named months in this calendar, localized to the Calendar’s `locale`.
- [standaloneMonthSymbols](standalonemonthsymbols.md) — A list of standalone months in this calendar, localized to the Calendar’s `locale`.
- [shortStandaloneMonthSymbols](shortstandalonemonthsymbols.md) — A list of shorter-named standalone months in this calendar, localized to the Calendar’s `locale`.

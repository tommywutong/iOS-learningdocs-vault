---
title: standaloneQuarterSymbols
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/standalonequartersymbols
source_url: 'https://developer.apple.com/documentation/foundation/calendar/standalonequartersymbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/standalonequartersymbols.json'
content_hash: 'sha256:ab5ca362a7b1871a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# standaloneQuarterSymbols

<sub>Instance Property</sub>

A list of standalone quarter names in this calendar, localized to the Calendar’s `locale`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var standaloneQuarterSymbols: [String] { get }
```

## Discussion

For example, for English in the Gregorian calendar, returns `["1st quarter", "2nd quarter", "3rd quarter", "4th quarter"]`.

> [!note] Note
> Stand-alone properties are for use in places like calendar headers. Non-stand-alone properties are for use in context (for example, “Saturday, November 12th”).

> [!note] Note
> By default, Calendars have no locale set. If you wish to receive a localized answer, be sure to set the `locale` property first - most likely to `Locale.autoupdatingCurrent`.

## See Also

### Getting Quarter Symbols

- [quarterSymbols](quartersymbols.md) — A list of quarter names in this calendar, localized to the Calendar’s `locale`.
- [shortQuarterSymbols](shortquartersymbols.md) — A list of shorter-named quarters in this calendar, localized to the Calendar’s `locale`.
- [shortStandaloneQuarterSymbols](shortstandalonequartersymbols.md) — A list of shorter-named standalone quarters in this calendar, localized to the Calendar’s `locale`.

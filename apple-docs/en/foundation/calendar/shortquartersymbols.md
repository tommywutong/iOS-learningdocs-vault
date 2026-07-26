---
title: shortQuarterSymbols
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/shortquartersymbols
source_url: 'https://developer.apple.com/documentation/foundation/calendar/shortquartersymbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/shortquartersymbols.json'
content_hash: 'sha256:0d64676d4d4e8f53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# shortQuarterSymbols

<sub>Instance Property</sub>

A list of shorter-named quarters in this calendar, localized to the Calendar’s `locale`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var shortQuarterSymbols: [String] { get }
```

## Discussion

For example, for English in the Gregorian calendar, returns `["Q1", "Q2", "Q3", "Q4"]`.

> [!note] Note
> By default, Calendars have no locale set. If you wish to receive a localized answer, be sure to set the `locale` property first - most likely to `Locale.autoupdatingCurrent`.

## See Also

### Getting Quarter Symbols

- [quarterSymbols](quartersymbols.md) — A list of quarter names in this calendar, localized to the Calendar’s `locale`.
- [standaloneQuarterSymbols](standalonequartersymbols.md) — A list of standalone quarter names in this calendar, localized to the Calendar’s `locale`.
- [shortStandaloneQuarterSymbols](shortstandalonequartersymbols.md) — A list of shorter-named standalone quarters in this calendar, localized to the Calendar’s `locale`.

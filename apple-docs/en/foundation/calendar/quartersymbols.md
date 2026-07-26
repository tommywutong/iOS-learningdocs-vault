---
title: quarterSymbols
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/quartersymbols
source_url: 'https://developer.apple.com/documentation/foundation/calendar/quartersymbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/quartersymbols.json'
content_hash: 'sha256:4ea54d3a9ffd38fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# quarterSymbols

<sub>Instance Property</sub>

A list of quarter names in this calendar, localized to the Calendar’s `locale`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var quarterSymbols: [String] { get }
```

## Discussion

For example, for English in the Gregorian calendar, returns `["1st quarter", "2nd quarter", "3rd quarter", "4th quarter"]`.

> [!note] Note
> By default, Calendars have no locale set. If you wish to receive a localized answer, be sure to set the `locale` property first - most likely to `Locale.autoupdatingCurrent`.

## See Also

### Getting Quarter Symbols

- [shortQuarterSymbols](shortquartersymbols.md) — A list of shorter-named quarters in this calendar, localized to the Calendar’s `locale`.
- [standaloneQuarterSymbols](standalonequartersymbols.md) — A list of standalone quarter names in this calendar, localized to the Calendar’s `locale`.
- [shortStandaloneQuarterSymbols](shortstandalonequartersymbols.md) — A list of shorter-named standalone quarters in this calendar, localized to the Calendar’s `locale`.

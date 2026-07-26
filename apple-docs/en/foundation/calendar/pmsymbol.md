---
title: pmSymbol
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/pmsymbol
source_url: 'https://developer.apple.com/documentation/foundation/calendar/pmsymbol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/pmsymbol.json'
content_hash: 'sha256:28dc211e9b121801'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# pmSymbol

<sub>Instance Property</sub>

The symbol used to represent “PM”, localized to the Calendar’s `locale`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var pmSymbol: String { get }
```

## Discussion

For example, for English in the Gregorian calendar, returns `"PM"`.

> [!note] Note
> By default, Calendars have no locale set. If you wish to receive a localized answer, be sure to set the `locale` property first - most likely to `Locale.autoupdatingCurrent`.

## See Also

### Getting AM and PM symbols

- [amSymbol](amsymbol.md) — The symbol used to represent “AM”, localized to the Calendar’s `locale`.

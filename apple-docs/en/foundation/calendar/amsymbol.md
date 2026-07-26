---
title: amSymbol
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/amsymbol
source_url: 'https://developer.apple.com/documentation/foundation/calendar/amsymbol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/amsymbol.json'
content_hash: 'sha256:b72af57e62f5a7f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# amSymbol

<sub>Instance Property</sub>

The symbol used to represent “AM”, localized to the Calendar’s `locale`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var amSymbol: String { get }
```

## Discussion

For example, for English in the Gregorian calendar, returns `"AM"`.

> [!note] Note
> By default, Calendars have no locale set. If you wish to receive a localized answer, be sure to set the `locale` property first - most likely to `Locale.autoupdatingCurrent`.

## See Also

### Getting AM and PM symbols

- [pmSymbol](pmsymbol.md) — The symbol used to represent “PM”, localized to the Calendar’s `locale`.

---
title: eraSymbols
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/erasymbols
source_url: 'https://developer.apple.com/documentation/foundation/calendar/erasymbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/erasymbols.json'
content_hash: 'sha256:7f0b262ffd86869a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# eraSymbols

<sub>Instance Property</sub>

A list of eras in this calendar, localized to the Calendar’s `locale`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var eraSymbols: [String] { get }
```

## Discussion

For example, for English in the Gregorian calendar, returns `["BC", "AD"]`.

> [!note] Note
> By default, Calendars have no locale set. If you wish to receive a localized answer, be sure to set the `locale` property first - most likely to `Locale.autoupdatingCurrent`.

## See Also

### Getting Era Symbols

- [longEraSymbols](longerasymbols.md) — A list of longer-named eras in this calendar, localized to the Calendar’s `locale`.

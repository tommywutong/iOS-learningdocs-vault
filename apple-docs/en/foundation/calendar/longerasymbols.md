---
title: longEraSymbols
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/longerasymbols
source_url: 'https://developer.apple.com/documentation/foundation/calendar/longerasymbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/longerasymbols.json'
content_hash: 'sha256:a0b9611542599645'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# longEraSymbols

<sub>Instance Property</sub>

A list of longer-named eras in this calendar, localized to the Calendar’s `locale`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var longEraSymbols: [String] { get }
```

## Discussion

For example, for English in the Gregorian calendar, returns `["Before Christ", "Anno Domini"]`.

> [!note] Note
> By default, Calendars have no locale set. If you wish to receive a localized answer, be sure to set the `locale` property first - most likely to `Locale.autoupdatingCurrent`.

## See Also

### Getting Era Symbols

- [eraSymbols](erasymbols.md) — A list of eras in this calendar, localized to the Calendar’s `locale`.
